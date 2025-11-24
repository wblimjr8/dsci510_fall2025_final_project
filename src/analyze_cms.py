import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.merge_cms import merge_cms_datasets

def analyze_cms_data():
    df = merge_cms_datasets()

    # Plot 1: Readmission Ratio by Hospital Type
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df,
        x="Hospital Type",
        y="Excess Readmission Ratio",
        estimator="mean",
        errorbar=None
    )
    plt.xticks(rotation=45, ha="right")
    plt.title("Average Excess Readmission Ratio by Hospital Type")
    plt.tight_layout()
    plt.savefig("results/cms_readmission_by_type.png")
    plt.close()

    # Plot 2: Readmission Ratio by Hospital Ownership
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df,
        x="Hospital Ownership",
        y="Excess Readmission Ratio",
        estimator="mean",
        errorbar=None
    )
    plt.xticks(rotation=45, ha="right")
    plt.title("Excess Readmission Ratio by Hospital Ownership")
    plt.tight_layout()
    plt.savefig("results/cms_readmission_by_ownership.png")
    plt.close()

    # Plot 3: Star Rating vs Readmission Ratio

    # Convert columns to numeric
    df["Hospital overall rating"] = pd.to_numeric(df["Hospital overall rating"], errors="coerce")
    df["Excess Readmission Ratio"] = pd.to_numeric(df["Excess Readmission Ratio"], errors="coerce")

    # Filter valid rows
    df_filtered = df.dropna(subset=["Hospital overall rating", "Excess Readmission Ratio"]).copy()

    # Using .loc
    df_filtered.loc[:, "Hospital overall rating"] = df_filtered["Hospital overall rating"].astype(float)
    df_filtered.loc[:, "Excess Readmission Ratio"] = df_filtered["Excess Readmission Ratio"].astype(float)

    # Assert correct types
    assert df_filtered["Hospital overall rating"].dtype != "object"
    assert df_filtered["Excess Readmission Ratio"].dtype != "object"

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df_filtered,
        x="Hospital overall rating",
        y="Excess Readmission Ratio",
        alpha=0.4
    )

    sns.regplot(
        data=df_filtered,
        x="Hospital overall rating",
        y="Excess Readmission Ratio",
        scatter=False,
        color="red"
    )

    plt.title("Hospital Overall Rating vs Readmission Ratio")
    plt.tight_layout()
    plt.savefig("results/cms_rating_vs_readmission.png")
    plt.close()
    
    print("CMS analysis complete. Plots saved in /results/.")

if __name__ == "__main__":
    analyze_cms_data()
