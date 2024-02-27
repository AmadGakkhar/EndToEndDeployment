# EndToEndDeployment

## Create a Template for Folder Strcture
Created template.py and created a barebones project structure.

## Setting up Environment
Created virtual environment and updated requirements.txt. Added ("-e .") at the end of requirements.txt.
This is because we want to use this as our local package and we want to utilize setup.py. Due to this ("-e .") our package will be installed.

According to ChatGPT:

"Certainly! In simpler terms, when you have -e . in the requirements.txt file of a Python project, it means that instead of installing the project like a regular Python package, it should be installed in a way that any changes you make to the code immediately take effect without needing to reinstall.

It's like telling the Python package manager (pip): "Hey, when you install this project, do it in a way that I can easily modify the code, and those changes will be automatically reflected without reinstalling the package."

This is often used during development to streamline the testing and modification process."

