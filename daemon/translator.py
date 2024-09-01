import pyaudio
import wave
import speech_recognition as sr
import time
from google.cloud import texttospeech
from google.cloud import translate_v2 as translate
from google.cloud import exceptions
import os
import argparse
import threading

def audio_to_text(audio_file, debug=False):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            if debug:
                print("O: " + text)
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def record_audio():
    # Parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    current_time_epoch = int(time.time())
    OUTPUT_FILENAME = f"/tmp/{current_time_epoch}_output.wav"

    audio = pyaudio.PyAudio()

    # Start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    return OUTPUT_FILENAME

def speak(content, language="es-US", voice="es-US-Studio-B"):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=content)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language,
        name=voice,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1
    )
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    current_time_epoch = int(time.time())
    file_path = f"/tmp/{current_time_epoch}_{language}.mp3"

    with open(file_path, "wb") as out:
        out.write(response.audio_content)
    
    # play the audio file
    os.system(f"play {file_path}")
    os.system(f"rm {file_path}")

def translate_text(target: str, text: str) -> dict:
    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    return result

def execute(language="es-US", voice="es-US-Studio-B", debug=False):
    os.system('clear')
    while True:
        file_path = record_audio()
        temporary_thread = threading.Thread(target=execute_async, args=(language, voice, debug, file_path))
        temporary_thread.start()        

def execute_async(language="es-US", voice="es-US-Studio-B", debug=False, file_path=""):
    if file_path == "":
        return

    if not os.path.exists(file_path):
        return

    try:
        # convert the audio file to text
        english_text = audio_to_text(file_path, debug=debug)
        # remove the temp file
        os.system(f"rm {file_path}")
        # avoid empty text
        if not english_text:
            return

        # post the english text to our API to get the translated text
        post_text(english_text)

        #translated_text = translate_text(language, english_text)
        #text = translated_text["translatedText"]
        
    except Exception as exc:
        print(exc)
        return

def post_text(text):
    # post the text to the API
    url = "http://http://192.168.0.148:5000/api/v1/translate"

languages = {
    "es": "es-US",
    "en": "en-US",
    "pt": "pt-BR",
    "cn": "cmn-CN",
    "tr": "tr-TR",
    "ar": "ar",
    "de": "de-DE"
}

voices = {
    "es": "es-US-Studio-B",
    "en": "en-US-Standard-C",
    "pt": "pt-BR-Neural2-B",
    "cn": "cmn-CN-Standard-A",
    "tr": "tr-TR-Standard-A",
    "ar": "ar-XA-Standard-A",
    "de": "de-DE-Standard-A"
}

def run():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Description of your script")
    parser.add_argument("-l", "--language", help="Language", required=True)
    parser.add_argument("-d", "--debug", help="Debug", required=False, default=False)
    args = parser.parse_args()

    if args.language not in languages:
        print("Language not supported")
        exit()

    execute(language=languages[args.language], voice=voices[args.language], debug=args.debug)

if __name__ == "__main__":
    run()