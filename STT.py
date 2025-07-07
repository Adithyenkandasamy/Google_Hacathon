import pyaudio
import wave
import whisper
import os

# 🎙️ Record voice using PyAudio
def record_audio(filename="tamil_input.wav", duration=5):
    chunk = 1024  # Buffer size
    format = pyaudio.paInt16
    channels = 1
    rate = 16000

    print("🎤 Speak in Tamil now...")

    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    frames = []
    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("✅ Audio recorded:", filename)

# 🧠 Transcribe Tamil using Whisper
def transcribe_tamil(filename="tamil_input.wav"):
    model = whisper.load_model("base")  # You can also use "small" or "medium"
    result = model.transcribe(filename, language="ta")  # "ta" = Tamil
    print("📝 Tamil Transcription:")
    print(result["text"])

# 🔁 Full process
record_audio()
transcribe_tamil()
