import json
import csv

#Create a seperate table for the Hours property
with open("business100ValidForm.json") as file:
    json_string = file.read()

data = json.loads(json_string)

header_hours = ['ID', 'Name', 'Monday Open', 'Monday Closed', 'Tuesday Open', 'Tuesday Closed',
                'Wednesday Open', 'Wednesday Closed', 'Thursday Open', 'Thursday Closed',
                'Friday Open', 'Friday Closed', 'Saturday Open', 'Saturday Closed', 'Sunday Open', 'Sunday Closed']
with open('hours.csv', 'w', newline="") as data_dump2:
    writer = csv.DictWriter(data_dump2, fieldnames=header_hours)
    writer.writeheader()

    for i in range(100):
        hours = \
        {
            "ID": data['Business'][i]['business_id'],
            "Name": data['Business'][i]['name'],
        }
        for days in data['Business'][i]['hours']:
                hours[days + ' Open'] = data['Business'][i]['hours'][days]['open']
                hours[days + ' Closed'] = data['Business'][i]['hours'][days]['close']
        writer.writerow(hours)