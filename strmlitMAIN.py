import streamlit as st
from st_audiorec import st_audiorec
from voicefunctions import SpeechToText, TextToSpeech
from tools import CallLLM
# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Voice Chat"])

# Page 1: Voice Chat
if page == "Voice Chat":
    st.title("🎙️ Voice Chat with AI Bot")
    
    wav_audio_data = st_audiorec()
    
    if wav_audio_data is not None:
        # st.audio(wav_audio_data, format="audio/wav")
    
        with open("input.wav", "wb") as f:
            f.write(wav_audio_data)
    
        st.success("Saved recording to input.wav")
        text = SpeechToText("input.wav")
        st.header('Query:')
        st.write(text)
        reply = CallLLM(text)
        
        TextToSpeech(reply)


    else:
        st.info("Click the record button above to capture your voice.")


# Page 2: Docs Ingestion
# elif page == "Docs Ingestion":
#     st.title("📚 Docs Ingestion")
    
    
