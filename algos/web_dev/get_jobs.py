import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_jobs(job_type, location):
    job_in_url = job_type.lower().split(' ')
    job_list = "+".join(job_in_url)
    url = "https://www.indeed.com/jobs?q="
    joiner = "&l="
    soup = BeautifulSoup(requests.get(url + job_list + joiner + location).content, "html.parser")
    for job in soup.find_all("div", attrs={"data-tn-component": "organicJob"}):
        job_anchor = job.find("a", attrs={"class": "turnstileLink"})
        job_title = job_anchor.text.strip()
        job_link = urljoin(url,job_anchor.get("href"))
        easy_apply = False
        easy_apply_tag = job.find("span", attrs={"class": "iaLabel iaIconActive"})
        company_name = job.find("span", {"class": "company"}).text.strip()
        if easy_apply_tag:
            easy_apply = True
        yield job_title, company_name, job_link, easy_apply

job_type = input('Enter job title: ')
zip_code = input("Zip Code: ")
for i, job in enumerate(fetch_jobs(job_type, zip_code), 1):
    print(f"================== Job{i:>4} ===================")
    print("----------------------------------------------")
    print(f"{job[0]} at {job[1]}.\nLink :{job[2]} \nEasy apply? {job[3]}")
    print("----------------------------------------------")
    print("==============================================")