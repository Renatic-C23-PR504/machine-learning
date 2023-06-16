<div align="center">
  
  # 👁️ Machine Learning Renatic API 👁️ 
  
  
</div>




## How to use locally?
First, clone this branch from this repository with:

```
git clone --single-branch --branch deploy-api-image https://github.com/Renatic-C23-PR504/machine-learning.git
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
pip install -r /path/to/requirements.txt
```

Run the `app.py` file with:
```
py app.py
```

Now, it will run in localhost.

## Endpoint
### POST
```
  POST/predict
```
#### Input
| Key          | Info     | Data Type |
| :----------- | :------- | :------- | 
| `img_url`    | Required | string |



#### Output
| Key          | Data Type |
| :----------- | :------- | 
| `dr_class`    | string |
| `error`    | boolean |
| `message`    | string |
| `retina_detected`    | boolean |

Example:  
Input
```json
{
    "image_url": "https://storage.googleapis.com/renatic-image/1686665526642_1650786148646.jpg"
}
```
Output
```json
{
    "dr_class": "",
    "error": false,
    "message": "Retina tidak terdeteksi",
    "retina_detected": false
}
```

Input
```json
{
    "image_url": "https://storage.googleapis.com/renatic-image/0a4e1a29ffff.png"
}
```
Output
``` json
{
    "dr_class": "No DR",
    "error": false,
    "message": "Diabetic Retinopathy Level",
    "retina_detected": true
}
```

## About Member 
| Members                        | Github                                                                                                                                            | LinkedIn                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steven Ardi Christanto - M166DKX4053    | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BlackBone09)  | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/steven-ardi-398539272/)      |
| Muhammad Fakhrul Amin - M131DSX1440    | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mfakhrulam)  | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mfakhrulam/)       |
| Muhammad Naufal Kusumajaya - M038DSX1492 | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/naufaljaya) | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/naufal-kusumajaya-b27959155/)              |
