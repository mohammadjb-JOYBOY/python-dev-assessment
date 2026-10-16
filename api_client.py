import requests


def fetch_and_display_users(num_users):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()

        for user in response.json()[:num_users]:
            print(
                f"Name: {user['name']}\nEmail: {user['email']}\nCity: {user['address']['city']}\n---"
            )

    except Exception as e:
        print(f"Error: {e}")


fetch_and_display_users(5)