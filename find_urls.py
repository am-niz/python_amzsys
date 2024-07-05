import requests
import re

def get_linked_urls(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Use regex to find all URLs in the HTML content
        urls = re.findall(r'href=["\'](https?://[^"\'>]+)', response.text)

        return set(urls)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return set()

# Example usage:
if __name__ == "__main__":
    url = "https://anandology.com/python-practice-book/modules.html"  # Replace with your desired URL
    linked_urls = get_linked_urls(url)
    for linked_url in linked_urls:
        print(linked_url)
