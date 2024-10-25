from q_links_extractor import get_all_question_links
from qa_extractor import get_question_and_answer

def main():
    # Get question links
    question_links = get_all_question_links(limit=1)

    # Extract and print questions and answers
    for link in question_links:
        question, answer = get_question_and_answer(link)
        print(f"Question: {question}\nAnswer: {answer}\n")
        print("\n\n")

if __name__ == "__main__":
    main()
