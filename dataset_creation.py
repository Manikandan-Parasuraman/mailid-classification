import random

# Common public email domains
public_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com", "aol.com", "zoho.com"]

# Example organization email domains
org_domains = [
    "company.com", "enterprise.org", "startup.io", "business.net", "corporate.tech",
    "techfirm.ai", "financecorp.com", "healthcare.org", "education.edu", "government.gov"
]

# Generate dataset
dataset = []
for _ in range(500):  # 500 public emails
    email = f"user{random.randint(1, 10000)}@{random.choice(public_domains)}"
    dataset.append((email, "public email"))

for _ in range(500):  # 500 organization emails
    email = f"employee{random.randint(1, 10000)}@{random.choice(org_domains)}"
    dataset.append((email, "organization email"))

# Shuffle the dataset
random.shuffle(dataset)

# Save as a CSV file
import csv

with open("email_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["email", "label"])
    writer.writerows(dataset)

print("1000-sample dataset saved as email_dataset.csv")
