#!/bin/bash

echo "AWS Resource Management and Teardown Script"

# Function to list VPCs
list_vpcs() {
    echo "Available VPCs:"
    aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,CidrBlock,Tags[?Key==`Name`].Value|[0],IsDefault]' --output table
}

# Function to manage EC2 instances
manage_ec2_instances() {
    echo "Listing all EC2 instances..."
    aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,Tags[?Key==`Name`].Value|[0]]' --output table
    read -p "Enter the Instance ID you want to terminate or press enter to skip: " instance_id
    if [ -n "$instance_id" ]; then
        aws ec2 terminate-instances --instance-ids "$instance_id"
        echo "Terminating instance $instance_id"
    else
        echo "Skipping EC2 instance termination."
    fi
}

# Function to manage S3 buckets
manage_s3_buckets() {
    echo "Listing all S3 buckets..."
    aws s3api list-buckets --query 'Buckets[*].Name' --output table
    read -p "Enter the S3 bucket name you want to delete or press enter to skip: " bucket_name
    if [ -n "$bucket_name" ]; then
        aws s3 rb "s3://$bucket_name" --force
        echo "Deleting bucket $bucket_name"
    else
        echo "Skipping S3 bucket deletion."
    fi
}

# Function to delete NAT Gateways and release associated Elastic IPs
delete_nat_gateways() {
    echo "Deleting NAT Gateways in VPC $vpc_id..."
    nat_ids=$(aws ec2 describe-nat-gateways --filter "Name=vpc-id,Values=$vpc_id" --query 'NatGateways[*].NatGatewayId' --output text)
    for id in $nat_ids; do
        echo "Deleting NAT Gateway: $id"
        aws ec2 delete-nat-gateway --nat-gateway-id $id
    done
    echo "Waiting for NAT Gateways to be deleted..."
    sleep 60  # Adjust based on your AWS environment
}

# Function to detach and delete Internet Gateways
delete_internet_gateways() {
    echo "Detaching and Deleting Internet Gateways in VPC $vpc_id..."
    igw_ids=$(aws ec2 describe-internet-gateways --filter "Name=attachment.vpc-id,Values=$vpc_id" --query 'InternetGateways[*].InternetGatewayId' --output text)
    for id in $igw_ids; do
        aws ec2 detach-internet-gateway --internet-gateway-id $id --vpc-id $vpc_id
        aws ec2 delete-internet-gateway --internet-gateway-id $id
    done
}

# Function to delete Subnets
delete_subnets() {
    echo "Deleting Subnets in VPC $vpc_id..."
    subnet_ids=$(aws ec2 describe-subnets --filter "Name=vpc-id,Values=$vpc_id" --query 'Subnets[*].SubnetId' --output text)
    for id in $subnet_ids; do
        aws ec2 delete-subnet --subnet-id $id
    done
}

# Function to delete Route Tables
delete_route_tables() {
    echo "Deleting Route Tables in VPC $vpc_id..."
    rt_ids=$(aws ec2 describe-route-tables --filter "Name=vpc-id,Values=$vpc_id" --query 'RouteTables[?Associations[0].Main!=`true`].RouteTableId' --output text)
    for id in $rt_ids; do
        aws ec2 delete-route-table --route-table-id $id
    done
}

# Function to delete the VPC
delete_vpc() {
    echo "Deleting VPC: $vpc_id"
    aws ec2 delete-vpc --vpc-id $vpc_id
}

# Function to teardown AWS network infrastructure
teardown_network_infrastructure() {
    list_vpcs
    read -p "Enter the VPC ID you want to teardown: " vpc_id
    delete_nat_gateways
    delete_internet_gateways
    delete_subnets
    delete_route_tables
    delete_vpc
    echo "AWS network infrastructure teardown completed successfully."
}

# Main menu for resource management
while true; do
    echo "Select the resource type you want to manage:"
    echo "1. EC2 Instances"
    echo "2. S3 Buckets"
    echo "3. AWS Network Infrastructure Teardown"
    echo "4. Exit"
    read -p "Enter your choice (1-4): " choice

    case $choice in
        1) manage_ec2_instances ;;
        2) manage_s3_buckets ;;
        3) teardown_network_infrastructure ;;
        4) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid option, please enter a number between 1 and 4." ;;
    esac
done

