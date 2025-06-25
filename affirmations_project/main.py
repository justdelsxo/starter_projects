import requests
from config import API_BASE_URL

def get_daily_affirmation():
    headers = {'Content-Type': 'application/json'}
    response = requests.get(f'{API_BASE_URL}/affirmations', headers=headers)
    if response.ok:
        return response.json()
    else:
        return {"error": f"Failed to get affirmation: {response.status_code}"}

def add_affirmation(affirmation, author, category):
    payload = {
        'text': affirmation,
        'author': author,
        'category': category
    }
    response = requests.post(f'{API_BASE_URL}/new_affirmation', json=payload)
    if response.ok:
        return response.json()
    else:
        return {"error": f"Failed to add affirmation: {response.status_code}","details": response.text}


def run():
    print("###############################")
    print("Fetching a daily affirmation...")
    print("###############################")
    print(get_daily_affirmation())

    print("\nLet's add a new affirmation!")
    text = input("Enter affirmation text: ").strip()
    author = input("Enter your name: ").strip()
    category = input("Enter category e.g Motivation, Self-Love, Gratitude etc: ").strip()

    if text and author and category:
        response = add_affirmation(text, author, category)
        print(response)
    else:
        print("Missing input(s). Affirmation not added.")

if __name__ == '__main__':
    run()
