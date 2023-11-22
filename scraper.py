import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

def get_company_links(page_url):
    response = requests.get(page_url)
    # print(f"Response = {response.text}")
    job_openings = []
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(f"Soup = {soup}")
        rows = soup.find_all('tr')
                             # , {'class': ["even", "odd", "views-row-first"]})
        # rows empty
        print(f"Rows: {rows}")

        for row in rows:
            company_name = row.find('td', class_='views-field-title').text.strip()
            print(f"Company: {company_name}")

            job_link_element = row.find('td', class_='views-field-field-opt-find-jobs-link').find('a', href=True)
            if job_link_element:
                job_link = job_link_element['href']
                job_openings.append({'company_name': company_name, 'job_link': job_link})

    else:
        print("Failed to open page")

    return job_openings

# Loading secure values from dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL")
PWD = os.getenv("PASSWORD")

login_url = "https://online.usacareerguides.com/user/login"

# Session to persist login cookies
session = requests.Session()

# Login with secure values
login_payload = {'EMAIL': EMAIL, 'PASSWORD': PWD}
login_response = session.post(login_url, data=login_payload)

opt_links = []

if login_response.ok:
    print("Login successful")

    page_url = "https://online.usacareerguides.com/h1b-opt/opt-listing"
    opt_links = get_company_links(page_url)

else:
    print("Login failed")

for link in opt_links:
    print(f"\nCompany: {link['company_name']}, ")
    print(f"Link: {link['job_link']}")
