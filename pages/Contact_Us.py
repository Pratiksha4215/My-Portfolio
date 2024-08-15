import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")

    # Define the subject and recipient email
    subject = "New email from " + user_email
    to_email = "recipient@example.com"  # Replace with actual recipient email

    # Handle form submission
    button = st.form_submit_button("Submit")
    if button:
        try:
            # Send email using the defined function
            send_email(subject, raw_message, to_email)
            st.info("Your email was sent successfully")
        except Exception as e:
            st.error(f"An error occurred: {e}")
