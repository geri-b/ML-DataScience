import requests
from bs4 import BeautifulSoup
import csv

main_url = "https://www.infoplease.com"
page_content = requests.get("https://www.infoplease.com/primary-sources/government/presidential-speeches/state-union-addresses")
soup = BeautifulSoup(page_content.text, 'html.parser')
articles = soup.find_all('span', {'class': 'article'})

urls = []
for i in range(len(articles)):
    title = articles[i].find('a')['href']
    urls.append(main_url + title)

csv_rows = []
invalid_url = []
for url in urls:
    subcontent = requests.get(url)
    soup1 = BeautifulSoup(subcontent.text, 'html.parser')
    #sections = soup1.find_all("div", {"class": "article", "lang": "en"})
    sections = soup1.find_all('article', class_='article')

    if len(sections) > 0:
        president_header = sections[0].find("h2", {"class": "title"})

        if president_header is None:
            president_header = sections[0].find('h1', class_='page-title')

        if president_header is not None:

            president = president_header.text.split("(")[0]
            date = president_header.text.split("(")[1][0:-1]
            paragraphs = sections[0].find_all("p")
            text = ""
            for i in range(3):
                p_text = paragraphs[i].text
                text += p_text
            row = {"President": president, "Date": date, "Link": url, "Speech": text}
            csv_rows.append(row)
        else:
            invalid_url.append(url)
    else:
        invalid_url.append(url)

with open('bigdata.csv', 'w', newline="") as data_dump:
    header = ['President', 'Date', 'Link', 'Speech']
    writer = csv.DictWriter(data_dump, fieldnames=header)
    writer.writeheader()
    writer.writerows(csv_rows)

for inv_url in invalid_url:
    print(inv_url)