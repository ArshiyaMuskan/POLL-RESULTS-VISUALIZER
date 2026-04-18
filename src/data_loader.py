import pandas as pd

def load_data():
    df = pd.read_csv("data/poll_data.csv")
    return df