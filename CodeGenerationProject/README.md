# Code Generation Project - Architecture :

- we're going to create API Gateway Endpoints (Enables us to call AWS as an API) , we use Restfox/Postman to call API Gateway.
- API GW trigger Lambda Function.
- Lambda Function calls the Bedrock API with the specific model we want to and it's going to get to a response back from the Bedrock Model and it's going to save it into S3.
- In this project , we're going to give instructions to Bedrock as to what kind of code it should produce in what programming language & save the output to s3.

## steps :

- Create a Lambda Function
  - Author From Scratch
    - name : bedrock_code_generation
    - runtime : python 3.11
    - Create Function
  - Give us Execution Role - which can be found in configuration TAB.
- Execution Role 
    - Give it Administrator access , as this model is going to be talking with S3,Bedrock, monitoring with cloudwatch logs - Attach a Policy