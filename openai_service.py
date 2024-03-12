import whisper
import os
from openai import OpenAI

class OpenAIWhisperService:

    def __init__(self):
        os.environ["path"] += ";c:\\ffmpeg\\bin"
        self.model = whisper.load_model("base")

    def predict(self, path):
        result = self.model.transcribe(path)
        return result["text"]

class OpenAIChatGPTService:

    def __init__(self):
        with open("data/chatgpt/openai.env") as f:
            key = f.read()
        self.client = OpenAI(api_key=key)

    def predict(self, text: str) -> str:
        completion = self.client.chat.completions.create(model="gpt-3.5-turbo",
                                                         # response_format={"type": "json_object"},
                                                    messages=[
                                                        {"role": "system",
                                                         "content": "Fais moi un résumé en 5 parties de ce texte"},
                                                        {"role": "user", "content": text}
                                                    ]
                                                    )
        return completion.choices[0].message.content

    def correction(self, text: str) -> str:
        completion = self.client.chat.completions.create(model="gpt-3.5-turbo",
                                                         # response_format={"type": "json_object"},
                                                    messages=[
                                                        {"role": "system",
                                                         "content": "Corrige moi ce texte dans le contexte de la programmation informatique"},
                                                        {"role": "user", "content": text}
                                                    ]
                                                    )
        return completion.choices[0].message.content

class OpenAIDallEService(OpenAIChatGPTService):

    def predict(self, text: str) -> str:
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=text,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url

class OpenAIMp3(OpenAIChatGPTService):

    def predict(self, text: str):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text[:4096]
        )
        response.stream_to_file("data/chatgpt/out.mp3")



if __name__ == '__main__':
    # whisper = OpenAIWhisperService()
    # res = whisper.predict("data/chatgpt/python.mp3")
    # print(res)
    # with open("data/chatgpt/python.txt", "w") as f:
    #     f.write(res)
    #
    # openai = OpenAIChatGPTService()
    # with open("data/chatgpt/python.txt") as f:
    #     text = f.read()
    # summary = openai.predict(text)
    # print(summary)
    # with open("data/chatgpt/summary.txt", "w") as f:
    #     f.write(summary)
    #
    # openai = OpenAIChatGPTService()
    # with open("data/chatgpt/python.txt") as f:
    #     text = f.read()
    # correction = openai.correction(text)
    # print(correction)
    # with open("data/chatgpt/python_correction.txt", "w") as f:
    #     f.write(correction)

    openai = OpenAIDallEService()
    # url = openai.predict("Un Python sur un ordinateur des années 80")
    url = openai.predict("Un PACS (Picture archiving and communication system) dans une clinique vétérinaire avec des radiographies de squelette de chiens")
    print(url)

    # openai = OpenAIMp3()
    # with open("data/chatgpt/python.txt") as f:
    #     text = f.read()
    # openai.predict(text)






