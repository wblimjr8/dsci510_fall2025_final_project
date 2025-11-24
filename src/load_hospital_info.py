import pandas as pd

def load_hospital_info():
    """
    Loads CMS Hospital General Information dataset (xubh-q36u)
    Returns a cleaned dataframe.
    """
    url = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0/download?format=csv"
    df = pd.read_csv(url)
    print(f"Loaded {len(df)} rows from CMS Hospital General Info API")
    return df

if __name__ == "__main__":
    load_hospital_info()