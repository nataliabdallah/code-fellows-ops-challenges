#!/bin/bash

set -u # Exit script if uninitialized variable is used

# Function to check command execution status
check_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed."
        exit 1
    fi
}

# Prompt for trail name
echo "Enter a name for the CloudTrail trail:"
read TRAIL_NAME

# Create S3 bucket for CloudTrail logs
echo "Creating S3 bucket for CloudTrail logs..."
aws s3 mb s3://"${TRAIL_NAME}-bucket"
check_status "Creating S3 bucket"

# Create a CloudTrail trail
echo "Creating CloudTrail trail..."
aws cloudtrail create-trail --name "$TRAIL_NAME" --s3-bucket-name "${TRAIL_NAME}-bucket" --is-multi-region-trail
check_status "Creating CloudTrail trail"

# Start logging
echo "Starting CloudTrail logging..."
aws cloudtrail start-logging --name "$TRAIL_NAME"
check_status "Starting CloudTrail logging"

# Enable CloudTrail to log events
echo "Enabling CloudTrail to log events..."
aws cloudtrail put-event-selectors --trail-name "$TRAIL_NAME" --event-selectors '[{"ReadWriteType": "All", "IncludeManagementEvents":true, "DataResources": [{"Type": "AWS::S3::Object","Values": ["arn:aws:s3:::'"${TRAIL_NAME}-bucket"'/*"]}]}]'
check_status "Enabling CloudTrail event logging"

# Configure CloudWatch to ingest log data from CloudTrail
echo "Configuring CloudWatch to ingest log data from CloudTrail..."
aws logs create-log-group --log-group-name "${TRAIL_NAME}-CloudWatch-Logs"
check_status "Configuring CloudWatch"

# Create CloudWatch rule
echo "Enter a name for the CloudWatch rule:"
read CW_RULE_NAME

echo "Enter the service name for the CloudWatch event pattern (e.g., ec2, s3):"
read SERVICE_NAME

echo "Enter the event type for the CloudWatch event pattern (e.g., AWS API Call via CloudTrail):"
read EVENT_TYPE

# Create CloudWatch rule
echo "Creating CloudWatch rule..."
aws events put-rule --name "$CW_RULE_NAME" --event-pattern "{\"source\":[\"aws.$SERVICE_NAME\"],\"detail-type\":[\"$EVENT_TYPE\"]}"
check_status "Creating CloudWatch rule"

# Prompt for VPC ID for creating VPC Flow Logs
echo "Enter your VPC ID to create VPC Flow Logs:"
read VPC_ID

# Prompt for S3 bucket name for VPC Flow Logs
echo "Enter the S3 bucket name for storing VPC Flow Logs:"
read FLOW_LOGS_BUCKET

# Create VPC Flow Log
echo "Creating VPC Flow Log..."
aws ec2 create-flow-logs --resource-type VPC --resource-ids "$VPC_ID" --traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::"$FLOW_LOGS_BUCKET"
check_status "Creating VPC Flow Log"

echo "Setup complete."
