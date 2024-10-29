import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    # Load dataset
    data = pd.read_csv('code_dataset.csv')  
    X = data['code']
    y = LabelEncoder().fit_transform(data['label'])
    return X, y
