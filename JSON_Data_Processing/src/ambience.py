import json
import csv

#Create a seperate table for the Hours property
with open("business100ValidForm.json") as file:
    json_string = file.read()

data = json.loads(json_string)

header = ['ID', 'Name', 'romantic', 'intimate', 'classy', 'hipster', 'divey', 'touristy',
          'trendy', 'upscale', 'casual']

with open('ambience.csv', 'w', newline="") as data_dump:
    writer = csv.DictWriter(data_dump, fieldnames=header)
    writer.writeheader()

    for i in range(100):
        ambience = \
            {
                "ID": data['Business'][i]['business_id'],
                "Name": data['Business'][i]['name']
            }
        for key in data['Business'][i]['attributes']:
            if key == 'Ambience':
                for key in data['Business'][i]['attributes']['Ambience']:
                    if key in header:
                        ambience[key] = data['Business'][i]['attributes']['Ambience'][key]
        writer.writerow(ambience)