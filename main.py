import streamlit as st
from lc_helper import get_few_shot_db_chain

st.set_page_config(
    page_title="Database Q&A",
    page_icon=":question:",
    layout="wide",  # Set layout to 'wide' for better use of space
)

st.title("Database Q & A ")

with st.container():
    st.header("Database Connection")
    # Database URI Input
    db_uri = st.text_input(
        "Enter your database URI (e.g., mysql+pymysql://root:shabeeth@localhost/atliq_tshirts",
        key="db_uri",  # Add a unique key for the input
        placeholder="e.g., postgresql://user:password@localhost:5432/mydatabase",
        help="Ensure your database is accessible with this URI.",
    )

with st.container():
    st.header("Ask your Question")
    # Question Input
    question = st.text_input("Question: ", key="question")

    if question:
        # Create the chain with the provided database URI
        chain = get_few_shot_db_chain(db_uri)

        # Run the chain and display the response
        response = chain.run(question)

        st.header("Answer")
        st.write(response)