# Crop_Recommendation_Model

## **Abstract:** 

Given the soil nutrients (N, P, K), environmental factors (temperature, humidity, pH, and rainfall), 
the goal is to recommend an optimal crop. This is a classification problem where the model predicts the crop type based on soil and climate conditions.


## **Variable Information:**

This dataset is useful for building a classification model that predicts the best crop based on soil nutrients and climate conditions.

The dataset consists of 2200 records with 8 columns.
Nitrogen content (N) --->	Amount of nitrogen in the soil (N)	---> Integer
Phosphorous content (P) ---> Amount of phosphorous in the soil (P)	---> Integer
Potassium content (K) --->	Amount of potassium in the soil (K)	---> Integer
Temperature	---> Atmospheric temperature in degrees Celsius (°C)	---> Float
Humidity --->	Relative humidity in percentage (%) --->	Float
pH --->	Acidity or alkalinity of the soil (pH scale)	---> Float
Rainfall --->	Annual rainfall in millimeters (mm)	---> Float
Label --->	Type of crop recommended based on conditions Categorical ---> (String)

## **Model Building Steps**

Step 1: Importing Data Manipulation Libraries

Step 2: Loading Dataset using Pandas Function

Step 3: Model Preprocessing : Including Feature Engineering

Step 4: Split the Dataset into Train and Test [Ensuring Data Leackage Not There]

Step 5: Model Building

Step 6 : Save Pickle File