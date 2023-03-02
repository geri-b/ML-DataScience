import json
import csv

#Create a seperate table for the Hours property
with open("business100ValidForm.json") as file:
    json_string = file.read()

data = json.loads(json_string)

header = ['ID', 'Name', 'dessert', 'latenight', 'lunch', 'dinner', 'brunch', 'breakfast']

with open('speciality.csv', 'w', newline="") as data_dump:
    writer = csv.DictWriter(data_dump, fieldnames=header)
    writer.writeheader()

    for i in range(100):
        speciality = \
            {
                "ID": data['Business'][i]['business_id'],
                "Name": data['Business'][i]['name']
            }
        for key in data['Business'][i]['attributes']:
            if key == 'Good For':
                for key in data['Business'][i]['attributes']['Good For']:
                    if key in header:
                        speciality[key] = data['Business'][i]['attributes']['Good For'][key]
        writer.writerow(speciality)