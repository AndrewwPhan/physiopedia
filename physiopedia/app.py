from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.utilities import SQLDatabase
import streamlit as st

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    # db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    db_uri = "sqlite:///gym.db"
    print(db_uri)
    return SQLDatabase.from_uri(db_uri)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database."),
    ]

def main():
    load_dotenv()

    st.set_page_config(page_title="Chat with PhysioPedia", page_icon=":speech_balloon:")
    
    st.title("Chat with PhysioPedia")

    with st.sidebar:
        st.subheader("Settings")
        st.write("This is a simple chat application using PhysioPedia. Connect to the database and start chatting.")

        st.text_input("Host", value="localhost", key="Host")
        st.text_input("Port", value = "3306", key="Port")
        st.text_input("User", value ="root", key="User")
        st.text_input("Password", type="password", value="admin", key="Password")
        st.text_input("Database", value="Chinook", key="Database")

        if st.button("Connect"):
            with st.spinner("Connecting to database..."):
                db = init_database(
                    st.session_state["User"],
                    st.session_state["Password"],
                    st.session_state["Host"],
                    st.session_state["Port"],
                    st.session_state["Database"]
                )
                st.session_state.db = db
                st.success("Connected to database!")

    for message in st.session_state.chat_history:
            if isinstance(message, AIMessage):
                 with st.chat_message("AI"):
                    st.markdown(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("Human"):
                    st.markdown(message.content)

    user_query = st.chat_input("Type a message...")
    if user_query is not None and user_query.strip() != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            response = "I don't know how to respond to that."
            st.markdown(response)

        st.session_state.chat_history.append(AIMessage(content=response))

if __name__ == "__main__":
    main()