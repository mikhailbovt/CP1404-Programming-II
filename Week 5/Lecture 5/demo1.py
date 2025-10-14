import csv
import os
FILENAME = os.path.join(os.path.dirname(__file__), "countries.csv")

def main():
    country_to_data = read_data(FILENAME)
    print_details(country_to_data)
def read_data(filename):
    country_to_data = {}
    with open(filename) as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            record[2] = int(record[2].replace(",", ""))
            record[3] = float(record[3][:-1])
            country_to_data[record[0]] = record[1:-1]
    return country_to_data

def print_details(country_to_data):
    country_names = sorted(country_to_data.keys())

main()