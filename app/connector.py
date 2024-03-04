import csv
from converter import coins_to_hryvnia, remove_prefix

from settings import TIME_DIFFERENCE
from utils import unix_timestamp_to_date


def change_data_in_csv(input_file, output_file):
    with open(input_file, "r", newline="") as infile, open(
        output_file, "w", newline=""
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        writer.writerow(next(reader))

        for row in reader:
            # Timestamp - time difference (Wallet adds 2 hours to the time of transaction)
            row[1] = unix_timestamp_to_date(int(row[1]) + int(TIME_DIFFERENCE))
            row[2] = remove_prefix(row[2])
            row[6] = coins_to_hryvnia(int(row[6]))
            row[7] = coins_to_hryvnia(int(row[7]))
            row[9] = coins_to_hryvnia(int(row[9]))
            row[10] = coins_to_hryvnia(int(row[10]))
            row[11] = coins_to_hryvnia(int(row[11]))
            writer.writerow(row)
