import datetime

def unix_to_standard_string(unix_tstamp):
    return datetime.datetime.fromtimestamp(int(unix_tstamp)).strftime('%a %b %d %H:%M:%S %Y')

def unix_to_timestamp_string(unix_tstamp):
    return datetime.datetime.fromtimestamp(int(unix_tstamp)).strftime('%Y-%m-%d %H:%M:%S %Y')
