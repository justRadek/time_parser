import datetime, re

insert_text = input("Please insert text which should be parsed: ")

search = re.search('\d{2}:\d{2}:d{2}', insert_text, re.I)
                   #('|\d{2}:\d{2}:d{2}(AM)|\d{2}:\d{2}:d{2}(PM)', insert_text, re.I)

datetime = datetime.datetime.strptime(search, '%H:%M:%S').date()

print("time is: ", datetime.time())






