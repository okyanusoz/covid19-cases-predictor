"""
Creates data.json.
Simply pass the CSV data file path as the first argument.
"""
import sys
import os
# We need to do this to fix imports
sys.path.append(os.getcwd())
from predict_cases import predict_cases
from predict_deaths import predict_deaths
import json
import csv
from datetime import datetime, timedelta

print("Retreiving latest date available...")
reader = csv.DictReader(open(sys.argv[1], "r"))
latest = None
for i in reader:
    latest = i
print("Retreiving tomorrow's date(from the latest date available)...")
current = datetime.strptime(latest["date"], "%Y-%m-%d")
tomorrow = current + timedelta(days=1)

data = {
    "prediction": {
        "date": tomorrow.strftime("%Y-%m-%d")
    },
    "current": {
        "date": current.strftime("%Y-%m-%d"),
        "cases": int(latest["cases"]),
        "deaths": int(latest["deaths"])
    }
}

print("Predicting cases...")
predicted_cases = predict_cases(sys.argv[1])
data["prediction"]["cases"] = predicted_cases

print("Predicting deaths...")
predicted_deaths = predict_deaths(sys.argv[1])
data["prediction"]["deaths"] = predicted_deaths

print("Saving predictions to data.json...")
with open("data.json", "w") as f:
    f.write(json.dumps(data, indent=4))