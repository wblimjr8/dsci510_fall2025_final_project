import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_kaggle_data(df):
    """
    Cleans the Kaggle readmission dataset:
    - Normalizes missing values
    - Converts all categorical columns to numeric
    - Creates numeric age column
    - Encodes diag_1, diag_2, medical_specialty properly
    """

    # Normalize missing-like values
    df = df.replace(
        ["Missing", "?", "None", "unknown", "Unknown", "missing"], 
        "Unknown"
    )

    # Convert age ranges ("[70-80)") to numeric midpoint
    def parse_age(age_str):
        if isinstance(age_str, str) and "-" in age_str:
            low = int(age_str.strip("[]()").split("-")[0])
            high = int(age_str.strip("[]()").split("-")[1])
            return (low + high) / 2
        return 0

    df["age_num"] = df["age"].apply(parse_age)
    df = df.drop(columns=["age"])

    # Binary target: yes → 1, no → 0
    df["target"] = df["readmitted"].apply(lambda x: 1 if x == "yes" else 0)

    # Identify all categorical columns left
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    # Remove original target
    if "readmitted" in categorical_cols:
        categorical_cols.remove("readmitted")

    # Label encode all remaining categorical columns
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

    # Drop original readmitted
    df = df.drop(columns=["readmitted"])

    # Fill any remaining NaN
    df = df.fillna(0)

    print("Cleaning done. Dataset shape:", df.shape)
    print("Categorical columns encoded:", categorical_cols)

    return df