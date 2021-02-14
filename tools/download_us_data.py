"""
Download US cases data to 'US.csv'
Simply pass the country name as the first argument.
NOTE: You need to run date-sort.py after running this.
"""
import requests
from tqdm import tqdm
import csv
from io import StringIO
from datetime import datetime

country = "US"

print("Getting a list of CSV files available for download...")
r = requests.get("https://api.github.com/repos/CSSEGISandData/COVID-19/contents/csse_covid_19_data/csse_covid_19_daily_reports")
csv_files = {}
for i in r.json():
    if(not i["name"].endswith(".csv")):
        continue
    date = i["name"].strip(".csv")
    csv_files[date] = i["download_url"]

print("Downloading and parsing CSV files...")
final_data = []
for i in tqdm(csv_files):
    r = requests.get(csv_files[i], stream=True)
    csv_stream = StringIO()
    for chunk in r.iter_content(1024):
        csv_stream.write(chunk.decode())
    csv_stream.seek(0)
    reader = csv.DictReader(csv_stream)
    cases = 0
    deaths = 0
    for x in reader:
        country_region = x.get("Country_Region") if x.get("Country_Region") else x.get("Country/Region")
        if(country_region == country):
            try:
                cases += int(x["Confirmed"])
                deaths += int(x["Deaths"])
            except:
                pass
    try:
        final_data.append({
            "date": datetime.strptime(i, "%m-%d-%Y").strftime("%Y-%m-%d"),
            "cases": cases,
            "deaths": deaths
        })
    except:
        pass

print(f"Writing to {country}.csv...")
with open(f"{country}.csv", "w") as f:
    fieldnames = ["date", "cases", "deaths"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in tqdm(final_data):
        writer.writerow(i)

print("Finished.")
print(f"Downloaded and parsed {len(csv_files)} CSV data files.")