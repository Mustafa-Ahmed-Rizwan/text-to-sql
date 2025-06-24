import os
import sqlite3
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv  

load_dotenv()

def get_sql_query(user_query):
    groq_sys_prompt = ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    The SQL database has the name STUDENT and has the following columns - ID,NAME, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
                    Example 2 - Tell me all the students studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM STUDENT 
                        where COURSE="Data Science"; 
                    also the sql code should not have ``` in beginning or end and sql word in output.
                    Now convert the following question in English to a valid SQL Query: {user_query}. 
                    No preamble, only valid SQL please
                                                       """)
    model="llama3-8b-8192"
    llm = ChatGroq(
    groq_api_key = os.environ.get("GROQ_API_KEY"),
    model_name=model
    )

    chain = groq_sys_prompt | llm | StrOutputParser()
    response = chain.invoke({"user_query": user_query})
    return response


def return_sql_response(sql_query):
    database = "student.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()


def main():
    st.set_page_config(page_title="Text To SQL", page_icon="🧑‍💻", layout="wide")
    st.markdown(
        """
        <style>
        .main {background-color: #18191A;}
        .stButton>button {background-color: #ff4b4b; color: white;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🧑‍💻 Text To SQL")
    st.write("Ask questions about your database in plain English and get instant answers!")

    with st.sidebar:
        st.header("Instructions")
        st.markdown(
            """
            - Enter your question in plain English.
            - Click **Enter** to get the SQL query and results.
            - Example: *Show me all students with marks above 80*
            """
        )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user_query = st.text_input("Input your question:")
        submit = st.button("Enter", use_container_width=True)

    if submit and user_query.strip():
        try:
            sql_query = get_sql_query(user_query)
            retrieved_data = return_sql_response(sql_query)
            st.subheader(f"SQL Query: `{sql_query}`")
            if retrieved_data:
                st.dataframe(retrieved_data)
            else:
                st.info("No results found for your query.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()