#!/bin/bash

echo "AWS Comprehensive Resource Inventory Script"

# Function to list EC2 instances
list_ec2_instances() {
    echo "EC2 Instances:"
    aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,Tags[?Key==`Name`].Value|[0]]' --output table
}

# Function to list S3 buckets
list_s3_buckets() {
    echo "S3 Buckets:"
    aws s3api list-buckets --query 'Buckets[*].Name' --output table
}

# Function to list NAT Gateways
list_nat_gateways() {
    echo "NAT Gateways:"
    aws ec2 describe-nat-gateways --query 'NatGateways[*].[NatGatewayId,VpcId,State,SubnetId]' --output table
}

# Function to list Internet Gateways
list_internet_gateways() {
    echo "Internet Gateways:"
    aws ec2 describe-internet-gateways --query 'InternetGateways[*].[InternetGatewayId,Attachments[0].VpcId]' --output table
}

# Function to list Subnets
list_subnets() {
    echo "Subnets:"
    aws ec2 describe-subnets --query 'Subnets[*].[SubnetId,VpcId,CidrBlock,AvailabilityZone]' --output table
}

# Function to list Route Tables
list_route_tables() {
    echo "Route Tables:"
    aws ec2 describe-route-tables --query 'RouteTables[*].[RouteTableId,VpcId]' --output table
}

# Function to list VPCs
list_vpcs() {
    echo "VPCs:"
    aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,CidrBlock,IsDefault]' --output table
}

# Function to list Elastic IPs
list_elastic_ips() {
    echo "Elastic IPs:"
    aws ec2 describe-addresses --query 'Addresses[*].[PublicIp,AllocationId,AssociationId,Domain]' --output table
}

# Function to list Security Groups
list_security_groups() {
    echo "Security Groups:"
    aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupId,GroupName,VpcId]' --output table
}

# Function to list RDS Databases
list_rds_databases() {
    echo "RDS Databases:"
    aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceStatus]' --output table
}

# Function to list Lambda Functions
list_lambda_functions() {
    echo "Lambda Functions:"
    aws lambda list-functions --query 'Functions[*].[FunctionName,Runtime]' --output table
}

# Function to list IAM Users
list_iam_users() {
    echo "IAM Users:"
    aws iam list-users --query 'Users[*].[UserName]' --output table
}

# Function to list CloudTrail Trails
list_cloudtrail_trails() {
    echo "CloudTrail Trails:"
    aws cloudtrail describe-trails --query 'trailList[*].[Name,S3BucketName]' --output table
}

# Function to list CloudWatch Log Groups
list_cloudwatch_log_groups() {
    echo "CloudWatch Log Groups:"
    aws logs describe-log-groups --query 'logGroups[*].[logGroupName,storedBytes]' --output table
}

# Main menu for resource listing
while true; do
    echo "Select the resource type you want to list:"
    echo "1. EC2 Instances"
    echo "2. S3 Buckets"
    echo "3. NAT Gateways"
    echo "4. Internet Gateways"
    echo "5. Subnets"
    echo "6. Route Tables"
    echo "7. VPCs"
    echo "8. Elastic IPs"
    echo "9. Security Groups"
    echo "10. RDS Databases"
    echo "11. Lambda Functions"
    echo "12. IAM Users"
    echo "13. CloudTrail Trails"
    echo "14. CloudWatch Log Groups"
    echo "15. List All"
    echo "16. Exit"
    read -p "Enter your choice (1-16): " choice

    case $choice in
        1) list_ec2_instances ;;
        2) list_s3_buckets ;;
        3) list_nat_gateways ;;
        4) list_internet_gateways ;;
        5) list_subnets ;;
        6) list_route_tables ;;
        7) list_vpcs ;;
        8) list_elastic_ips ;;
        9) list_security_groups ;;
        10) list_rds_databases ;;
        11) list_lambda_functions ;;
        12) list_iam_users ;;
        13) list_cloudtrail_trails ;;
        14) list_cloudwatch_log_groups ;;
        15)
            list_ec2_instances
            list_s3_buckets
            list_nat_gateways
            list_internet_gateways
            list_subnets
            list_route_tables
            list_vpcs
            list_elastic_ips
            list_security_groups
            list_rds_databases
            list_lambda_functions
            list_iam_users
            list_cloudtrail_trails
            list_cloudwatch_log_groups
            ;;
        16) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid option, please enter a number between 1 and 16." ;;
    esac
done