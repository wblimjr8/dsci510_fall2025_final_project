from src.merge_cms import merge_cms_datasets
from src.analyze_cms import analyze_cms_data
from src.load_additional import load_kaggle_readmissions
from src.clean_data import clean_kaggle_data
from src.model import train_models

def main():
    print("Step 1: Analyze CMS Readmission Data")
    analyze_cms_data()  # loads CMS, merges, saves plots

    print("\nStep 2: Load and Clean Kaggle Readmission Data")
    df_raw = load_kaggle_readmissions()
    df_clean = clean_kaggle_data(df_raw)

    print("\nStep 3: Train Predictive Models")
    train_models(df_clean)

    print("\nPipeline complete. Check the results/ folder for plots.")

if __name__ == "__main__":
    main()
