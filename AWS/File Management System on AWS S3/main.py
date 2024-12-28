# I imported the necessary libraries to work with AWS S3 and manage environment variables.
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

# I loaded the environment variables from the .env file using the dotenv library.
load_dotenv()

# I retrieved my AWS credentials and bucket name from the environment variables.
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

# I initialized the S3 client to connect to my AWS account and manage my S3 bucket.
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# I defined a function to upload a file to my S3 bucket.
def upload_file_to_s3(file_name, bucket, object_name=None):
    # If no object name is provided, I use the file name.
    if object_name is None:
        object_name = file_name
    try:
        # I uploaded the file to the specified S3 bucket.
        s3.upload_file(file_name, bucket, object_name)
        print(f"I successfully uploaded {file_name} to {bucket} as {object_name}.")
    except NoCredentialsError:
        print("I encountered a problem: AWS credentials are missing or incorrect.")
    except Exception as e:
        print(f"I encountered an error: {e}")

# I defined a function to list all the files in my S3 bucket.
def list_files_in_s3(bucket):
    try:
        # I retrieved the list of objects from the specified S3 bucket.
        response = s3.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            print("Here are the files in your bucket:")
            for obj in response['Contents']:
                # I printed each file name and its size in the bucket.
                print(f" - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("I didn't find any files in the bucket.")
    except Exception as e:
        print(f"I encountered an error: {e}")

# I defined a function to delete a file from my S3 bucket.
def delete_file_from_s3(bucket, object_name):
    try:
        # I deleted the specified file from the S3 bucket.
        s3.delete_object(Bucket=bucket, Key=object_name)
        print(f"I successfully deleted {object_name} from {bucket}.")
    except Exception as e:
        print(f"I encountered an error: {e}")

# I provided some examples of how to use these functions.
if __name__ == "__main__":
    # I uploaded a sample file to the S3 bucket.
    upload_file_to_s3('example.txt', BUCKET_NAME)

    # I listed all the files currently in the S3 bucket.
    list_files_in_s3(BUCKET_NAME)

    # I deleted a specific file from the S3 bucket.
    delete_file_from_s3(BUCKET_NAME, 'example.txt')
