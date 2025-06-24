# Text-to-SQL Web Application

## Overview
This is a Streamlit-based web application that converts plain English questions into SQL queries and retrieves data from a SQLite database. The app uses the Grok AI model from xAI to generate SQL queries based on user input and displays the results in a user-friendly interface.

## Features
- Converts natural language questions into valid SQL queries.
- Executes SQL queries on a SQLite database (`student.db`) containing student records.
- Displays query results in a clean, tabular format using Streamlit.
- Supports queries on a `STUDENT` table with columns: `ID`, `NAME`, `COURSE`, `SECTION`, and `MARKS`.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.8+
- SQLite3
- Required Python libraries (listed in `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variable for the Groq API key:
   - Create a `.env` file in the project root.
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

5. Create the SQLite database:
   - Run the `database.py` script to initialize the `student.db` database:
     ```bash
     python database.py
     ```

## Usage
1. Start the Streamlit application:
   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Enter a question in plain English (e.g., "Show me all students with marks above 80") and click **Enter** to see the generated SQL query and results.

## Project Structure
```
├── .env              # Environment variables (e.g., GROQ_API_KEY)
├── database.py       # Script to create and populate the SQLite database
├── main.py           # Main Streamlit application
├── requirements.txt  # Python dependencies
└── student.db        # SQLite database (generated after running database.py)
```

## Example Queries
- "How many students are in the Computer Science course?"
- "Show all students with marks above 85."
- "List all students in section A."

## Dependencies
- `streamlit`: For the web interface.
- `langchain-groq`: To interact with the Groq API for query generation.
- `sqlite3`: For database operations.
- `python-dotenv`: To load environment variables.

## Notes
- Ensure the `.env` file is not committed to version control (add it to `.gitignore`).
- The Groq API key is required to use the query generation feature. Obtain it from [xAI](https://x.ai/api).

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions or bug reports.

## License
This project is licensed under the MIT License.