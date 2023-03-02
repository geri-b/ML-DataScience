import json
import csv

#Create a seperate table for the Hours property
with open("business100ValidForm.json") as file:
    json_string = file.read()

data = json.loads(json_string)

header = ['ID', 'Name', 'garage', 'street', 'validated', 'lot', 'valet']

with open('parking.csv', 'w', newline="") as data_dump:
    writer = csv.DictWriter(data_dump, fieldnames=header)
    writer.writeheader()

    for i in range(100):
        parking = \
            {
                "ID": data['Business'][i]['business_id'],
                "Name": data['Business'][i]['name']
            }
        for key in data['Business'][i]['attributes']:
            if key == 'Parking':
                for key in data['Business'][i]['attributes']['Parking']:
                    if key in header:
                        parking[key] = data['Business'][i]['attributes']['Parking'][key]
        writer.writerow(parking)