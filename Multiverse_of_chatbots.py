import streamlit as st

st.title("THE MULTIVERSE OF CHATBOTS")
personality=st.selectbox("Who do you want to talk to?. ",
    ["Mr. cool dhoni",
    "The torchberer Rajamouli",
    "The masterpeice Hans zimmer",
    "The goat Vijay Thalapathi",]
)

import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_message=st.text_input("Ask a question.")
if st.button("Send"):
    if user_message:
        ai_instruction=f"You are acting as {personality}. respond to the message sent by the user staying complete in that character: {user_message}"
        with st.spinner("sit tight!, we are working on it..."):
            response=client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instruction
            )

            st.success("Message received!")
            st.write(response.text)
    else:
        st.warning("Please type something!")



