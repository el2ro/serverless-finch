from __future__ import print_function
import urllib
import zipfile
import boto3
import io

#
# Python code was copied from https://medium.com/@johnpaulhayes/how-extract-a-huge-zip-file-in-an-amazon-s3-bucket-by-using-aws-lambda-and-python-e32c6cf58f06
#

def hello(event, context):
  zip_key = "archive.zip"
  bucket = "flinch-s3-test-bucket"
  s3_resource = boto3.resource('s3')
  zip_obj = s3_resource.Object(bucket_name=bucket, key=zip_key)
  buffer = io.BytesIO(zip_obj.get()["Body"].read())

  z = zipfile.ZipFile(buffer)
  for filename in z.namelist():
    file_info = z.getinfo(filename)
    s3_resource.meta.client.upload_fileobj(
      z.open(filename),
      Bucket=bucket,
      Key=f'{filename}'
    )
  return 'OK'
