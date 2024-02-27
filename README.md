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
- Update config/config.yaml

    We will be adding configuration related to data ingestion. In this particular project, we are creating artifacts folder in which we will store our data. We are setting certain attributes like source url, downloaded zip name, unzip dir etc.

- Update secrets.yaml [optional]

    Don't have any secrets.

- Update params.yaml

    Don't have any model yet. Just add dummy value

- Update entity

    Create a custom data type to hold all the entities of config.yaml file needed for data ingestion.
    Create src/EndToEndImplementation/entity/config_entity.py and store the created entity there.

- Update configuration manager in src/config

    Save config.yaml and params.yaml paths in src/EndToEndDeployment/constants/__init__.py.

    Create ConfigurationManager Class in **src/EndToEndDeployment/config/configuration.py** and write a method which return data ingestion configuration of the type we created in previous step. i.e DataIngestionConfig

- Update components

    Create DataIngestion Class in **src/EndToEndDeployment/components/data_ingestion.py** which takes DataIngestionConfig object. It has methods for downloading the data, unzipping the data, cleaning the data etc. These functions can be changed according to project requirements.

- Update pipeline

    Create src/EndToEndDeployment/pipeline/stage_01_data_ingestion.py. Import ConfigurationManager and DataIngestion Class along with logger.
    Create TrainingPipeline Class. Write its main function which tests the basic functionality uptil now.

- Update main.py
