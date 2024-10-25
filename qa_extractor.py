import requests
from bs4 import BeautifulSoup

def get_question_and_answer(question_url):
    try:
        response = requests.get(question_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        question_section = soup.find('section', class_='single_fatwa__question')
        answer_section = soup.find('section', class_='single_fatwa__answer__body')
        
        question_text = ""
        if question_section:
            question_paragraphs = question_section.find_all('p')
            question_text = "\n".join(p.get_text(strip=True) for p in question_paragraphs)

        answer_text = ""
        if answer_section:
            answer_paragraphs = answer_section.find_all('p')
            answer_text = "\n".join(p.get_text(strip=True) for p in answer_paragraphs)
        
        return question_text, answer_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching question page: {e}")
        return None, None
