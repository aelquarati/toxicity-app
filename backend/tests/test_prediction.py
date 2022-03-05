from backend.toxicbert.predict import predict_toxicity

string = 'I Hate this '
assert len(predict_toxicity(string)) !=0, "Couldn't treat your txt"