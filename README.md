# Real-time-forest-fire-detection-using-ML-
This repo presents an efficient Machine Learning model that predicts forest fires with utmost  accuracy using the real time weather info from a 3rd party API.
# Direction to implement the project
Firstly, download all the data files attached to this repo. 

Secondly, make sure all the libraries are installed properly in your system. Namely -
flask, requests, os, sengrid, pandas, sklearn

Thirdly, we open our IDE then we run main.py in the terminal using the command - 'python main.py'
# Abstract
Forest fires destroy natural life and demolish lands that provide a livelihood. Accurate prediction 
of fire occurrence is required in order to reduce its adverse effects. This paper presents an 
effective and reliable solution to predict the forest fires so as to minimize their effects. The 
current solution to this problem is to gather info through sensors which are placed at several 
locations inside of the forest and predict the chances of occurrence of fire. But this method is 
quite expensive and requires maintenance.
# Work Break down structure
![image](https://github.com/Prats13/Real-time-forest-fire-detection-using-ML-/assets/93511663/347c8d8d-853d-40a9-8b36-1f61b4d935db)
# Methodology
Pre-Processing the Data: 

  ● The Dataset that would be used by the ML model would contain a lot of unnecessary information. So, preprocessing is necessary. 
  
  ● Only the required attributes are selected to form the data frame.
  
  ● The rows with NaN values would either be deleted or would be filled with the median value of that column. 
  
  ● Outliers must be removed before it is fed into the model. 

Creating the Machine Learning Model: 

  ● Various Machine Learning Models including Regression and Classification would be developed that would predict the chances of forest fires. 
  
  ● The Model would be trained using the training set obtained after preprocessing the dataset. 
  
  ● Efficiency of each model will be checked using the test dataset and accordingly the best model will be selected.

Creating the web application to deploy our model: 

  ○ The web application would send a http request to the Weather Stack API, that would send us the weather data in JSON format. 
  
  ○ We will retrieve the necessary information and feed it to the ML model at the backend. 
  
  ○ The model will predict the chances of the forest fire and send it back to the web application which would then be displayed on the web page. 
  
  ○ Every time the web page is visited or refreshed; the same process would be continued.
  
# Machine Learning Algorithm implemented
We have used decision tree algorithms which gives more accuracy for less data 

 1)extratreeregressor 

 2)decision tree classifier 
 
 3)random forest regressor 
 
 4)bagging regressor 
 
Among these machine learning models extra tree regression give best accuracy so we have implemented it in our application
# Screenshots of Implementation
