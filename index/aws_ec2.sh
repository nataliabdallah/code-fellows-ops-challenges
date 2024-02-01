#!/bin/bash

echo "Starting EC2 instance deployment..."

# List available VPCs and prompt user for selection
echo "Available VPCs:"
aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,Tags[?Key==`Name`].Value | [0]]' --output table
read -p "Enter the VPC ID from the above list where you want to launch the instance: " vpc_id

# List available subnets in the selected VPC and prompt user for selection
echo "Available Subnets in VPC $vpc_id:"
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$vpc_id" --query 'Subnets[*].[SubnetId,CidrBlock,Tags[?Key==`Name`].Value | [0]]' --output table
read -p "Enter the Subnet ID from the above list where you want to launch the instance: " subnet_id

# List available security groups in the selected VPC and prompt user for selection
echo "Available Security Groups in VPC $vpc_id:"
aws ec2 describe-security-groups --filters "Name=vpc-id,Values=$vpc_id" --query 'SecurityGroups[*].[GroupId,GroupName]' --output table
read -p "Enter the Security Group ID from the above list for the instance: " sg_id

# Prompt user for key pair name
read -p "Enter a name for the new key pair: " key_name

# Create the key pair and save the private key
echo "Creating key pair..."
key_output=$(aws ec2 create-key-pair --key-name "$key_name" --query 'KeyMaterial' --output text)
if [ $? -ne 0 ]; then
    echo "Key pair creation failed."
    exit 1
else
    echo "$key_output" > "${key_name}.pem"
    echo "Key pair '${key_name}' created successfully."
    chmod 400 "${key_name}.pem"
fi

# Prompt user for instance name
read -p "Enter a name for the EC2 instance: " instance_name

# Get the AMI ID for Ubuntu Server 20.04 LTS (HVM), SSD Volume Type
echo "Retrieving Ubuntu Server 20.04 LTS AMI ID..."
ami_id=$(aws ec2 describe-images --owners 099720109477 --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*" "Name=state,Values=available" --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' --output text)

# Launch the instance with the name tag
echo "Launching EC2 instance..."
instance_id=$(aws ec2 run-instances --image-id "$ami_id" --count 1 --instance-type t2.micro --key-name "$key_name" --security-group-ids "$sg_id" --subnet-id "$subnet_id" --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$instance_name}]" --query 'Instances[0].InstanceId' --output text)
echo "Launched instance with ID: $instance_id and Name: $instance_name"

echo "EC2 instance deployment completed successfully."
