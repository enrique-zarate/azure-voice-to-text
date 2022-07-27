import os
from flask import jsonify
from flask import Flask, render_template,request
from speech_recognition import *
from pydub import AudioSegment
from sample_recognize_custom_entities import *
from data_cleaning import clean_dict
from db import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('carga-sintomas.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        #print('este es el file', f)
        print('este es el tipo file', type(f))
        path = os.path.join('./audio', "AAA.ogg")
        f.save(path)
        # print('saved', saved)

    #     print(type(f.read()))
    #     f.save('audio/audio_uploaded.wav')
        # f.save(f.filename)
        # voice_to_text(audio)

        wav_path = convert_audio(path)

        texto = voice_to_text(wav_path)

        path_text = os.path.join('./text', "text_recognized.txt")

        with open(path_text, 'w') as f:
            f.write(texto.text)

        response = sample_recognize_custom_entities()
        print("response: ", response)
        return response

def convert_audio(input_path):
    src = input_path
    dst = "audio/test.wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_file(src)
    sound.export(dst, format="wav")
    return dst

@app.route('/consultadrpaciente',methods = ['GET',"POST"])
def consultadr():
    path_text = os.path.join('./text', "text_recognized.txt")
    with open(path_text, 'r') as f:
        lines =  f.readlines()
    return render_template('consultadrpaciente.html',data=lines)

		
if __name__ == '__main__':
   app.run(debug = True)


