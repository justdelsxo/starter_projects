from dotenv import load_dotenv
import os, requests

load_dotenv()

API_URL = os.getenv("API_URL")


categories = {
    'self love': 'self-love',
    'motivation': 'motivation',
    'gratitude': 'gratitude',
    'confidence': 'confidence',
    'success': 'success',
    'healing': 'healing',
    'abundance': 'abundance',
    'mental health': 'mental-health',
    'relationships': 'relationships',
    'spirituality': 'spirituality',
    'peace': 'peace',
    'growth': 'growth',
    'resilience': 'resilience',
    'forgiveness': 'forgiveness',
    'positivity': 'positivity'
}

def get_daily_affirmation():
    headers = {'Content-Type': 'application/json'}
    response = requests.get(f'{API_URL}/affirmations', headers=headers)
    if response.ok:
        return response.json()
    else:
        return {"error": f"Failed to get affirmation: {response.status_code}"}

def add_affirmation(affirmation, author, category):
    headers = {'Content-Type': 'application/json'}
    affirmation_data = {
        'text': affirmation,
        'author': author,
        'category': category
    }
    response = requests.post(f'{API_URL}/new_affirmation', headers=headers, json=affirmation_data)
    if response.ok:
        return response.json()
    else:
        return {"error": f"Failed to add affirmation: {response.status_code}","details": response.text}

def get_affirmations_by_category(category):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(f'{API_URL}/affirmations/category/{category}', headers=headers)
    if response.ok:
        return response.json()
    else:
        return {"error": f"Failed to find category: {response.status_code}"}

def run():
    while True:
        print("\n###############################")
        print("    The Positive Vibes Hub  ")
        print("###############################")
        print("1. Get your daily affirmation")
        print("2. Add a new affirmation")
        print("3. View affirmations by category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            print("\nFetching your daily affirmation...")
            print("---------------------------------")
            print(get_daily_affirmation())

        elif choice == '2':
            print("\nAdd a New Affirmation")
            print("----------------------")
            text = input("Enter affirmation text: ").strip().lower().capitalize()
            author = input("Enter your name: ").strip().lower().title()
            print("----------------------")
            print("Available categories:")
            print("----------------------")
            print(", ".join(categories.values()))
            print("-----------------------------------------------------")
            category = input("Choose which category this affirmation belongs to: ").strip().lower().replace(" ", "-")

            if text and author and category:
                response = add_affirmation(text, author, category)
                print(response)
            else:
                print("❌ Missing input(s). Affirmation not added. Please try again")

        elif choice == '3':
            print("\nView Affirmations by Category")
            print("------------------------------")
            print("Available categories:")
            print(", ".join(categories.values()))
            print("------------------------------")
            by_category = input("Enter a category: ").strip().lower().replace(' ', '-')

            if by_category in categories.values():
                results = get_affirmations_by_category(by_category)
                print(results)

            else:
                print("❌ Invalid category. Please choose a category from the list above.")

        elif choice == '4':
            print("Thank you for using the Affirmation App! Stay positive! :)")
            break
        else:
            print("❌ Invalid option. Please select 1, 2, 3 or 4.")

if __name__ == '__main__':
    run()
