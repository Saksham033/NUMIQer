import requests
from bs4 import BeautifulSoup
import pandas as pd
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

url = "https://economictimes.indiatimes.com/wealth/insure/life-insurance/latest-life-insurance-claim-settlement-ratio-of-insurance-companies-in-india/articleshow/97366610.cms"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) >= 6:
        company = cells[0].text.strip()
        claim_settlement_percentage = cells[5].text.strip().replace('%', '')
        data.append([company, claim_settlement_percentage])

df = pd.DataFrame(data, columns=['Company', 'Claim Settlement Percentage'])
df.to_csv('claim_settlement_percentage.csv', index=False)

with open('claim_settlement_percentage.csv', 'rb') as file:
    file_data = file.read()
encrypted_data = fernet.encrypt(file_data)
with open('claim_settlement_percentage_encrypted.csv', 'wb') as file:
    file.write(encrypted_data)