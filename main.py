import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Productivity Tracker")

tasks = st.text_area("Enter tasks and priority:", "Finish project: High, Read book: Low, Gym: Medium")

if st.button("Analyze Productivity"):
    if tasks:
        input_data = {"tasks": tasks}
        response = client.flow.execute("import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Productivity Tracker")

tasks = st.text_area("Enter tasks and priority:", "Finish project: High, Read book: Low, Gym: Medium")

if st.button("Analyze Productivity"):
    if tasks:
        input_data = {"tasks": tasks}
        response = client.flow.execute("import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Productivity Tracker")

tasks = st.text_area("Enter tasks and priority:", "Finish project: High, Read book: Low, Gym: Medium")

if st.button("Analyze Productivity"):
    if tasks:
        input_data = {"tasks": tasks}
        response = client.flow.execute("dakshkansil/ProductivityTracker", input_data)
        st.write(response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter your tasks.")
/ProductivityTracker", input_data)
        st.write(response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter your tasks.")
/ProductivityTracker", input_data)
        st.write(response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter your tasks.")
