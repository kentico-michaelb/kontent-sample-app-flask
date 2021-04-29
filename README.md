# Kentico Kontent sample Flask application

This is a sample Flask app that uses the [Kentico Kontent Python SDK](#https://github.com/kentico-michaelb/kontent-delivery-python-sdk) to retrieve content from Kentico Kontent.

This application uses the Dancing Goat sample project within Kentico Kontent. If you don't have your own Sample Project, any administrator of a Kentico Kontent subscription [can generate one](https://app.kontent.ai/sample-project-generator).

If you find a bug in the sample or have a feature request, please submit a GitHub issue.

## Table of Contents
- [Getting started](#Getting-started)
  - [Connecting to your Sample Project](#Connecting-to-your-Sample-Project)

## Getting started
We recommend running this sample application using virtual environment tooling such as [virtualenv](https://virtualenv.pypa.io/en/latest/).

To run the application:
1. Clone the app repository with your favorite GIT client
2. Add your Kontent Project ID key to `config.py` in the project root - detailed instructions available [below](#connecting-to-your-sample-project)
3. Install the project dependencies: `pip install -r requirements.txt`
4. Set the FLASK_APP environment variable: `set FLASK_APP=sample`
5. Install the application using `pip install -e .` (including the period)
6. Run the application: `flask run`

### Connecting to your Sample Project
If you already have a [Kentico Kontent account](https://app.kontent.ai), you can connect this application to your version of the Sample project.

1. In Kentico Kontent, choose Project settings from the app menu
1. Under Development, choose API keys and copy the Project ID
1. Open the `config.py` file
1. Use the values from your Kentico Kontent project as the `project_id` value
1. Save the changes