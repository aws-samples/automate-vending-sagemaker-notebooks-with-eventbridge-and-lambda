# Automate vending SageMaker notebooks with EventBridge and Lambda
---

Having an environment capable of delivering Amazon SageMaker notebook instances quickly provides a means for data scientists and business analysts to efficiently respond to organizational needs.  

# Motivation
---

Data is the very lifeblood of an organization and the ability to analyze that data efficiently provides useful insights for businesses.  This article illustrates how to deliver SageMaker instance notebooks using AWS services including AWS CloudFormation, AWS Service Catalog, Amazon EventBridge, and AWS Lambda.  

# AWS Services Used
---

Let’s review the AWS services we are deploying with this project.

*CloudWatch* - [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (Amazon CloudWatch) is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers to provide data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health.  

*CloudFormation* - [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/) (AWS CloudFormation) is a platform service which provides a means to deliver AWS resources leveraging Infrastructure as Code to deliver repeatable and consistent solutions.

*AWS Service Catalog* - [AWS Service Catalog](https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc) (AWS Service Catalog) allows organizations the ability to quickly and efficiently provision predefined environments that are consistent with their organizational best practices by presenting to users a catalog of available services, applications, or environments to provide and deliver the solution.

*Amazon EventBridge* - [Amazon EventBridge](https://aws.amazon.com/eventbridge/) (Amazon EventBridge) is a serverless event bus.  It provides a platform to consolidate events from multiple logging streams or sources and define triggers for event based actions.

*AWS Lambda* - [AWS Lambda](https://aws.amazon.com/lambda/) (AWS Lambda) is a serverless code execution environment.  Lambda executes code or scripts in functions and provides a means to effectively reduce operational costs, optimize code execution to specific code environments, and reduce operational complexity associated with instance management.

## Dependencies
---

This CloudFormation template has dependencies or requirements in order to successfully deliver the desired state.  These dependencies include the following:

- An AWS account is required
- An execution role or IAM key is required for authentication with the AWS account

## Summary
---

This template is designed to provide a comprehensive deployment solution for SageMaker notebooks including the following component configurations:

- Cloudwatch - alert metrics defined
- CloudFormation - used to self-provision templates containing configurations for SageMaker instances
- Service Catalog - used to provide a means of requesting, managing, and terminating SageMaker resources
- EventBridge - used to provide event bus to respond to notebook provisioning events to trigger Lambda functions
- Lambda - used to execute code that delivers the pre-signed URL after the notebook resource is provisioned

**Please read the rest of this document prior to leveraging this template for delivery.**

## Usage
---

#### Get product metadata

```
aws servicecatalog describe-product-as-admin --id prod-1234567890
```

### Deployment
---


```
aws servicecatalog provision-product \
    --product-id prod-clkzyvlgv6lmo \
    --provisioned-product-name "demoProduct2" \
    --provisioning-artifact-id pa-g337l4ugplmpc \
    --provisioning-parameters Key=NotebookInstanceName,Value=myNotebookDemo Key=NotebookInstanceType,Value=ml.t3.medium Key=KMSStackName,Value=kms-config Key=NotebookUserName,Value=joe \
    --tags "Key"="Owner","Value"="awsjoe"
```

### Cleanup
---


```
aws servicecatalog terminate-provisioned-product --provisioned-product-id pp-1234567890
```

### Security
---

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

### License
---

This library is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file.


