# CLAC-TinyURL
This will be the solution repo for a lab aiming to emulate the functionality of tinyurl

We will take inspiration of features from [this](https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR#div-stylecolorblack-background-colore2f4c7-border-radius5px-padding5px2-requirements-and-goals-of-the-systemdiv) link

Some important notes and dev links:

 - We reccomend using an IDE of some kind(PyCharm/VSCode/Atom). As students we get free access to the entire jetbrains toolbox. You can apply
for a student account [here](https://www.jetbrains.com/shop/eform/students)
 
 - We use the high level api everywhere we can.
   - The [Dynamo Resource API](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html) use resource
    **not** the client api
   - For developing and testing Lambdas we use [SAM](https://aws.amazon.com/serverless/sam/)
   - For questions about Lambda in general refer to the [AWS docs for lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
   - For connecting Lambda to the world see [API Gateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_api_mapping) 

The above should be all the documentation you *need* inorder to contribute/solve to the assignment. Off course, feel
free to use any other resources or tutorials you find helpful :)

Please create a local_constants.py file for all environment variables specific to your project, including:
``` python
 AWS_PROFILE = '<your_local_profile_name>'
```
