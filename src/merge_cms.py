import pandas as pd
from src.load import load_cms_data
from src.load_hospital_info import load_hospital_info

def merge_cms_datasets():
    df_hrrp = load_cms_data()
    df_info = load_hospital_info()

    # Standardize the merge key
    df_hrrp["Facility ID"] = df_hrrp["Facility ID"].astype(str)
    df_info["Facility ID"] = df_info["Facility ID"].astype(str)

    # Perform merge
    df_merged = df_hrrp.merge(df_info, on="Facility ID", how="inner")

    print("Merged CMS dataset shape:", df_merged.shape)
    return df_merged

if __name__ == "__main__":
    merge_cms_datasets()