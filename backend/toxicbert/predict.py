from backend.toxicbert.predict import predict_toxicity

string = 'I Hate this shit'
assert len(predict_toxicity(string)) !=0, "Couldn't treat your txt"
