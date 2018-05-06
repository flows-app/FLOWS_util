import boto3
import json
import os
import uuid

S3 = boto3.client('s3')
DataBucket = os.environ.get("DataBucket")

def handler(event, context):
    print("event")
    print(event)
    print("context")
    print(context)

    objectname = str(uuid.uuid4())
    targeturl = S3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': DataBucket,
            'Key': objectname,
            'ContentType':'application/octet-stream',
        },
        ExpiresIn=3600,
        HttpMethod='PUT'
    )
    sourceurl = S3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': DataBucket,
            'Key': objectname
        },
        ExpiresIn=3600
    )
    result=[{"sourceurl":sourceurl,"targeturl":targeturl}]
    return result
