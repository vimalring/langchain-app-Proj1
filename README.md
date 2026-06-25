# LangChain + OpenAI + LangSmith Demo

A beginner-friendly Python application built using **LangChain**, **OpenAI**, and **LangSmith** as part of the **Gen AI Architect Program - Assignment 5**.

This project demonstrates how to use the **LangChain framework** to send a user prompt to an OpenAI chat model, receive the AI response, print it in the terminal, and automatically trace the execution in **LangSmith**.

---

## 📌 Project Objective

Build a simple Python application that:

- Uses **LangChain** to communicate with an OpenAI chat model.
- Accepts a user prompt from the terminal.
- Sends the prompt to the OpenAI model.
- Prints the AI-generated response.
- Automatically logs the execution to **LangSmith**.
- Loads all API keys securely from environment variables.

---

## 🚀 Tech Stack

- Python 3.x
- LangChain
- OpenAI
- LangSmith
- python-dotenv

---

## 📁 Project Structure

```text
langchain-app/
│
├── venv/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔄 Application Workflow

```text
                User Prompt
                     │
                     ▼
                  main.py
                     │
                     ▼
         Load Environment Variables
                     │
                     ▼
             LangChain Framework
                     │
                     ▼
           OpenAI Chat Model (GPT)
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
 Print Response             LangSmith Trace
   in Terminal                 Saved
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vimalring/langchain-app.git

cd langchain-app
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=langchain-assignment
```

> **Important:** Never commit your `.env` file to GitHub.

---

## ▶️ Run the Application

```bash
python main.py
```

Example:

```text
Enter your prompt:

Tell me a fun fact about Tamil Nadu.
```

Output:

```text
AI Response:

Tamil Nadu is home to the Brihadeeswarar Temple, a UNESCO World Heritage Site built over 1,000 years ago during the Chola Empire.
```

---

## 📊 LangSmith Integration

Once the application runs successfully, LangSmith automatically records:

- User Prompt
- Model Used
- AI Response
- Execution Time
- Token Usage
- Run Metadata

You can view all traces in your LangSmith dashboard.

---

## 📦 Dependencies

```text
langchain
langchain-openai
langsmith
python-dotenv
```

---

## 📸 Screenshots

Add screenshots of:

- Project Folder Structure
- VS Code
- Terminal Output
- LangSmith Dashboard Trace

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Creating and using Python Virtual Environments
- Managing API keys securely with `.env`
- Using LangChain to communicate with OpenAI
- Sending prompts to GPT models
- Receiving AI-generated responses
- Integrating LangSmith for execution tracing
- Building a clean Python GenAI application

---

## 👨‍💻 Author

**Vimal**


