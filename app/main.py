import os

from connector import change_data_in_csv
from monobank import init_monobank
from monobank import get_all_statements
from datetime import datetime


def main():
    init_monobank()

    get_all_statements()

    for subdir in os.listdir("data/monobank"):
        subdir_path = os.path.join("data/monobank", subdir)
        if os.path.isdir(subdir_path):
            for filename in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, filename)
                if os.path.isfile(file_path):
                    parts = file_path.split(".")
                    current_date = datetime.now()
                    updated_file_path = f"{parts[0]} {current_date.strftime("%b %d")}.{parts[1]}"
                    change_data_in_csv(file_path, f"{updated_file_path}")


if __name__ == "__main__":
    main()
