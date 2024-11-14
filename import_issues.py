import csv
import requests

# Configuration
GITHUB_TOKEN = "y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"
REPO = "taylor-allen/taylor-allen"  # Replace with your GitHub repo name
API_URL = f"https://api.github.com/repos/{REPO}/issues"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Read the CSV file
with open("GitHub_Project_Board_Import.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Prepare the issue data
        issue_data = {
            "title": row["Title"],
            "body": row["Description"],
            "labels": [row["Labels"]] if row["Labels"] else []
        }
        # Create the issue
        response = requests.post(API_URL, json=issue_data, headers=HEADERS)
        if response.status_code == 201:
            print(f"Successfully created issue: {row['Title']}")
        else:
            print(f"Failed to create issue: {row['Title']}")
            print(response.json())
