import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from io import BytesIO
from elevenlabs import ElevenLabs, play
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()


def record_voice(filename="input.wav", duration=5, sample_rate=16000):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="float32")
    sd.wait()
    # Convert float32 (-1..1) to int16 for WAV
    audio_int16 = np.int16(audio * 32767)
    wav.write(filename, sample_rate, audio_int16)
    print(f"Saved to {filename}")

client = ElevenLabs(

  api_key=os.environ.get("ELEVEN_LAB_APIKEY"),

)


def SpeechToText(audio_file, model_id="scribe_v1", language_code="eng",
                 tag_audio_events=True, diarize=True):
    with open(audio_file, "rb") as f:
        audio_data = BytesIO(f.read())

    transcription = client.speech_to_text.convert(
        file=audio_data,
        model_id=model_id,
        tag_audio_events=tag_audio_events,
        language_code=language_code,  # None for auto-detect
        diarize=diarize
    )
    
    return transcription.text

def TextToSpeech(text):
    audio = client.text_to_speech.convert(

    text=text,

    voice_id="nPczCjzI2devNBz1zQrb",

    model_id="eleven_multilingual_v2",

    output_format="mp3_44100_128",

    )
    st.header('AI Reply:')
    
    play(audio)
    st.write(text)

