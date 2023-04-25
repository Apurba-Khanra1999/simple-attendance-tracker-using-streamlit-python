import pandas as pd
import streamlit as st
from datetime import datetime

st.markdown("<h1 style='text-align: center;'>Mark Attendance</h1>", unsafe_allow_html=True)
st.markdown('---')
# Define the file name for the Excel file
file_name = 'attendance.xlsx'
file_name2 = 'students.xlsx'

fdf1=pd.read_excel(file_name2)

nameData = fdf1['Name'].to_list()
#st.write(nameData)

# Define the column names for the attendance sheet
attendance_cols = ['name', 'date', 'Entry time','Exit time', 'topic', 'status']

# Define a list of students to choose from
students = nameData

# Define a Streamlit app to allow users to mark attendance
def mark_attendance():
    # Add a dropdown menu to choose a student
    student_name = st.selectbox('Select a student', students)

    # Add a date picker to choose the date
    today = datetime.today()
    date = st.date_input('Date', today)
    # Add a time picker to choose the time
    entrytime = st.time_input('Entry Time')

    exittime =  st.time_input('Exit Time')

    # Add a text input to enter the topic
    topic = st.text_input('Topic')

    # Add a radio button to select the status
    status = st.radio('Status', ('Absent', 'Present', 'Late'))

    # Add a button to submit the attendance
    if st.button('Submit'):
        # Read the existing attendance data from the Excel file, if it exists
        try:
            attendance_data = pd.read_excel(file_name, sheet_name='attendance')
        except FileNotFoundError:
            # If the file doesn't exist yet, create a new DataFrame
            attendance_data = pd.DataFrame(columns=attendance_cols)

        # Append the new attendance data to the DataFrame
        new_row = pd.DataFrame([[student_name, date, entrytime,exittime, topic, status]], columns=attendance_cols)
        attendance_data = attendance_data.append(new_row, ignore_index=True)

        # Write the new attendance data to the Excel file
        attendance_data.to_excel(file_name, sheet_name='attendance', index=False)

        # Show a success message
        st.success(f"{student_name}'s attendance has been marked as {status}.")


# Run the Streamlit app
mark_attendance()

# Display the attendance data in a table
st.write('## Attendance Data')
try:
    attendance_data = pd.read_excel(file_name, sheet_name='attendance')
    st.dataframe(attendance_data)
except FileNotFoundError:
    st.warning('No attendance data found.')
