import boto3
from datetime import datetime, timedelta

# Initialize Cost Explorer client
ce = boto3.client('ce')

# Define time period for the report
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

def get_cost_and_usage(start_date, end_date):
    try:
        response = ce.get_cost_and_usage(
            TimePeriod={'Start': start_date, 'End': end_date},
            Granularity='DAILY',
            Metrics=['UnblendedCost', 'UsageQuantity'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'},
                {'Type': 'DIMENSION', 'Key': 'REGION'}
            ]
        )
        return response['ResultsByTime']
    except Exception as e:
        print(f"Error fetching cost and usage data: {e}")
        return None

# Fetch cost and usage data
cost_usage_data = get_cost_and_usage(start_date, end_date)

# Process and display the data
if cost_usage_data:
    for day_data in cost_usage_data:
        print(f"Date: {day_data['TimePeriod']['Start']}")
        for group in day_data['Groups']:
            service, region = group['Keys']
            amount = group['Metrics']['UnblendedCost']['Amount']
            usage = group['Metrics']['UsageQuantity']['Amount']
            print(f"  Service: {service}, Region: {region}, Cost: ${amount}, Usage: {usage}")
else:
    print("No data available.")

