from helper import make_prediction
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/", methods=["POST"])
def index():
    try:
        data = request.get_json() 
        if data:
            Pregnancies = data.get("Pregnancies") 
            Glucose = data.get("Glucose")
            BloodPressure = data.get("BloodPressure")
            SkinThickness = data.get("SkinThickness")
            Insulin = data.get("Insulin")
            BMI = data.get("BMI")
            DiabetesPedigreeFunction = data.get("DiabetesPedigreeFunction")
            Age = data.get("Age")

            prediction = make_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
            
            return jsonify({"prediction":prediction})

    except Exception as e:
        return jsonify({"error":str(e)})

if __name__ == "__main__":
    app.run(debug=False)