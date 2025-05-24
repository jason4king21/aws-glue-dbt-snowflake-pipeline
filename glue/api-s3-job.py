import boto3
import requests
import base64
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Example usage
github_url = "https://raw.githubusercontent.com/deacademygit/project-data/refs/heads/main/country_details.json"  # Raw file URL from GitHub
bucket_name = "jk-de-glueproject-bucket"  # The S3 bucket where the file will be uploaded
s3_key = "data/country_details.json"  # The key (path) in the S3 bucket

def fetch_data_from_github_and_upload_to_s3(github_url, bucket_name, s3_key):
    try:
        # Fetch the file content from GitHub (raw URL or GitHub API URL)
        response = requests.get(github_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the content from the response (for raw URL, it's already plain text or binary)
            file_content = response.content

            # Initialize the S3 client
            s3_client = boto3.client('s3')

            # Upload the file content to S3
            s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)
            print(f"File uploaded successfully to s3://{bucket_name}/{s3_key}")
        else:
            print(f"Error: Failed to fetch file from GitHub. Status code {response.status_code}")

    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: AWS credentials are missing or incomplete. {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the file from GitHub: {e}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

fetch_data_from_github_and_upload_to_s3(github_url, bucket_name, s3_key)