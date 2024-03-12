import json
import torch
from flask import Flask, request, jsonify
from transformers import pipeline

useFlash = False

print('Computing model whisper for insanely...', flush=True)

pipe = pipeline("automatic-speech-recognition",
                "openai/whisper-large-v3",
                torch_dtype=torch.float16,
                model_kwargs={"use_flash_attention_2": useFlash},
                device="cuda:0")

if not useFlash:
    pipe.model = pipe.model.to_bettertransformer()
else:
    pipe.model = pipe.model.to('cuda')

print('Computation done ! API will start', flush=True)

app = Flask(__name__)

@app.get('/')
def index():
    return "Hello !"

@app.route('/transcribe', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    input_file = '/tmp/audio.wav'
    output_text = "/tmp/output.json"

    file.save(input_file)

    print('File saved', input_file, flush=True)

    print('Will run insanely', flush=True)

    data = pipe(input_file,
                chunk_length_s=30,
                batch_size=24,
                return_timestamps=True,
                generate_kwargs={"task": "transcribe", "language": "fr"})

    print(json.dumps(data, indent=2), flush=True)
    
    # Enregistrer le résultat dans un nouveau fichier JSON
    with open(output_text, "w") as output:
        json.dump(data, output, indent=2)

    print('Finished result saved to', output_text, flush=True)

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860, debug=False)
