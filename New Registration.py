import datetime
import os.path
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="New Registration",
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

st.markdown("<h1 style='text-align: center;'>New Student Registration</h1>", unsafe_allow_html=True)
st.markdown('---')

# check if file exists
if os.path.isfile("students.xlsx"):
    # load existing data from file
    df = pd.read_excel("students.xlsx")
else:
    # create empty dataframe
    df = pd.DataFrame(columns=['Name', 'Address', 'Class', 'Date of Birth', 'Contact No', 'Fees'])
    # create empty file
    writer = pd.ExcelWriter('students.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()

# collect inputs from user
name = st.text_input("Name").lower()
address = st.text_input("Address")
class_ = st.selectbox("Class", ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"])
dob = st.date_input("Date of Birth",min_value=datetime.date(year=1960,month=1,day=1))
contactno = st.text_input("Contact No")
fees = st.text_input("Fees")

# add row to dataframe when user clicks "Register"
if st.button("Register"):
    new_row = {'Name': name, 'Address': address, 'Class': class_, 'Date of Birth': dob.strftime("%Y-%m-%d"),
               'Contact No': contactno, 'Fees': fees}
    df = df.append(new_row, ignore_index=True)
    df.to_excel("students.xlsx",sheet_name='student', index=False)
    st.success("Registration successful!")

st.markdown('---')
# display current students in dataframe
if len(df) > 0:
    st.subheader("Current Students")
    st.write("Count - ", len(df))
    st.write(df)
