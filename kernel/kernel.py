import os
import json
import streamlit as st

def readData():
    if os.path.exists("kernel.json"):
        with open("kernel.json", "r") as f:
            data = json.load(f)
            return data
        
def saveData():
    with open("kernel.json", "w") as f:
        json.dump(st.session_state.messages, f)