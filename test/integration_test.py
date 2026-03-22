import json
import boto3
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Invoke California GIS Lambda function')
    parser.add_argument('--profile', default='redzilla-infra', 
                        help='AWS profile to use (default: redzilla-infra)')
    parser.add_argument('--function-name', default='dev-california-gis',
                        help='Lambda function name to invoke (default: dev-california-gis)')
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Define the payload with proper AddressKey format
    payload = [
        {
            "addressKey": {
                "address": "1600 Amphitheatre Parkway",
                "city": "Mountain View",
                "state": "CA",
                "zip": "94043"
            },
            "county": "Santa Clara",
            "latitudeHint": 37.422,
            "longitudeHint": -122.084
        }
    ]

    # Create Lambda client with specified profile
    session = boto3.Session(profile_name=args.profile)
    lambda_client = session.client('lambda')

    try:
        # Invoke Lambda function
        response = lambda_client.invoke(
            FunctionName=args.function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )

        # Get the payload from response and decode it
        result = json.loads(response['Payload'].read().decode())

        # Print the result
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Error invoking Lambda function: {e}")

if __name__ == "__main__":
    main()
