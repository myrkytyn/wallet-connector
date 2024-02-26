from datetime import datetime, timedelta


# Converts date from format dd.mm.yyyy -> Unix Timestamp
def date_to_unix_timestamp(date):
    if is_timestamp(date):
        return date
    else:
        dt = datetime.strptime(date, "%d.%m.%Y")
        unix_timestamp = int(dt.timestamp())
        return unix_timestamp


# Converts date from format Unix Timestamp -> dd.mm.yyyy
def unix_timestamp_to_date(unix_timestamp):
    dt = datetime.fromtimestamp(unix_timestamp)
    date = dt.strftime("%d.%m.%Y %H:%M")

    return date


def is_timestamp(timestamp):
    try:
        datetime.fromtimestamp(timestamp)
        return True
    except OSError:
        return False


def get_timestamps(period):
    """
    Get timestamps for time period.

    Parameters:
        period (str): The time period. It can be one of the following:
            - "current_month": Process data for the current month.
            - "previous_month": Process data for the previous month.
            - "today": Process data for today.
            - "yesterday": Process data for yesterday.

    Returns:
        timestamp_from, timestamp_to
    """
    if period == "previous_month":
        today = datetime.today()
        first_day_of_current_month = today.replace(day=1)
        last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
        first_day_of_previous_month = last_day_of_previous_month.replace(day=1)

        timestamp_from = int(
            first_day_of_previous_month.replace(hour=0, minute=0, second=1).timestamp()
        )
        timestamp_to = int(
            last_day_of_previous_month.replace(
                hour=23, minute=59, second=59
            ).timestamp()
        )
        return timestamp_from, timestamp_to
