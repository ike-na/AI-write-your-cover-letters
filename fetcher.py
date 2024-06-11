import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://duunitori.fi/tyopaikat?alue=Uusimaa%3BUusimaa&haku=teollisuus+ja+teknologia+%28ala%29%3BHarjoittelija"

def fetch_job_listings(soup):
    jobs = soup.find_all('a', {'class': 'job-box__hover gtm-search-result'})
    job_data = []
    
    for job in jobs:
        job_info = {}
        job_info['title'] = job.text.strip()
        job_info['company'] = job.get('data-company', 'N/A')
        job_info['category'] = job.get('data-category', 'N/A')
        job_info['url'] = "https://duunitori.fi" + job['href']
        job_data.append(job_info)
    
    return job_data

def fetch_job_details(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            job_soup = BeautifulSoup(response.content, 'html.parser')
            
            h1_tag = job_soup.find('h1', {'class': 'text--break-word'})
            title = h1_tag.text.strip() if h1_tag else "No title found"
            
            div_tag = job_soup.find('div', {'class': 'gtm-apply-clicks description description--jobentry'})
            description = div_tag.get_text(separator=' ').strip() if div_tag else "No description found"
            
            return title, description
        else:
            return "Failed to load job page", "Failed to load job page"
    except Exception as e:
        return f"Error: {str(e)}", f"Error: {str(e)}"

def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('duunitori_jobs.xlsx', index=False)

def main():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {URL}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    job_listings = fetch_job_listings(soup)

    if job_listings:
        print("Job listings fetched successfully!")
        for job in job_listings:
            title, description = fetch_job_details(job['url'])
            job['detail_title'] = title
            job['description'] = description
        
        save_to_excel(job_listings)
        print("Job listings saved to 'duunitori_jobs.xlsx'")
    else:
        print("No job listings fetched!")

if __name__ == "__main__":
    main()
