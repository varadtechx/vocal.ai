import streamlit as st
import requests
import os

def main():
    st.title("Vocal.ai")
    text_input = st.text_area("Enter the text to be converted to speech.....")

    
    if st.button("Submit"):
        
        response = requests.post("http://localhost:5000/text_to_speech", json={"text": text_input})
        lip_synced_output = response.json().get("lip_synced_output", "")
        st.video(lip_synced_output)

        download_button(lip_synced_output)
    st.video('assets/avatar.mp4')
    

def download_button(file_path):
    with open(file_path, 'rb') as file:
        btn = st.download_button(
            label="Download Video",
            data=file,
            file_name='lip_synced_output.mp4',
            mime='video/mp4'
        )
        return btn

if __name__ == "__main__":
    main()




