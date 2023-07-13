def lambda_handler(event, context):
    message = "Hello LocalStack!"
    print(f"{message=}")
    return {"message": message}
