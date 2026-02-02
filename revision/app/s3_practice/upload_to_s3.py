import os
import requests
import boto3


IMAGE_URL = "https://picsum.photos/seed/picsum/200/300"
LOCAL_DIR = "s3_practice"
LOCAL_FILE = "heorhii.jpg"
LOCAL_PATH = f"{LOCAL_DIR}/{LOCAL_FILE}"

os.makedirs(LOCAL_DIR, exist_ok=True)

response = requests.get(IMAGE_URL)
response.raise_for_status()

with open(LOCAL_PATH, "wb") as file:
    file.write(response.content)

BUCKET_NAME = "group11112025"
PUBLIC_URL = "https://pub-f8a0a61d58744db88283773e03043bb4.r2.dev"

s3 = boto3.client(
    "s3",
    region_name="EEUR",
    endpoint_url="https://8721af4803f2c3c631a90d8b64d397b7.r2.cloudflarestorage.com",
    aws_access_key_id="2ae25d402a48e45a66e8400661cb1e8f",
    aws_secret_access_key="32d65a0b27b9fb3789484262804a790c877a1257d96831a197f2cb182b616bdd",
)

S3_KEY = "images/heorhii.jpg"

s3.upload_file(
    LOCAL_PATH,
    BUCKET_NAME,
    S3_KEY
)

public_link = f"{PUBLIC_URL}/{S3_KEY}"

print(public_link)