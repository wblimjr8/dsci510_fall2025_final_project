import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import os

def train_models(df):
    # Split features and target
    X = df.drop(columns=["target"])
    y = df["target"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Logistic Regression
    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(X_train, y_train)

    y_pred_lr = log_reg.predict(X_test)
    lr_acc = accuracy_score(y_test, y_pred_lr)
    print("Logistic Regression Accuracy:", lr_acc)

    # Random Forest
    rf = RandomForestClassifier(n_estimators=150, random_state=42)
    rf.fit(X_train, y_train)

    y_pred_rf = rf.predict(X_test)
    rf_acc = accuracy_score(y_test, y_pred_rf)
    print("Random Forest Accuracy:", rf_acc)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred_rf)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix (Random Forest)")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    os.makedirs("results", exist_ok=True)
    plt.savefig("results/confusion_matrix.png")
    plt.close()

    # Feature Importance
    importances = pd.Series(rf.feature_importances_, index=X.columns)
    importances.sort_values(ascending=False).plot(kind="bar", figsize=(12,6))
    plt.title("Feature Importance (Random Forest)")
    plt.tight_layout()
    plt.savefig("results/feature_importance.png")
    plt.close()

    print("Modeling complete. Plots saved in /results/.")
