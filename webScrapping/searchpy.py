import requests
from bs4 import BeautifulSoup
import webbrowser, sys, pyperclip
try:
    if len(sys.argv) > 1:
        # Get address from command line.
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard.
        address = pyperclip.paste()
    words=address.split(' ')
    address = ''
    for w in words:
        address+=w+'+'
    address=address[:len(address)-1]
    print('https://www.bing.com/search?q=' + address)
    page = requests.get('https://www.bing.com/search?q=' + address)
    # Parsing the HTML

    soup = BeautifulSoup(page.content, 'html.parser')
    soup.prettify()
    print(soup.main)
    code = soup.main.find_all('a')
    print(code)
    listOfLinks = []
    print(code)
    for link in code:
        listOfLinks.append(link['href'])
        print(link['href'])
    print("here")
    for link in listOfLinks:
        webbrowser.open(link)
    print(listOfLinks)
except Exception as exc:
    print('There was a problem: %s' % (exc))

    
