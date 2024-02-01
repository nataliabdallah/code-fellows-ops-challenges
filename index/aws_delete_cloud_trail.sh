#!/bin/bash

set -u # Exit script if an uninitialized variable is used

# Function to list and delete CloudTrail trails
manage_cloudtrail() {
    echo "Available CloudTrail Trails:"
    aws cloudtrail describe-trails --query 'trailList[*].Name' --output table
    echo "Enter the name of the CloudTrail trail to delete (leave blank to skip):"
    read TRAIL_NAME
    if [ -n "$TRAIL_NAME" ]; then
        aws cloudtrail delete-trail --name "$TRAIL_NAME"
        echo "Trail $TRAIL_NAME deleted."
    fi
}

# Function to list and delete CloudWatch log groups
manage_cloudwatch_logs() {
    echo "Available CloudWatch Log Groups:"
    aws logs describe-log-groups --query 'logGroups[*].logGroupName' --output table
    echo "Enter the name of the CloudWatch Log Group to delete (leave blank to skip):"
    read LOG_GROUP_NAME
    if [ -n "$LOG_GROUP_NAME" ]; then
        aws logs delete-log-group --log-group-name "$LOG_GROUP_NAME"
        echo "Log group $LOG_GROUP_NAME deleted."
    fi
}

# Function to list and delete CloudWatch rules
manage_cloudwatch_rules() {
    echo "Available CloudWatch Rules:"
    aws events list-rules --query 'Rules[*].Name' --output table
    echo "Enter the name of the CloudWatch Rule to delete (leave blank to skip):"
    read RULE_NAME
    if [ -n "$RULE_NAME" ]; then
        aws events delete-rule --name "$RULE_NAME"
        echo "Rule $RULE_NAME deleted."
    fi
}

# Function to list and delete S3 buckets
manage_s3_buckets() {
    echo "Available S3 Buckets:"
    aws s3 ls
    echo "Enter the name of the S3 Bucket to delete (leave blank to skip):"
    read BUCKET_NAME
    if [ -n "$BUCKET_NAME" ]; then
        aws s3 rb s3://"$BUCKET_NAME" --force
        echo "Bucket $BUCKET_NAME deleted."
    fi
}

echo "Resource Deletion Script"
echo "========================"

manage_cloudtrail
manage_cloudwatch_logs
manage_cloudwatch_rules
manage_s3_buckets

echo "Resource deletion completed."
