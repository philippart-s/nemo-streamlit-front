# import dependences
import streamlit as st
import os
from PIL import Image
import requests
import json

# if you have chosen prediction in the sidebar
def choice_prediction():
    st.write('# Prediction')
    st.write('### Choose a marine mammal sound file in .wav format')
    
    # upload sound
    uploaded_file = st.file_uploader(' ', type='wav')
    
    if uploaded_file is not None:
            
        # view details
        file_details = {'filename':uploaded_file.name, 'filetype':uploaded_file.type, 'filesize':uploaded_file.size}
        st.write(file_details)
        
        # read and play the audio file
        st.write('### Play audio')
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format='audio/wav')
      
        # save_file function
        upload_audio_file = requests.post('http://127.0.0.1:8080/send-sound', data=audio_bytes, headers={'Content-Type': 'audio/wave'})
        upload_audio_file.close()

        # define the filename
        #sound = uploaded_file.name
        
        st.write('### Classification results')
        
        # if you select the predict button
        if st.button('Predict'):
            prediction_result = requests.get('http://127.0.0.1:8080/get-animal-name?sound_name=sound-uploaded')
            st.write("The marine mammal is: ",  prediction_result.json()["animal"])
            prediction_result.close()
    else:
        st.write('The file has not been uploaded yet')
    
    return
        
# main
if __name__ == '__main__':
    
    st.image(Image.open('logo_ovh.png'), width=200)
    st.write('___')
    
    # create a sidebar
    st.sidebar.title('Marine mammal sounds classification')
    select = st.sidebar.selectbox('', ['Marine mammals', 'Prediction'], key='1')
    st.sidebar.write(select)
    
    # if sidebar selection is "Prediction"
    if select=='Prediction':
        # choice_prediction function
        choice_prediction()
    
    # else: stay on the home page
    else:
        st.write('# Marine mammals')
        st.write('The different marine mammals studied are the following.')
        st.write('For more information, please refer to this [link](https://cis.whoi.edu/science/B/whalesounds/index.cfm).')
        st.image(Image.open('marine_mammal_animals.png'))
