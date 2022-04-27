import json
import boto3
sm_client = boto3.client('sagemaker')
ssm_client = boto3.client('ssm')

def lambda_handler(event, context):

# Store relevant information to variables
    event_data = event['detail']['responseElements']['recordDetail']
    user_name = event['detail']['requestParameters']['provisioningParameters'][1]['value']
    notebook_name="%s-Notebook"%user_name

# Wait for notebook to become available
    waiter = sm_client.get_waiter('notebook_instance_in_service')
    waiter.wait(
        NotebookInstanceName=notebook_name,
        WaiterConfig={
            'Delay': 30,
            'MaxAttempts': 20
            }
        )
    print("Notebook Ready!")

# Create presigned URL using notebook_name
    generate_presigned_url = sm_client.create_presigned_notebook_instance_url(
        NotebookInstanceName=notebook_name,
        SessionExpirationDurationInSeconds=43200
    )
    ps_url = generate_presigned_url['AuthorizedUrl']

# Create SSM parameter to store user Notebook presigned url
    create_parameter = ssm_client.put_parameter(
        Name="/SageMaker/Notebooks/%s-Notebook"%user_name,
        Description='Presigned URL for user.',
        Value=ps_url,
        Type='String',
        Overwrite=True,
        Tier='Standard'
    )