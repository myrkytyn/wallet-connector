import json
import os
import requests
import csv
import time

from utils import get_timestamps


from settings import MONOBANK_PATH, MONOBANK_TOKEN, ACCOUNT, PERIOD, CUSTOM_NAMES

from utils import date_to_unix_timestamp


def init_monobank():
    if os.path.exists(MONOBANK_PATH):
        return

    os.makedirs(f"./{MONOBANK_PATH}")

    response = get_monobank_client_info()
    client_info = parse_client_info(response)

    with open(f"{MONOBANK_PATH}/client_info.json", "w") as json_file:
        json.dump(client_info, json_file, ensure_ascii=False, indent=4)


def parse_client_info(client_info):
    client_info = {
        "client_id": client_info["clientId"],
        "name": client_info["name"],
        "accounts": [
            {
                "id": account["id"],
                "currency_code": account["currencyCode"],
                "balance": account["balance"],
                "type": account["type"],
                "iban": account["iban"],
            }
            for account in client_info["accounts"]
        ],
        "jars": [
            {
                "id": jar["id"],
                "title": jar["title"],
                "description": jar["description"],
                "currency_code": jar["currencyCode"],
                "balance": jar["balance"],
                "goal": jar["goal"],
            }
            for jar in client_info["jars"]
        ],
    }
    return client_info


def get_monobank_client_info():
    url = "https://api.monobank.ua/personal/client-info"

    headers = {"X-Token": MONOBANK_TOKEN}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return None


def get_account_statement(account_id, date_from, date_to=""):
    unix_date_from = date_to_unix_timestamp(date_from)
    if date_to:
        unix_date_to = date_to_unix_timestamp(date_to)
    else:
        unix_date_to = ""

    url = f"https://api.monobank.ua/personal/statement/{account_id}/{unix_date_from}/{unix_date_to}"

    headers = {"X-Token": MONOBANK_TOKEN}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.text
        return data
    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return None


def get_all_statements():
    period = PERIOD

    with open(f"{MONOBANK_PATH}/client_info.json", "r") as file:
        client_info = json.load(file)

    if period == "latest":
        from_timestamp = int(time.time())
        to_timestamp = int(client_info["latest_synchronization"])
    else:
        from_timestamp, to_timestamp = get_timestamps(period)

    skip_first_time = True
    for account in client_info["accounts"]:
        if not skip_first_time:
            time.sleep(60)
        else:
            skip_first_time = False

        account_id = account["id"]

        if CUSTOM_NAMES:
            account_name = account["custom_name"]
        else:
            account_name = account_id

        try:
            statement = get_account_statement(account_id, from_timestamp, to_timestamp)
            if statement != None and statement and statement != "[]":
                statement = json.loads(statement)
            else:
                raise ValueError("Value cannot be None")
        except Exception:
            continue

        write_to_csv(account_name, statement)


def write_to_csv(account_name, statement):
    if not os.path.exists(f"{MONOBANK_PATH}/{account_name}"):
        os.makedirs(f"{MONOBANK_PATH}/{account_name}")

    fieldnames = [
        "id",
        "time",
        "description",
        "comment",
        "mcc",
        "originalMcc",
        "amount",
        "operationAmount",
        "currencyCode",
        "commissionRate",
        "cashbackAmount",
        "balance",
        "hold",
        "receiptId",
    ]
    with open(
        f"{MONOBANK_PATH}/{account_name}/{account_name}.csv", "w", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in statement:
            row_to_csv = {key: row.get(key, "") for key in fieldnames}
            writer.writerow(row_to_csv)
