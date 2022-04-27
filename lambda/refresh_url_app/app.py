import json
import boto3
sm_client = boto3.client('sagemaker')
ssm_client = boto3.client('ssm')

def lambda_handler(event, context):

# Store event data to variables.
    event_body = (event['body'])

# Convert event body to dictionary.
    event_dict = json.loads(event_body)

# Create new presigned URL. 
    notebook_user_name = event_dict["notebook_user_name"]
    notebook_name="%s-Notebook"%notebook_user_name
    refresh_presigned_url = sm_client.create_presigned_notebook_instance_url(
        NotebookInstanceName=notebook_name,
        SessionExpirationDurationInSeconds=3600
    )
    ps_url = refresh_presigned_url['AuthorizedUrl']

# Refresh SSM parameter with new presigned url
    update_parameter = ssm_client.put_parameter(
        Name="/SageMaker/Notebooks/%s-Notebook"%notebook_user_name,
        Description='Presigned URL for user.',
        Value=ps_url,
        Type='String',
        Overwrite=True,
        Tier='Standard'
    )

    # Return response to API Gateway.
    return {
        "isBase64Encoded": False,
        "headers": {},
        "statusCode": 200,
        "body": json.dumps({ "PreSignedURL": ps_url })
    }