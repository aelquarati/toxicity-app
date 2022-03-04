from detoxify import Detoxify

def predict_toxicity(txt):
    model = Detoxify('original')
    predictions = model.predict(txt)
    return predictions
    
string = 'I Hate this'
assert len(predict_toxicity(string)) !=0, "Couldn't treat your txt"