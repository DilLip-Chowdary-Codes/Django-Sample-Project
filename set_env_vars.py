environment_variables = {
    'Variables': {
        "DJANGO_SETTINGS_MODULE": "todo.settings.prod",
        "SECRET_KEY": "mys3cr3tkey",
        "SQL_DB_NAME": "<DB Name>",
        "SQL_DB_USERNAME": "<DB Username>",
        "SQL_DB_PASSWORD": "<DB Password>",
        "SQL_DB_HOST": "<DB Host ex: https://mydomain.com>",
        "SQL_DB_PORT": "3306",
        "USE_S3_STATIC": "True",
        "CUSTOM_AWS_ACCESS_KEY_ID": "AWS Access Key",
        "CUSTOM_AWS_SECRET_ACCESS_KEY": "AWS secret access key",
        "AWS_STORAGE_BUCKET_NAME": "<s3 bucket for static files hosting>",
        "function": "django-sample-project-alpha"
    }
}

import boto3

lambda_client = boto3.client('lambda', region_name='ap-south-1')

print(lambda_client.update_function_configuration(FunctionName=environment_variables['Variables']['function'],
                                                  Environment=environment_variables))
