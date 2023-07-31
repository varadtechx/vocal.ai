import numpy as np
from flask import Flask, request, jsonify
import requests , os 
import subprocess

cwd=os.getcwd()
TEMP_DIR = os.path.join(cwd, "test")



app = Flask(__name__)

def start_torchserve():
    torchserve_cmd = "torchserve --start --model-store tts_model --models waveglow_synthesizer.mar "
    subprocess.Popen(torchserve_cmd, shell=True)

TORCHSERVE_URL = "http://localhost:8080/predictions/waveglow_synthesizer"

@app.route('/api',methods=['POST'])

def text_to_video():
    data = request.get_json()
    text = data.get("text", "")

    torchserve_data = {"text": text}
    response = requests.post(TORCHSERVE_URL, json=torchserve_data)
    audio_output = response.content
    with open('test/audio.wav', 'wb') as audio_file:
        audio_output.write(data)
    # audio_output = response.json().get("audio_output", "")

    wav2lip_output = os.path.join(TEMP_DIR, "output_video.mp4")
    inference_command = f"python inference.py --checkpoint_path /path/to/your/wav2lip_checkpoint.pth --face {video_file} --audio {audio_file} --outfile {wav2lip_output}"
    subprocess.run(inference_command, shell=True)

    
    

    return jsonify({"lip_synced_output": wav2lip_output})

def crop_video(video_file):
    #wrtie code to crop video according to the audio file lentgh 
    # return cropped_video_file



if __name__ == '__main__':
    start_torchserve()
    app.run(port=5000, debug=True)