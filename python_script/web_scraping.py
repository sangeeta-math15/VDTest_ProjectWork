import requests
from bs4 import BeautifulSoup

url = 'https://www.cnn.com/'

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('a', href=True)

    for article in articles:
        link = article['href']
        if '/2024/' in link:
            title = article.get_text(strip=True)

            if link.startswith('/'):
                link = 'https://www.cnn.com' + link

            print(f"Title: {title}")
            print(f"URL: {link}")
            print('---')

except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve the page: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
