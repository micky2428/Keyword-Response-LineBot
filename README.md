# Keyword-Response-LineBot

Keyword-Response-LineBot is designed to assist with verification processes. The bot, written in Python, enables users to input a number and receive images and related information about the item under inspection.

## Project Overview

The primary functionalities of the bot include:

1. **Automatic Response on Line**: Users can input a specific number into the Line chat, and the bot will automatically return images and relevant details about the inspection item, enhancing the efficiency of verification processes.

2. **Webhook Integration**: The bot is integrated with a Webhook that retrieves data from a remote server deployed on Render, ensuring real-time access to product information for field inspectors.

![ggg](https://github.com/user-attachments/assets/c217a543-eba7-4ab0-968f-10423c6c6eed)


## Purpose

The motivation behind developing the Keyword-Response-LineBot stems from the need to improve the traditional verification process, which relied on paper documents with small text and images, making it difficult to review details efficiently. 

By using the Line Bot, inspectors can now easily zoom in on images and view clear, legible information directly on their phones, simplifying inspections and reducing errors during fieldwork.

## File Descriptions

1. **Procfile**: Tells the server to use Gunicorn, a Python WSGI HTTP server, to serve the app function located in the try.py file. This is essential for deploying the Line Bot on platforms like Render.

2. **final.xlsx**: Contains images and textual descriptions related to the inspection items, used by the Line Bot to provide responses based on user inputs.

3. **render.yaml**: Defines the configuration settings for deploying the Line Bot on Render, including environment settings, service type, and deployment parameters.

4. **requirement.txt**: Lists all the Python dependencies and packages required for the bot to run. These packages will be installed during deployment.

5. **try.py**:The main script that contains the code for the Line Bot’s automatic response functionality. It handles user inputs, fetches the corresponding data, and sends back images and information. 


## References
- [line-bot-python-on-render](https://github.com/haojiwu/line-bot-python-on-render)
- LINE Developers

