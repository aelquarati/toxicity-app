import requests
import sys
import json
sys.path.append('..')
from backend.toxicbert.predict import predict_toxicity
class TestApp:

    def test_uni(self):
        string = 'I wish to find the universe formula'
        assert len(predict_toxicity(string)) !=0, "Couldn't treat your txt"""

    def test_integration(self):

        response = requests.post('http://192.168.56.1:5000/predict',data = {"key":"text"})
        content = response.content.decode('utf-8')
        assert content!=None, "Couldn't treat your txt"
