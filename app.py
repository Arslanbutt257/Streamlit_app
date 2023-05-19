import requests
import streamlit as st

# Define API endpoints
upload_endpoint = "http://3.141.126.10/api/summarizer/"
status_endpoint = "http://3.141.126.10/api/summarizer/"

# Streamlit UI
st.title("Book Analyzer")

# Book Upload Section
uploaded_file = st.file_uploader("Upload Book File")

# Token Input Section
token = st.text_input("Enter Token Number")

# Book Upload Button
if st.button("Analyze Book"):
    if uploaded_file is not None and token:
        # Prepare data for POST request
        files = {"file": uploaded_file}
        data = {"token": token}

        # Make POST request
        response = requests.post(upload_endpoint, files=files, data=data)
        if response.status_code == 200:
            st.success("Book uploaded successfully!")
        else:
            st.error("Failed to upload book. Please try again.")

st.title("Check Status of book being analyzed")
# Token Input Section
token1 = st.text_input("Enter Token Number", key='token_input')

# Check Status Button
if st.button("Check Status"):
    if token:
        # Prepare data for GET request
        params = {"token": token1}

        # Make GET request
        response = requests.get(status_endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            # Display response on frontend
            st.subheader("Short Summary")
            st.write(data["message"][0]["short_summary"])

            st.subheader("Long Summary")
            st.write(data["message"][0]["long_summary"])

            st.subheader("Tweet")
            tweets = data["message"][0]["tweet"].split("/")
            for i in range(len(tweets)):
                st.write(tweets[i], key=str(i))

            st.subheader("Post")
            posts = data["message"][0]["post"].split("/")
            for i in range(len(posts)):
                st.write(posts[i])
        else:
            st.write(response)
            st.error("Either the book is still being analyzed or you have not started the task")
    else:
        st.warning("Please enter a token number.")

