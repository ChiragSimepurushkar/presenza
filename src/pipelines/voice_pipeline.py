from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000) #sr(sample rate) => More the sr better the audio quality (but take time too) so here our normal task to detect audio will take little less sr(16000 samples/second)
        wav = preprocess_wav(audio) #wave-normalize audio
        #preprocess_wav() generally takes the waveform and performs preprocessing such as:audio->resampling (if needed)->normalization->silence/noise processing->clean waveform->wav
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist() #256D vector
    except Exception as e:
        st.error('Voice recognition Error!')
        return None

def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None , 0.0 # (student_id, similarity score)

    best_id = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.item():
        if stored_embedding:
            similarity = np.dot(new_embedding, stored_embedding) #similarity score calculated using Dot product=> if the vectors points at single point => more close the vectors are
            if similarity > best_score:
                best_score = similarity
                best_id = sid

    if best_score >= threshold:
         return best_id, best_score


def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65): #when teacher load all classroom students voice ,we want to break the audio into parts and reapeat the process for identification of each voice
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000) 
        segments = librosa.effects.split(audio, top_db=30)# top_db-> control sensitivy of voice ,(catch the voice which is load , and not talking softly), if top_dp is set high will only catch person shouting

        identified_results = {}

        for start, end in segments:
            if (end-start) < sr *0.5: #skip the audio which is noice(garbage(empty,distractions..))
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.eembed_utterance(wav)

            sid, score = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error("Bulk processing Error!!")
        return {}




