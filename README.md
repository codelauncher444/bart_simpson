This documentation will guide you through the steps to get the chatbot up and running on Huggingface Spaces. The chatbot is designed to act like Bart Simpson.

## Steps to Set Up the Chatbot

### Create a New Huggingface Space

1. Go to [Huggingface Spaces](https://huggingface.co/spaces) and create a new space.
2. Name your space and select the appropriate settings.

### Create and Configure `app.py`

1. Create a new file called `app.py` in your Huggingface Space.
2. Copy the code from `app.py` in this repository and paste it into the `app.py` file in your Huggingface Space.

### Obtain and Secure Your API Key

#### API Key: Obtain your API key from Groq

Go to the [Groq Console](https://console.groq.com/keys) and grab your API key.

#### Steps to Secure the API Key

##### Use Secrets Management in Hugging Face Spaces

Hugging Face Spaces provides a way to manage secrets securely. 

##### Set Up Secrets in Hugging Face Spaces

1. Navigate to your Hugging Face Space.
2. Go to the "Settings" tab.
3. Find the "Secrets" section.
4. Add a new secret with the name `API_KEY` and paste your API key as the value.

### Create and Configure `requirements.txt`

1. Create a `requirements.txt` file in your Huggingface Space.
2. Copy the content from `requirements.txt` in this repository and paste it into the `requirements.txt` file in your Huggingface Space.
3. Save and commit the changes.


After deployment, the URL of the Huggingface Space is used to embed it into the chatbot.html file

## Additional Information

- **Model Information**: We are using the `llama3-8b-8192` model, which is open-sourced by Meta AI. It is specially prompted to behave like Bart Simpson
- **Performance**: Groq provides faster access and supports open-source models efficiently.




