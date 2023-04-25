import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Attendance Tracker",
    page_icon="🧑‍🎓",
    layout="wide",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>JAGRAV COMPUTER LOG BOOK</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;font-size:18px;color:yellow;'>Attendance Tracker</p>",unsafe_allow_html=True)