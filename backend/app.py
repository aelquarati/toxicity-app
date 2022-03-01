from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
#CORS(app)
api  = Api(app)


@app.route("/")
class Input_data(Resource): 
    
    def post (self):
        

        content = request.get_json(silent=True)
        
        response = request.post('http://0.0.0.0:5000/predict', content)
        

        return response
 
api.add_resource(Input_data,"/call")



if __name__ == '__main__':
    app.run()
