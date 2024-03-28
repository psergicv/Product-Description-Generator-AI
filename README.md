# Product-Description-Generator-AI

## Overview
This is a Flask application that is generating a product descriptions based on the product name provided by user and the desired style of the description. It is integrated with an AI text generation service to create descriptions that can be humorous, brief, detailed, or professional.

## Installation
1. Clone the repository
```
git clone https://github.com/yourusername/product-description-generator.git
cd product-description-generator
```
2. Install the required Python packages:
```
pip install flask openai
```
3. Add API and App_Secret key in config.py:
```
api_key = ""
app_secret_key = ""
```
4. Start the Flask application:
```
flask run
```

## How To Use the App
1. After running the app, go to http://127.0.0.1:5000/index in your web browser.
2. Enter the Product Name and select the desired style for the description.
3. Click the "Creaza descrierea" button to generate the product description.
4. After, you will be redirect to a new page where you will find the generated description

