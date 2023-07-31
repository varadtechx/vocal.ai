import streamlit as st
import requests

TORCHSERVE_ENDPOINT = 'http://localhost:8080/predictions/waveglow_synthesizer'

st.title('TorchServe Dashboard')


def get_predictions(text):
    
    response = requests.post(TORCHSERVE_ENDPOINT, json={'text':text})
    data = response.content
    return data


text = st.text_area("Enter your speech here.......", height=200)

if st.button('Predict'):
    predictions = get_predictions(text)
    if predictions:
            
            st.write('Predictions:')
            for pred in predictions:
                st.write(f"{pred['text']}: {pred['score']:.2f}")

            
            if 'audio' in predictions[0]:
                st.audio(predictions[0]['audio'], format='audio/wav')
            else:
                st.warning("No response from the API. Please check the server and try again.")
    else:
        st.warning("Please enter text to generate audio.")
    


