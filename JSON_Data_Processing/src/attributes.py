import json
import csv

#Create a seperate table for the Attributes property
with open("business100ValidForm.json") as file:
    json_string = file.read()

data = json.loads(json_string)

header = ['ID', 'Name', 'Happy Hour', 'Take-out', 'Drive-Thru', 'Caters', 'Noise Level',
          'Takes Reservations', 'Delivery', 'Has TV', 'Outdoor Seating',
          'Attire', 'Alcohol', 'Waiter Service', 'Accepts Credit Cards',
          'Good for Kids', 'Good For Groups', 'Good For Dancing', 'Price Range', 'Wi-Fi', 'Smoking', 'Coat Check']

with open('attributes.csv', 'w', newline="") as data_dump:
    writer = csv.DictWriter(data_dump, fieldnames=header)
    writer.writeheader()

    for i in range(100):
        attributes = \
            {
                "ID": data['Business'][i]['business_id'],
                "Name": data['Business'][i]['name']
            }
        for key in data['Business'][i]['attributes']:
            if key in header and (key != 'Good For' or key != 'Parking'):
                attributes[key] = data['Business'][i]['attributes'][key]
        writer.writerow(attributes)