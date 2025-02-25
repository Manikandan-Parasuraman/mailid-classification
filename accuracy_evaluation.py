import pandas as pd
from transformers import pipeline

# Load model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)

# Load dataset
df = pd.read_csv("email_dataset.csv")

# Function to evaluate accuracy
def evaluate_model(df):
    correct = 0
    for _, row in df.iterrows():
        email = row["email"]
        expected_label = row["label"]
        domain = email.split("@")[-1]
        labels = ["organization email", "public email"]
        result = classifier(domain, labels)
        predicted_label = result["labels"][0]

        if predicted_label == expected_label:
            correct += 1

    accuracy = correct / len(df) * 100
    return accuracy

# Run evaluation
accuracy = evaluate_model(df)
print(f"Model Accuracy: {accuracy:.2f}%")
