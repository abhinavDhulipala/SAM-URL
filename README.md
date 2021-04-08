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

The above should be all the documentation you _need_ inorder to contribute/solve to the assignment. Off course, feel
free to use any other resources or tutorials you find helpful :)

Please create a local_constants.py file for all environment variables specific to your project, including:

```python
 AWS_PROFILE = '<your_local_profile_name>'
 DEPLOYED_GATEWAY = 'the.public.url.of.your.function.'
```

Before we get into deployment, we’d like to provide a high-level overview of the whole project. There are multiple components with this:

1. Starting the Home Page, the files for this aspect can be found within the Flask application. Essentially, all this is doing is creating a basic interface for the user to interact with.
2. The Flask application is, in turn, deployed on Elastic Beanstalk. The steps for this deployment will be described later below. Basically, Elastic Beanstalk offers a service to deploy and scale web applications. This can be done in a variety of languages (Java, Python, Node.js). You can read more about this at https://aws.amazon.com/elasticbeanstalk/ .
3. In the IAM roles, we are giving the application Create, Read, Update, and Delete access to the DynamoDB.
4. Then, in the DynamoDB, we are storing the key, value pairs (the key is the hash and the value is the original url inputted by the user).
5. Now, we can look at it from the user perspective. The hash generated creates a tiny url for the user to be able to access the original website. The user, then, creates an HTTP get request on the created tiny url (this is done by simply clicking the URL). This get request is processed in the Amazon API Gateway which, using the tiny url, gets the query_param “hash”.
6. From that, it creates an event in the lambda redirect function. Because this function has Read Access to the DynamoDB, it is able to uncover the original url. Thus, it redirects the tiny url to the original url.
7. At the same time, there is a record of the times in which the tiny url is called within the Amazon CloudWatch logs.
