from bs4 import BeautifulSoup
import requests #let's you download webpages into python
from IPython.display import IFrame

## Using requests library
#url = 'https://www.cnn.com'
url = 'https://www.bbc.com'

# # #Getting the content from the webpages's contents
response = requests.get(url)
print(response)

# Using IFrame to display the webpage
IFrame(url, width="100%", height="400")  

# #Using BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
all_text = soup.find_all('p')
combined_text = ""
for text in all_text:
    combined_text = combined_text + "\n" + text.get_text()
    print(combined_text)