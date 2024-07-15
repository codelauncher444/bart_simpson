This documentation will guide you through the steps to get the chatbot up and running. The chatbot is designed to act like Bart Simpson.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Embedding the Chat Interface](#embedding-the-chat-interface)

## Requirements

- Python 3.x
- Internet connection to download dependencies and access API keys

## Installation

1. **Clone the Repository**: Clone this repository to your local machine.
    ```bash
    git clone https://github.com/codelauncher444/bart_simpson.git
    cd bart_simpson
    ```

2. **Install Dependencies**: Install the necessary dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **API Key**: Obtain your API key from Groq.
    - Go to [Groq Console](https://console.groq.com/keys) and grab your API key.

2. **Update Configuration**:
    - Open the `config.json` file in the root directory of the project.
    - Replace `API_KEY` with your actual API key.

## Running the Application

1. **Start the Application**:
    ```bash
    python app.py
    ```

2. **Get the Public URL**:
    - After the application launches, a public URL will be provided. This URL is essential for embedding the chat interface.

3. **Update Public URL in Configuration**:
    - Copy the public URL provided by the application.
    - Update the `config.json` file with the public URL but keep the python program running.

## Embedding the Chat Interface

1. **Embed the Interface**:
    - The `chatbot.html` file will embed a Gradio chat interface app.
    - Ensure that the program remains running to keep the chat interface accessible.

## Additional Information

- **Model Information**: We are using the `llama3-8b-8192` model, which is open-sourced by Meta AI. It is specially prompted to behave like Bart Simpson
- **Performance**: Groq provides faster access and supports open-source models efficiently.


