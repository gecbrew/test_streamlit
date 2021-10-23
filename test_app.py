# import module
import streamlit as st
# Title
st.title("This is Title line")



#Title and option of radio button
status = st.radio("Select Subject: ", ('English', 'Math'))
#Choice based on condition
if (status == 'English'):
    st.success("English")
else:
    st.success("Math")

# slider
house_number = st.slider("Select the number", 1, 2)
# Fetching and Printing the house number
st.text('Selected House Number: {}'.format(house_number))