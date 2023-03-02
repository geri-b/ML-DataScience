import json
import csv

with open("business100ValidForm.json") as file:
    json_string = file.read()

data = json.loads(json_string)

header = ['ID', 'Name', 'Open', 'Stars', 'Review Count', 'Address', 'City', 'Neighborhoods','State', 'Longitude', 'Latitude',
              'Type', 'Category']
with open('mainInfo.csv', 'w', newline="") as data_dump:
    writer = csv.DictWriter(data_dump, fieldnames=header)
    writer.writeheader()

    for i in range(100):
         row = \
         {
             "ID" : data['Business'][i]['business_id'],
             "Name": data['Business'][i]['name'],
             "Open": data['Business'][i]['open'],
             "Address" : data['Business'][i]['full_address'],
             "City" : data['Business'][i]['city'],
             "State": data['Business'][i]['state'],
             "Stars": data['Business'][i]['stars'],
             "Review Count": data['Business'][i]['review_count'],
             "Longitude" : data['Business'][i]['longitude'],
             "Latitude" : data['Business'][i]['latitude'],
             "Type" : data['Business'][i]['type'],
             "Category" : data['Business'][i]['categories'],
             "Neighborhoods": data['Business'][i]['neighborhoods']
         }
         #Adjusting the Address and Category Values
         row['Address'] = row['Address'].replace('\n', ' ').replace(',', '')
         row['Category'] = ' & '.join(row['Category'])
         row['Neighborhoods'] = ' & '.join(row['Neighborhoods'])
         writer.writerow(row)