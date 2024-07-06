import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def scrape_data(request):
    # URL of the webpage to scrape
    url = 'https://pandas.pydata.org/docs/user_guide/style.html'

    # Send a request to fetch the content of the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract data (example: extracting a table)
    table = soup.find('table')
    rows = table.find_all('tr')

    # Extracting headers and rows
    headers = [header.text for header in rows[0].find_all('th')]
    data = []
    for row in rows[1:]:
        cells = row.find_all('td')
        data.append([cell.text for cell in cells])

    # Render the data to the template
    return render(request, 'scraper/table.html', {'headers': headers, 'data': data})

