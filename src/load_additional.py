import pandas as pd

def load_hospital_info():
    """ 
    Loads CMS Hospital General Information dataset.
    This dataset contains hospital type, ownership, ratings, etc.
    """
    url = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0/download?format=csv"
    df = pd.read_csv(url)
    print(f"Loaded hospital info dataset: {len(df)} rows")
    return df

def load_kaggle_readmissions(path="data/diabetes_readmission.csv"):
    """
    Loads the Kaggle diabetes readmissions dataset.
    """
    df = pd.read_csv(path)
    print(f"Loaded Kaggle readmissions dataset: {len(df)} rows")
    return df


if __name__ == "__main__":
    load_hospital_info()