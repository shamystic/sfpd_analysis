from bs4 import BeautifulSoup
import urllib
import requests 

# Load page with request module 
r = requests.get('http://zipatlas.com/us/ca/san-francisco/zip-code-comparison/median-household-income.htm')
# Convert to bs4 object 
c = r.content
soup = BeautifulSoup(c, "lxml")
# Scrape contents 
data = soup.find_all('td', {"class": "report_data"})
txts = [x.text for x in data]
zipcodes = [x for x in txts if x[:3] == '941'] # Zipcodes start with '941'
incomes = [int(x[1:-3].replace(',', '')) for x in txts if  x[0] == '$'] # Incomes 

# Populations are trickier - have a comma, and can be converted to ints, unlike others. We can make use of exceptions to filter them: 
populations = []
for x in txts: 
	if x not in zipcodes:  
		try: populations.append(int(x.replace(',', '')))
		except: continue 

dict_income = {int(k) : v for k, v in zip(zipcodes, incomes)}
dict_population = {int(k) : v for k, v in zip(zipcodes, populations)}
print ('Income =', dict_income)
print ('Population =', dict_population)
print ('Dictionaries the same size? {}'.format(len(dict_population) == len(dict_income)))