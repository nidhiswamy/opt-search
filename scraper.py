import requests
from bs4 import BeautifulSoup

def get_company_links(page_url):
    response = requests.get(page_url)
    # print(f"Response = {response.text}")
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Soup = {soup}")
    rows = soup.find_all('tr', {'class': ["even", "odd"]})
    print(f"Rows: {rows}")
    job_openings = []

    for row in rows:
        company_name = row.find('td', class_='views-field-title').text.strip()
        print(f"Company: {company_name}")

        job_link_element = row.find('td', class_='views-field-field-opt-find-jobs-link').find('a', href=True)
        if job_link_element:
            job_link = job_link_element['href']
            job_openings.append({'company_name': company_name, 'job_link': job_link})

    return job_openings

page_url = "https://online.usacareerguides.com/h1b-opt/opt-listing"
opt_links = get_company_links(page_url)

for link in opt_links:
    print(f"\nCompany: {link['company_name']}")
    print(f", Link: {link['job_link']}")
