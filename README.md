# Chat with PhysioPedia

Chat with PhysioPedia is a simple chat-based application designed to assist users with their physiotherapy exercises. This app allows users to ask questions related to exercises and muscle groups while integrating data stored in a SQLite database.

## Features

- **Interactive Chat**: Ask questions and receive responses from the virtual physio assistant.
- **Database Integration**: The app allows you to load exercise data from a CSV file and insert it into an SQLite database.
- **SQL Query Generation**: Automatically generates SQL queries based on user questions to fetch relevant data from the database.
- **Natural Language Responses**: The app uses AI to generate human-readable responses from the SQL query results.

## Technology Stack

- **Python**: The core logic is written in Python.
- **LangChain**: Used for managing conversational flow, querying, and generating SQL queries.
- **OpenAI's GPT-4**: Used for generating natural language responses from the chatbot.
- **Streamlit**: Provides the front-end for the application.
- **SQLite**: A lightweight database used to store and query exercise data.
- **dotenv**: Manages environment variables.

## How to Use

1. **Clone the Repository**:  
   Clone the repository to your local machine.

   ```bash
   git clone <repo-url>
   cd physioPedia

2. **Install Dependencies**:
    Make sure you have Python installed. Then, install the required packages by running:
    
    ```bash
    pip install -r requirements.txt

3. **Set Up Environmental Variables**:
    Create a '.env' file in the project root directory. Add your environment variables to the file:

    ```env
    OPENAI_API_KEY=<your-openai-api-key>

4. **Load CSV Data**:
    Place the megaGymDataset.csv file in the root directory, or specify the correct path in the Streamlit sidebar to load the data into the SQLite database.

5. **Run the App**:
    Start the Streamlit application by running:
     ```bash
     streamlit run app.py

     