import streamlit as st
import os
import time as tm
import random
import base64
import json
from PIL import Image
import requests as r

st.set_page_config(page_title = "PixMatch", page_icon="🕹️", layout = "wide", initial_sidebar_state = "expanded")
url = 'https://ntfy.sh/salvador'
st.title("Simple Web Site: Salvador")

def main(data = "From streamlit"):
    data = {'message': f"Streamlit {tm.time()} {os.uname()}"}
    response = r.post(url, data=data)
    st.toast(response.status_code)
    

if __name__ == "__main__":
    main()
