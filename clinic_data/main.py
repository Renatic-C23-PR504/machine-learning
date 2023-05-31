from helper import make_prediction
from flask import Flask
from flask_restful import Api, Resource, reqparse

# initiate Flask app and restful API
app = Flask(__name__)
api = Api(app)

# for validation from post method
args = reqparse.RequestParser()
args.add_argument('Pregnancies', required=True)
args.add_argument('Glucose', required=True)
args.add_argument('BloodPressure', required=True)
args.add_argument('SkinThickness', required=True)
args.add_argument('Insulin', required=True)
args.add_argument('BMI', required=True)
args.add_argument('DiabetesPedigreeFunction', required=True)
args.add_argument('Age', required=True)

# data from post method stored here
data = []

class Renatic(Resource):
    
    # for get method (get prediction)
    def get(self, app_id):
        
        # for clinical data
        if app_id == 0:
            try:
                # extract from data list (line 21)
                Pregnancies = float(data[0]["Pregnancies"])
                Glucose = float(data[0]["Glucose"])
                BloodPressure = float(data[0]["BloodPressure"])
                SkinThickness = float(data[0]["SkinThickness"])
                Insulin = float(data[0]["Insulin"])
                BMI = float(data[0]["BMI"])
                DiabetesPedigreeFunction = float(data[0]["DiabetesPedigreeFunction"])
                Age = float(data[0]["Age"])
                
                # get prediction with make_prediction from helper
                prediction = make_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
                
                # empty the data list (line 21) so that the api is reusable
                data.pop()

                # return the prediction (True / False)
                return prediction
            
            except Exception as e:
                return str(e)
            
        # prepare for image classification
        elif app_id == 1:
            pass
        
        else:
            return "Wrong app_id"
    
    # for post method (store data)
    def post(self, app_id):
        
        # for clinical data
        if app_id == 0:
            try:

                # parse body request
                receive = args.parse_args()

                # add to data list (line 21)
                data.append(receive)

                return "Success", 201
            
            except Exception as e:
                return str(e)
            
        # prepare for image classification
        elif app_id == 1:
            pass

        else:
            return "Wrong app_id"
        
    
api.add_resource(Renatic,'/predict/<int:app_id>')

if __name__ == "__main__":
    app.run(debug=False)