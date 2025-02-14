def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Example preprocessing steps
    data = data.dropna()  # Remove missing values
    data = data.reset_index(drop=True)  # Reset index
    return data