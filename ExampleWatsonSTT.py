import requests
import codecs
from requests.auth import HTTPBasicAuth

class ExampleWatsonSTT(object):
    def __init__(self):
        self.__url__ = "https://stream.watsonplatform.net/speech-to-text/api/v1"
        self.__auth__ = HTTPBasicAuth('{user}', '{pass}')

    def recognize(self, audio_file_path):
        headers = {
            'Content-Type': 'audio/wav'
        }
        params = {
            'model': 'pt-BR_BroadbandModel',
            'continuous': True
        }
        url = "{}/recognize".format(self.__url__)
        r = requests.post(url, auth=self.__auth__, headers=headers, params=params, data=open('{}'.format(audio_file_path), 'rb'))

        if r.status_code == 200:
            return r.json()
        else:
            return r.raise_for_status()

    def handle_recognize(self, recognize_output, audio_file_number):
        transcript = []
        output_file = codecs.open('results/watson_audio_{}.txt'.format(audio_file_number),'w',encoding='utf8')

        for result in recognize_output['results']:
            transcript.append(result['alternatives'][0]['transcript'])

        output_file.write(' '.join(transcript))
        output_file.close()
