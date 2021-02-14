"""
Sort the downloaded dataset by date
Simply pass the path to the CSV file as the first argument and the output filenames as the second argument
WARNING: It will load the entire CSV file into memory
"""
import csv
from datetime import datetime
import sys
from tqdm import tqdm

csv_file_path = sys.argv[1]
output_file_path = sys.argv[2]

reader = csv.DictReader(open(csv_file_path, "r"))
items = list(reader)
def sort_func(item):
    return datetime.strptime(item["date"], "%Y-%m-%d")
items.sort(key=sort_func)

with open(output_file_path, "w") as f:
    fieldnames = ["date", "cases", "deaths"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in tqdm(items):
        writer.writerow(i)