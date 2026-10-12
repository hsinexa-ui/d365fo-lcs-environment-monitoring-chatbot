# D365FO LCS Environment Monitoring Chatbot

An interactive chatbot designed to help monitor Microsoft Dynamics 365 Finance & Operations (D365FO) environments across DEV, UAT, and PROD. It allows users to ask questions in natural language and retrieve environment-related information, including the last database refresh date.

## 🚀 Live Demo

**Try the deployed application:** [D365FO LCS Environment Monitoring Chatbot](https://chatbot-environment-aub0gqh7g2esdehx.canadacentral-01.azurewebsites.net/)

**Hosting Platform:** Microsoft Azure App Service

## 📌 Project Overview

Managing multiple Dynamics 365 Finance & Operations environments requires tracking environment status and important maintenance activities. This project provides a simple web-based chatbot interface that helps users retrieve environment information through conversational queries.

For example, a user can ask:

- When was the DEV database last refreshed?
- When was the UAT database last refreshed?
- When was the PROD database last refreshed?
- What is the last database refresh date for a particular environment?

The chatbot responds with the relevant information available to the application.

## ✨ Key Features

- **Multi-Environment Monitoring:** Supports environment-related queries for DEV, UAT, and PROD.
- **Database Refresh Tracking:** Retrieves the last database refresh date when the information is available.
- **Natural-Language Interaction:** Allows users to ask questions in a conversational format.
- **Web-Based Interface:** Provides a simple interface for interacting with the chatbot.
- **Cloud Deployment:** Hosted on Microsoft Azure App Service.
- **Centralized Information Access:** Helps reduce the need to manually search for environment-related details.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Web Application:** Python-based web application
- **Frontend:** HTML and CSS
- **Cloud Platform:** Microsoft Azure
- **Hosting Service:** Azure App Service
- **Application Files:** Python, HTML, CSS, and requirements.txt

## 🏗️ Architecture

```text
User
  |
  v
Web-Based Chatbot Interface
  |
  v
Python Application (app.py)
  |
  v
Environment Query Processing
  |
  v
DEV / UAT / PROD Information
  |
  v
Response Displayed to User

Deployment:
Python Web Application
          |
          v
Microsoft Azure App Service
          |
          v
Live Web Application
```

*Note: This is a conceptual overview. Actual integrations and data sources depend on the application's implementation.*

## 📂 Project Structure

```text
Chat-Bot-Project/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── image.jpg
│   └── style.css
└── templates/
    └── index.html
```

## 💻 Run the Project Locally

### Prerequisites

- Python installed on your machine
- Git installed
- A terminal such as Command Prompt or PowerShell

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Chat-Bot-Project
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Application

```bash
python app.py
```

Open the local URL displayed by the application in your browser. For a typical Flask configuration, this is `http://127.0.0.1:5000/`.

## ☁️ Azure Deployment

The application is deployed to Microsoft Azure App Service and is accessible through its public web URL.

**Deployment platform:** Azure App Service

**Azure region indicated by the application URL:** Canada Central

Azure App Service provides managed hosting for web applications and supports deployment through multiple methods, including source-control-based workflows and deployment tools.

For official deployment guidance, see the [Microsoft Azure App Service Python Quickstart](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python).

## 🔐 Security and Limitations

- Environment information should only be accessible to authorized users.
- Do not commit credentials, access tokens, connection strings, or other secrets to the repository.
- The accuracy of database refresh dates depends on the configured information source.
- This chatbot should not be considered a real-time monitoring system for environment health unless health checks and status integrations are implemented.

## 🎯 Project Goals

- Simplify access to D365FO environment information.
- Reduce manual effort when checking database refresh history.
- Provide a conversational interface for common environment-related questions.
- Demonstrate practical Python web development and Azure cloud deployment skills.

## 👨‍💻 Author

**HSI Nexa**

DevOps Engineer | Azure | Python | Dynamics 365 Finance & Operations

## 📄 License

Add a license file if you intend to distribute this project for reuse. Otherwise, specify the applicable usage terms for your repository.

