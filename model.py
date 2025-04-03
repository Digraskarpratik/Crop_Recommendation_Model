# Importing Data Manipulation Libraries
import numpy as np
import pandas as pd

# Importing Data Visualization Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Importing Warining Libraries to ignore warnings
import warnings
warnings.filterwarnings('ignore')

# importing machine learning libraries
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.metrics import  accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Importing Data Logging Libraries
import logging
logging.basicConfig(level=logging.INFO,
                    filemode= "w",
                    filename='app.log',
                    format = '%(asctime)s - %(levelname)s - %(message)s')

url = "https://raw.githubusercontent.com/Digraskarpratik/Crop_Recommendation_Model/refs/heads/main/Crop_Recommendation.csv"

df = pd.read_csv(url)
df.sample(frac=1)

from sklearn.preprocessing import LabelEncoder
df["Crop"] = LabelEncoder().fit_transform(df["Crop"])

X = df.drop(columns = ["Crop","Rainfall"] , axis= 1)
y= df["Crop"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 0.70, random_state= 42)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

RF = RandomForestClassifier()

RF.fit(X_train, y_train)

y_pred_RF = RF.predict(X_test)

accuracy_score_RF = accuracy_score(y_test, y_pred_RF)

print(f"accuracy Score for Random Forest: {round(accuracy_score_RF,2)}%")