from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from backend.toxicbert.predict import predict_toxicity

app = Flask(__name__)
CORS(app)
api  = Api(app)



@app.route("/health")
def health():
    return '{"response":"ok"}'
    
class Input_data(Resource): 
    
    def post (self):

        content = request.get_json(silent=True)
        
        txt = content["text"]
        scores =[predict_toxicity(txt)]

        for dicts in scores:
            for keys in dicts:
                dicts[keys] = str(dicts[keys])
            
        return dicts
 
api.add_resource(Input_data,"/predict")



if __name__ == '__main__':
    app.run()
