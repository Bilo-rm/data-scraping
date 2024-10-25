import requests
from bs4 import BeautifulSoup

# Base URL and initial page URL
base_url = "https://islamqa.info"
initial_page_url = f"{base_url}/en/latest"

def get_question_links(page_url):
    try:
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Collect all question links on the current page
        question_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if "/en/answers/" in href:
                # Check if the link is relative or absolute
                full_link = base_url + href if href.startswith("/") else href
                question_links.append(full_link)

        return question_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

def get_all_question_links(limit):
    all_links = []
    current_page = 1
    while current_page <= limit: # instead of while true and fetching all the data, i will limit it to 5 pages
        # Construct URL for the current page
        page_url = f"{initial_page_url}?page={current_page}"
        print(f"Fetching page {current_page}...")

        # Get question links on the current page
        links = get_question_links(page_url)
        
        # Stop if no more links are found (last page)
        if not links:
            break
        
        all_links.extend(links)
        current_page += 1  # Move to the next page
    
    print(f"Total questions found: {len(all_links)}")
    return all_links
"""
# Fetch and print all question links across multiple pages
all_question_links = get_all_question_links()

# Print all the collected question links
for link in all_question_links:
    print(link)
"""