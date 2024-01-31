#!/bin/bash

echo "Starting creation of AWS Security Group and adding inbound rules..."

# Prompt user for VPC ID
read -p "Enter your VPC ID: " vpc_id

# Prompt user for Security Group Name
read -p "Enter the name for your Security Group: " sg_name

# Security Group Description
sg_description="Allow selective ports"

# Create Security Group
sg_id=$(aws ec2 create-security-group --group-name "$sg_name" --description "$sg_description" --vpc-id "$vpc_id" --query 'GroupId' --output text --tag-specifications "ResourceType=security-group,Tags=[{Key=Name,Value=$sg_name}]")
echo "Created Security Group '$sg_name' with ID: $sg_id"

# Define rules
declare -a rules=(
    "icmp -1 0.0.0.0/0"
    "tcp 22 0.0.0.0/0"
    "tcp 3389 0.0.0.0/0"
    "tcp 80 0.0.0.0/0"
    "tcp 443 0.0.0.0/0"
)

# Add inbound rules
for rule in "${rules[@]}"; do
    read -r proto port cidr <<< "$rule"
    aws ec2 authorize-security-group-ingress --group-id "$sg_id" --protocol "$proto" --port "$port" --cidr "$cidr"
    echo "Added inbound rule allowing $proto on port $port from $cidr to Security Group $sg_id"
done

echo "Security Group setup completed successfully."
