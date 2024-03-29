import json
import csv
import re


def json_to_csv(json_file, csv_file):
    with open(json_file, "r") as f:
        data = json.load(f)

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def coins_to_hryvnia(coins):
    hryvnia = coins / 100
    return hryvnia


def remove_prefix(string):
    updated_string = re.sub(r"В[іi]д: ", "", string)
    return updated_string
