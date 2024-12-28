import boto3
from botocore.exceptions import NoCredentialsError

# AWS Configuration
AWS_ACCESS_KEY = 'your_aws_access_key'
AWS_SECRET_KEY = 'your_aws_secret_key'
BUCKET_NAME = 'your_bucket_name'

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# Function to upload a file to S3
def upload_file(file_name, object_name=None):
    if object_name is None:
        object_name = file_name
    try:
        s3.upload_file(file_name, BUCKET_NAME, object_name)
        print(f"File '{file_name}' uploaded successfully to bucket '{BUCKET_NAME}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except NoCredentialsError:
        print("AWS credentials not available.")

# Function to list files in the S3 bucket
def list_files():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            print("Files in S3 bucket:")
            for obj in response['Contents']:
                print(f"- {obj['Key']}")
        else:
            print("No files found in the bucket.")
    except Exception as e:
        print(f"Error listing files: {e}")

# Function to delete a file from S3
def delete_file(object_name):
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=object_name)
        print(f"File '{object_name}' deleted successfully from bucket '{BUCKET_NAME}'.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Example Usage
if __name__ == "__main__":
    print("Cloud File Management System")
    print("1. Upload File")
    print("2. List Files")
    print("3. Delete File")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            file_name = input("Enter the file path to upload: ")
            upload_file(file_name)
        elif choice == '2':
            list_files()
        elif choice == '3':
            file_name = input("Enter the file name to delete: ")
            delete_file(file_name)
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
