from calendar import month
import csv

#   "client_email": "chris-budget@peppy-castle-149310.iam.gserviceaccount.com",

gc = gspread.oauth(
    credentials_filename='C:\Users\P003487F\OneDrive - Parsons Corp\Desktop\Coding\budgetting\peppy-castle-149310-1f150770201d.json',
    #authorized_user_filename='path/to/the/authorized_user.json'
)

MONTH = "july"

file = f"Chase6666_{MONTH}." #set file name according to month

#open ... as csvfile opens the file for Python to interpret. 
with open(r"C:\Users\P003487F\OneDrive - Parsons Corp\Desktop\Coding\budgetting\Chase6666_july.CSV") as csvfile: 
    csv_reader = csv.reader(csvfile) #csv.reader interprets the csv file for python to do loops
    for row in csv_reader:
        #transact date, post date, description, category, type, amount
        print(row)      