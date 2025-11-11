import pandas as pd

def load_cms_data():
    # Load CMS Hospital Readmissions Reduction Program data via API
    url = "https://data.cms.gov/provider-data/api/1/datastore/query/9n3s-kdb3/0/download?format=csv"
    df = pd.read_csv(url)
    print(f"Loaded {len(df)} rows from CMS API CSV data")
    return df

if __name__ == "__main__":
    load_cms_data()