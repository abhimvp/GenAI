from datetime import (
    datetime,
)  # to save the generated code with today's date into s3 bucket
import json
import boto3
import botocore.config


def generate_code_using_bedrock(message: str, language: str) -> str:
    """message : we send this from postman to API Gateway & API-GW is going to forward the message here along with langugae
    message : code a binary search tree for me, language : python -. returns a string"""

    prompt_text = f"""
    Human: Write {language} code for the following instructions : {message}
    Assistant:
    """
    body = {
        "prompt": prompt_text,
        "max_tokens_to_sample": 2048,
        "temparature": 0.1,
        "top_k": 250,
        "top_p": 0.2,
        "stop_sequence": [
            "\n\nHuman:"
        ],  # here we're telling that human is speaking& if it sees Human, it should generate code
    }
    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="us-west-2",
            config=botocore.config.Config(
                read_timeout=300, retries={"max_attempts": 3}
            ),
        )
        response = bedrock.invoke(
            body=json.dumps(body), modelId="anthropic.claude-3-sonnet-20240229-v1:0"
        )
        response_content = response.get("body").read().decode("utf-8")
        response_data = json.loads(response_content)  # json string to python obj
        code = response_data["completion"].strip()
        return code
    except Exception as e:
        print(f"Error generating the code: {e}")
        return ""


def save_code_to_s3_bucket(code, s3_bucket, s3_key):
    """_summary_

    Args:
        code (_type_): _description_
        s3_bucket (_type_): _description_
        s3_key (_type_): _description_
    """

    s3 = boto3.client("s3")

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=code)
        print("Code saved to s3")

    except Exception as e:
        print(f"Error when saving the code to s3 {e}")


def lambda_handler(event, context):
    """_summary_

    Args:
        event (_type_): _description_
        context (_type_): _description_

    Returns:
        _type_: _description_
    """
    event = json.loads(event["body"])
    message = event["message"]
    language = event["key"]
    print(message, language)

    generated_code = generate_code_using_bedrock(message, language)

    if generated_code:
        current_time = datetime.now().strftime("%H%M%S")
        s3_key = f"code-output/{current_time}.py"
        s3_bucket = "bedrock-course-bucket"

        save_code_to_s3_bucket(generated_code, s3_bucket, s3_key)

    else:
        print("No code was generated")

    return {"statusCode": 200, "body": json.dumps("Code generation complete")}
