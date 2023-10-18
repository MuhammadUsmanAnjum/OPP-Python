import requests
from bs4 import BeautifulSoup
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://www.whatmobile.com.pk/Price-List-Of-All-5G_Mobile-Phones"
res = requests.get(url=url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
selected_div = soup.find_all("td", height="51" ,align="center", class_="BiggerText")
print(selected_div)

with open("output.csv", 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    for mbl in selected_div:
        link = mbl.a.get("href")
        price = mbl.find("span", class_="PriceFont").text
        name = mbl.find("a", class_="BiggerText").text
        
        csvwriter.writerow([name, price, link])
    


















# score_block = soup.find_all("div", class_="cb-col cb-col-67 cb-scrs-wrp")[0]


# score_elements = score_block.find_all("div", class_="cb-col cb-col-100 cb-min-tm cb-text-gray")
# text = score_elements[0].text
# print(text)
    
# score_elements = score_block.find_all("div", class_="cb-col cb-col-100 cb-min-tm")
# text = score_elements[0].text
# print(text)

# status_line = soup.find("div", "cb-col cb-col-100 cb-min-stts cb-text-complete")
# print(status_line.text)
