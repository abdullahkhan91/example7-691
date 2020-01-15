#!/usr/bin/env python3

import csv
from datetime import datetime

# 1. load input.csv into a variable called `polls`
with open("input.csv") as f:
	reader = csv.DictReader(f)
	rows = list(reader) 
	rows = [dict(row) for row in rows]
print(rows)

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"
with open("output.csv", "w") as f: 
	writer = csv.writer(f)
	writer.writerow(["date", "approve"])


# 3. Loop through each row of `polls` 
	for row in rows:
		date = row ["enddate"]
		date_format = "%m/%d/%Y"
		approve = row["approve"]
	    # 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
	    # hint: to read the date you will need to use
	    #       date = datetime.datetime.strptime(myrawstring, "insert input format here")	
	    #       and to write the date you will need to use something like 
	    #       new_date = date.strftime("insert output format here")
	    # 
	    #       date formats can be found at https://strftime.org/
		parsed_date = datetime.strptime(date, date_format)
		new_date = parsed_date.strftime("%-d-%b-%y")
    # 5. write a new row of data with the transformed date and value for "approve" 
		writer.writerow([new_date, approve])
#By Ryuichiro and Abdullah