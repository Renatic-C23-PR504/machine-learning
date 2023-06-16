<div align="center">
  
  # 👁️ Machine Learning Renatic API 👁️ 
  
  
</div>




## How to use locally?
First, clone this branch from this repository with:

```
git clone --single-branch --branch deploy-clinical-data-api https://github.com/Renatic-C23-PR504/machine-learning.git
```

Now, create a virtual environment to run the project
```
py -3 -m venv .venv
```

Then, activate the virtual environment
```
.venv\Scripts\activate
```

Install the requirements from the `requirements.txt` file:
```
pip install -r clinic-data\deployment\requirement.txt
```

Run the `app.py` file with:
```
py clinic-data\deployment\main.py
```

Now, it will run in localhost.

## Endpoint
### POST
```
  POST/
```
#### Input
| Key          | Info     | Data Type |
| :----------- | :------- | :------- | 
| `Pregnancies`    | Required | float |
| `Glucose`   | Required | float |
| `BloodPressure`  | Required | float |
| `SkinThickness`    | Required | float |
| `Insulin`   | Required | float |
| `BMI`  | Required | float |
| `DiabetesPedigreeFunction`    | Required | float |
| `Age`   | Required | float |

#### Output
| Key          | Data Type |
| :----------- | :------- | 
| `advice`    | string |
| `prediction`    | boolean |
| `probabilty`    | string |


Example:  
Input
```json
{
    "Pregnancies":6,
    "Glucose":148.0,
    "BloodPressure":72.0,
    "SkinThickness":35.0,
    "Insulin":125.0,
    "BMI":33.6,
    "DiabetesPedigreeFunction":0.627,
    "Age":50.0
}
```
Output
```json
{
    "advice": "Gula darah anda tinggi, mohon kurangi gula darah anda!",
    "prediction": true,
    "probabilty": "99 %"
}
```

## About Member 
| Members                        | Github                                                                                                                                            | LinkedIn                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steven Ardi Christanto - M166DKX4053    | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BlackBone09)  | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/steven-ardi-398539272/)      |
| Muhammad Fakhrul Amin - M131DSX1440    | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mfakhrulam)  | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mfakhrulam/)       |
| Muhammad Naufal Kusumajaya - M038DSX1492 | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/naufaljaya) | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/naufal-kusumajaya-b27959155/)              |
 