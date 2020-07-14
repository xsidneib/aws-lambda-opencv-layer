# OpenCv 4.2 AWS Lambda Layer 

This small project is to help who is trying to deploy OpenCv apps using AWS lambdas and have facing issues.

In this repo, we are using the [AWS SAM Client](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)
to deploy serverless applications to AWS platform. The AWS SAM definition can be found [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html).

I spent couple hours trying to understand why my `sam build` was failing when I realised that was about the OpenCV 
version I was using in the `requirements.txt`. If you follow the internet tutorials, you will see that they use the
`4.2.0.x` which works correct with AWS Lambda Layers. However, when building from local, it sometimes try to get the
version `4.3.0`, which fails. 

So basically, use the latest `4.2.0.x` and enjoy.

## Requirements
+ OpenCV version `4.2.0`
+ Python version `3.6`

## Building the example

When running the `sam build` it will automatically pack each resource and its dependencies and that applies to lambdas
layers as well. 


    sam build -t template.yaml

It will take a while (~5 min) as it downloads and installs the OpenCV and its dependencies in a local package.

 
## Deploying the example

As we're using sam, the deployment is straight forward. The only think you need is to make sure you have the AWS access
key configured accordingly. Please take a look at [`awsume`](https://awsu.me/) if you need to handle multiple AWS Credentials 

    profile=<myprofile>
    eval $(awsume -s $profile)
    sam deploy --guided

The first time, it will create the `samconfig.toml` file. This file contains all the information about the stack for the 
further updates. It might a good idea to add this file to your version control.

Please note the `<stackName>` you must be unique.

## Cleaning the mess

To remove all the resources creates need to use the aws client command:


    aws cloudformation delete-stack --stack-name <stackName>

    

# Troubleshooting

+ Issues with python version?  Use the containerized build by adding the `--use-container` option.


# References
+ [AWS Serverless Application Model (AWS SAM)](https://github.com/awslabs/serverless-application-model)
+ [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
+ [Open CV](https://opencv.org)
+ [asume](https://awsu.me/)
