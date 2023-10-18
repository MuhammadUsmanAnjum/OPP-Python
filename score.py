import requests
from bs4 import BeautifulSoup
url = f"https://www.cricbuzz.com/live-cricket-scores/75490/nz-vs-afg-16th-match-icc-cricket-world-cup-2023"


res = requests.get(url=url)


soup = BeautifulSoup(res.content, 'html.parser')


match_report = soup.find_all("div", class_="cb-col cb-col-67 cb-nws-lft-col cb-comm-pg")[0]
print(match_report)
first_score = match_report.find("div", "cb-text-gray cb-font-16")
second_score = match_report.find("span", "cb-font-20 text-bold")
match_progress = match_report.find("div", class_="cb-text-inprogress")
# players = match_report.find_all("div", class_="cb-col cb-col-50")
# batter1 = match_report.find_all("div", class_="cb-col cb-col-50")[1]
# batter2 = match_report.find_all("div", class_="cb-col cb-col-50")[2]

overs_progress = match_report.find("div", class_="cb-col cb-col-100 cb-font-12 cb-text-gray cb-min-rcnt")
print(overs_progress)

# print(players)
# print(batter1.find("a").text)
# print(batter2.a.text)
print(first_score)
print(second_score)
print(match_progress)

