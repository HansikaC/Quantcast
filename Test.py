import sys
from datetime import date, datetime, time

# if invalid arguments are passed then,
if len(sys.argv) != 4 or sys.argv[2] != '-d':
    print("\nCommand to be used: ./most_active_cookie cookie_log.csv -d 2018-12-09\n")
    print(f"Please correct the command to {sys.argv[0]} <csv_file_name> -d \"yyyy-mm-dd\"\n")
    exit(1)

# we convert given date to datetime object
date_time = datetime.strptime(sys.argv[3], "%Y-%m-%d")
#print("date_time",date_time,"----------------------------------\n")

# here we keep the number of occurrences of cookies
cookie_logs = {}

# here we open csv file in read mode
file_data = open(sys.argv[1], "r")
#print("cookie_log",cookie_log,"----------------------------------\n")

for row in file_data.readlines()[1:]:

    row = row.replace("\n", "")
    #print("row",row,"\n")

    cookie, timestamp = row.split(",")
    #print("cookie is ",cookie,"timestamp is ", timestamp,"\n")

    tmp_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')
    #print("tmp_datetime is ", tmp_datetime,"\n==========================\n")

    # Here we count the occurances of each cookie
    if date_time.strftime('%Y-%m-%d') == tmp_datetime.strftime('%Y-%m-%d'):
        if cookie in cookie_logs:
            cookie_logs[cookie] += 1
        else:
            cookie_logs[cookie] = 1

# Now we get the cookie with highest number of occurences
most_logged = max(cookie_logs.values())

for item, occurrences in cookie_logs.items():
    if occurrences == most_logged:
        print(item)

# Now we can close the file
file_data.close()