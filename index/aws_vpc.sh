#!/bin/bash

echo "Starting AWS network infrastructure setup..."

# Function to validate CIDR block
validate_cidr() {
    local cidr=$1
    if ! echo "$cidr" | grep -E -q '^([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$'; then
        echo "Invalid CIDR block format: $cidr"
        exit 1
    fi
}

# Prompt user for VPC details and create VPC
read -p "Enter a name for your VPC: " vpc_name
read -p "Enter CIDR block for the VPC (e.g., 10.0.0.0/16): " vpc_cidr
validate_cidr "$vpc_cidr"
vpc_id=$(aws ec2 create-vpc --cidr-block "$vpc_cidr" --query 'Vpc.VpcId' --output text --tag-specifications "ResourceType=vpc,Tags=[{Key=Name,Value=$vpc_name}]")
echo "Created VPC with ID: $vpc_id"

# Prompt for public subnet details and create public subnet
read -p "Enter a name for your public subnet: " public_subnet_name
read -p "Enter CIDR block for the public subnet (e.g., 10.0.1.0/24): " public_subnet_cidr
validate_cidr "$public_subnet_cidr"
public_subnet_id=$(aws ec2 create-subnet --vpc-id "$vpc_id" --cidr-block "$public_subnet_cidr" --query 'Subnet.SubnetId' --output text --tag-specifications "ResourceType=subnet,Tags=[{Key=Name,Value=$public_subnet_name}]")
echo "Created public subnet with ID: $public_subnet_id"

# Enable auto-assign public IP for the public subnet
aws ec2 modify-subnet-attribute --subnet-id "$public_subnet_id" --map-public-ip-on-launch

# Prompt for private subnet details and create private subnet
read -p "Enter a name for your private subnet: " private_subnet_name
read -p "Enter CIDR block for the private subnet (e.g., 10.0.2.0/24): " private_subnet_cidr
validate_cidr "$private_subnet_cidr"
private_subnet_id=$(aws ec2 create-subnet --vpc-id "$vpc_id" --cidr-block "$private_subnet_cidr" --query 'Subnet.SubnetId' --output text --tag-specifications "ResourceType=subnet,Tags=[{Key=Name,Value=$private_subnet_name}]")
echo "Created private subnet with ID: $private_subnet_id"

# Create an Internet Gateway and attach it to the VPC
igw_id=$(aws ec2 create-internet-gateway --query 'InternetGateway.InternetGatewayId' --output text --tag-specifications "ResourceType=internet-gateway,Tags=[{Key=Name,Value=$vpc_name-igw}]")
aws ec2 attach-internet-gateway --vpc-id "$vpc_id" --internet-gateway-id "$igw_id"
echo "Created and attached Internet Gateway with ID: $igw_id"

# Create a route table for the public subnet and configure it
public_rt_id=$(aws ec2 create-route-table --vpc-id "$vpc_id" --query 'RouteTable.RouteTableId' --output text --tag-specifications "ResourceType=route-table,Tags=[{Key=Name,Value=$public_subnet_name-rt}]")
aws ec2 create-route --route-table-id "$public_rt_id" --destination-cidr-block 0.0.0.0/0 --gateway-id "$igw_id"
aws ec2 associate-route-table --route-table-id "$public_rt_id" --subnet-id "$public_subnet_id"
echo "Configured route table for public subnet with ID: $public_rt_id"

# Allocate an Elastic IP for the NAT Gateway
eip_allocation_id=$(aws ec2 allocate-address --domain vpc --query 'AllocationId' --output text)

# Create a NAT Gateway in the public subnet
nat_gw_id=$(aws ec2 create-nat-gateway --subnet-id "$public_subnet_id" --allocation-id "$eip_allocation_id" --query 'NatGateway.NatGatewayId' --output text --tag-specifications "ResourceType=natgateway,Tags=[{Key=Name,Value=$vpc_name-natgw}]")
echo "Created NAT Gateway with ID: $nat_gw_id. Waiting for it to become available..."
aws ec2 wait nat-gateway-available --nat-gateway-ids "$nat_gw_id"

# Create a route table for the private subnet and configure it
private_rt_id=$(aws ec2 create-route-table --vpc-id "$vpc_id" --query 'RouteTable.RouteTableId' --output text --tag-specifications "ResourceType=route-table,Tags=[{Key=Name,Value=$private_subnet_name-rt}]")
aws ec2 create-route --route-table-id "$private_rt_id" --destination-cidr-block 0.0.0.0/0 --nat-gateway-id "$nat_gw_id"
aws ec2 associate-route-table --route-table-id "$private_rt_id" --subnet-id "$private_subnet_id"
echo "Configured route table for private subnet with ID: $private_rt_id"

echo "AWS network infrastructure setup completed successfully."
