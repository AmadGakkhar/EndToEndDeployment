Replicated from entbappy/cnnClassifier

# EndToEndDeployment

## Create a Template for Folder Structure
Created template.py and created a barebones project structure.

## Setting up Environment
Created virtual environment and updated requirements.txt. Added ("-e .") at the end of requirements.txt.
This is because we want to use this as our local package and we want to utilize setup.py. Due to this ("-e .") our package will be installed.

According to ChatGPT:

"Certainly! In simpler terms, when you have -e . in the requirements.txt file of a Python project, it means that instead of installing the project like a regular Python package, it should be installed in a way that any changes you make to the code immediately take effect without needing to reinstall.

It's like telling the Python package manager (pip): "Hey, when you install this project, do it in a way that I can easily modify the code, and those changes will be automatically reflected without reinstalling the package."

This is often used during development to streamline the testing and modification process."

## Setting up Log

Created custom Log. Code in src/EndtoEndDeployment/__init__.py
Tested it using test .py in root.

## Setting up utilities

Created src/EndtoEndDeployment/utils/common.py to write some common utility functions.

*ConfigBox provides easy way to access dict elements. For Example for a dict d = {"key" : "value", "key1" : "value1"}, d.key will give error but for d2 = ConfigBox({"key" : "value", "key1" : "value1"}), d2.key will work.

** @ensure_annotation decorator enforces the data types of a function. i.e if any other data type is encountered it will make sure that an error is raised.

## Setting Up Data Ingestion

 ### Standard Workflow

1. Update config/config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update Entity
5. Update Configuration Manager in src/config
6. Update Components
7. Update Pipeline
8. Update main.py




    1. **Update config/config.yaml**

        We will be adding configuration related to data ingestion. In this particular project, we are creating artifacts folder in which we will store our data. We are setting certain attributes like source url, downloaded zip name, unzip dir etc.

    2. **Update secrets.yaml [optional]**

        Don't have any secrets.

    3. **Update params.yaml**

        Don't have any model yet. Just add dummy value

    4. **Update Entity**

        Create a custom data type to hold all the entities of config.yaml file needed for data ingestion.
        Create src/EndToEndImplementation/entity/config_entity.py and store the created entity there.

    5. **Update Configuration Manager in src/config**

        Save config.yaml and params.yaml paths in src/EndToEndDeployment/constants/__init__.py.

        Create ConfigurationManager Class in **src/EndToEndDeployment/config/configuration.py** and write a method which return data ingestion configuration of the type we created in previous step. i.e DataIngestionConfig

    6. **Update Components**

        Create DataIngestion Class in **src/EndToEndDeployment/components/data_ingestion.py** which takes DataIngestionConfig object. It has methods for downloading the data, unzipping the data, cleaning the data etc. These functions can be changed according to project requirements.

    7. **Update Pipeline**

        Create src/EndToEndDeployment/pipeline/stage_01_data_ingestion.py. Import ConfigurationManager and DataIngestion Class along with logger.
        Create TrainingPipeline Class. Write its main function which tests the basic functionality uptil now.

    8. **Update main.py**
        
        Create main function which calls the pipeline

## Prepare Base Model -> Follow above mentioned Workflow for this step as well.

## Prepare Callbacks -> Created TF Callbacks. Follow the same Workflow.
## Prepare Training -> Created Training Pipeline. Follow the same Workflow.
## Prepare Evaluation -> Created Evaluation Pipeline. Follow the same Workflow.
## Created UI using FlaskAPI

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/catdog

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
