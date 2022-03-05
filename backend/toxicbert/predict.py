
from detoxify import Detoxify

def predict_toxicity(txt):
    model = Detoxify('original')
    predictions = model.predict(txt)
    return predictions
