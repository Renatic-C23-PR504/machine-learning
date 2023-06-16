
<div align="center">
  
  # 👁️ Machine Learning Renatic 👁️ 
  
  <img src="https://img.shields.io/github/repo-size/Renatic-C23-PR504/machine-learning?style=for-the-badge">
  <img alt="Visitor Badge" src="https://visitor-badge.feriirawann.repl.co?username=Renatic-C23-PR504&repo=machine-learning&label=VISITOR&style=for-the-badge&color=blue&contentType=svg">
  <img src="https://img.shields.io/github/contributors/Renatic-C23-PR504/machine-learning?style=for-the-badge&color=blue"></br></br>
</div>
  
This repository is used to build machine learning models to predict whether a person has diabetes or not based on clinical data and to detect diabetic retinopathy based on eye images.

# Resource
* Dataset: For clinic data, we use [Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set). For diabetic retinopathy classification we use [Diabetic Retinopathy Arranged Dataset on Kaggle](https://www.kaggle.com/datasets/amanneo/diabetic-retinopathy-resized-arranged) and custom dataset [Eye and Not Eye Classification](https://github.com/Renatic-C23-PR504/machine-learning/tree/main/image_data/eyes_classification/dataset)
* Model : For clinic data, we use XGBoost classifier. For diabetic retinopathy classification, we use Tensorflow

# About Member Machine Learning Path
| Members                        | Github                                                                                                                                            | LinkedIn                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steven Ardi Christanto - M166DKX4053    | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BlackBone09)  | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/steven-ardi-398539272/)      |
| Muhammad Fakhrul Amin - M131DSX1440    | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mfakhrulam)  | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mfakhrulam/)       |
| Muhammad Naufal Kusumajaya - M038DSX1492 | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/naufaljaya) | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/naufal-kusumajaya-b27959155/)              |

# Model Development
## Clinic Data
For machine learning algorithm, we use XGBoost Classifier. In terms of the features, there are eight variables: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age. And the output are binary, 0 if there is no diabetes and 1 if there is a diabetes. We also doing feature engineering so that our model get higher accuracy. At the end we got 94% accuracy.

## Diabetic Retinopathy Classification
We built two models for this classification. The first is to classify whether the image is an eye or not, and the second is to classify the type of diabetic retinopathy. The first model we built uses a simple CNN architecture because the features contained in the eye or retina are obviously very different from other objects, such as cars, cats or humans. This model is used as a filter to ensure that the images fed into the diabetic retinopathy classification model are images of the retina of the eye. The second model we built uses transfer learning techniques to speed up the training process and produce a good model. We use the pre-trained MobileNetV2 model that is already available in the [Keras application](https://keras.io/api/applications/mobilenet/#mobilenetv2-function).

### Architecture 
The detail model architecture for the "eye/not-eye" model are using tensorflow sequential model as shown below.
  * Conv2D layer (`filter = 16`, `kernel size = (3,3)`, `input shape = (150,150,3)`)
  * MaxPooling2D layer (`(2,2) pool size`)
  * Conv2D layer (`filter = 32`, `kernel size = (3,3)`)
  * MaxPooling2D layer (`(2,2) pool size`)
  * Flatten layer
  * Dense layer (`64 unit size`, `activation = relu`)
  * Dense layer (`1 unit size`, `activation = sigmoid`)


While the details of the model architecture for diabetic retinopathy can be seen below.
  * Pretrained layer (`MobileNetV2`)
  * Globar Average Pooling layer 
  * Dropout layer (`0.4`)
  * Dense layer (`128 unit size`, `activation = relu`)
  * Dense layer (`5 unit size`, `activation = softmax`)

### Metrics 
#### Eye Classification Model
<div style="display:flex"> 
  <img width="50%" src="https://raw.githubusercontent.com/Renatic-C23-PR504/machine-learning/main/assets/output_accuracy_eye_classification.png">

  <img width="50%" src="https://raw.githubusercontent.com/Renatic-C23-PR504/machine-learning/main/assets/output_loss_eye_classification.png">
</div>

#### Diabetic Retinopathy Classification Model

![metrics.png](https://raw.githubusercontent.com/Renatic-C23-PR504/machine-learning/main/assets/metrics.png)

<!-- Tables -->
| Metrics      | Diabetic Retinopathy    | Eye |
| ------------ | ------ | -------------------- |
| accuracy     | 0.7425 | 0.9985 |
| val_accuracy | 0.7411 | 1.0000 |
| loss         | 0.7776 | 7.1724e-04 |
| val_loss     | 0.7704 | 0.0040 |

# Mode Deployment
For deployment we separate clinic data and diabetic retinopathy classification to avoid compatibility issue. Both are using Flask to deploy the model to Google Cloud Run
## Clinic Data
For dependecies all listed in [requirement.txt](https://github.com/Renatic-C23-PR504/machine-learning/blob/main/clinic-data/deployment/requirement.txt)
### Endpoint
#### POST
```
  POST/
```
##### Input
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

##### Output
| Key          | Data Type |
| :----------- | :------- | 
| `advice`    | string |
| `prediction`    | boolean |
| `probabilty`    | string |

## Diabetic Retinopathy Classification 
For dependecies all listed in [requirement.txt](https://github.com/Renatic-C23-PR504/machine-learning/blob/main/image_data/requirement.txt) 
### Endpoint
#### POST
```
  POST/predict
```
##### Input
| Key          | Info     | Data Type |
| :----------- | :------- | :------- | 
| `img_url`    | Required | string |

##### Output
| Key          | Data Type |
| :----------- | :------- | 
| `dr_class`    | string |
| `error`    | boolean |
| `message`    | string |
| `retina_detected`    | boolean |

