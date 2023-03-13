import requests
from bs4 import BeautifulSoup

url = 'https://www.fuzu.com/kenya'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'lxml')
jobs = soup.find_all('a', class_="Card__StyledDiv-sc-uckied-0 kUaCWW b2c-card clickable")

for job in jobs:
    company_name = job.find('p', class_="Text__StyledText-sc-152w2ki-0 MDWeZ b2c-text").text
    job_name = job.find('h6', class_="Title__StyledTitle-sc-5s9ddm-0 cvLYDq title").text
    location = job.find('p', class_="Text__StyledText-sc-152w2ki-0 ckLUZM b2c-text").text
    time = job.find('div', class_="styled__StyledPositionDetails-sc-1vpj8uj-0 jlFoVM").text

    print(f"Company Name: {company_name}")
    print(f"Job Title: {job_name}")
    print(f"Location: {location}")
    print(f"Time: {time}")
    print()



