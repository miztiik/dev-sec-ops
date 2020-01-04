def lambda_handler(event, context):
    import logging as log
    import cfnresponse
    import boto3
    log.getLogger().setLevel(log.INFO)

    # This needs to change if there are to be multiple resources
    # in the same stack
    physical_id = 'TheOnlyCustomResource'

    try:
        log.info('Input event: %s', event)

        # Check if this is a Create and we're failing Creates
        if event['RequestType'] == 'Create' and event['ResourceProperties'].get('FailCreate', False):
            raise RuntimeError('Create failure requested')

        # Do the thing
        # OriginalCode
        message = event['ResourceProperties']['Message']

        #MINE
        iam = boto3.client('iam')
        for i in message:
            if i.get('tags'):
                iam.tag_user(
                    UserName=i.get('user'),
                    Tags=i.get('tags')
                )
        #MINE

        attributes = {
            'Response': f"Message sent from function {message}"
        }

        cfnresponse.send(event, context, cfnresponse.SUCCESS, attributes, physical_id)
    except Exception as e:
        log.exception(e)
        # cfnresponse's error message is always "see CloudWatch"
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, physical_id)