from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
import requests
from bs4 import BeautifulSoup

# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')
Mytitle=''
i=1
while(sys.argv[i]!="#@"):
    Mytitle+=sys.argv[i]
    if(sys.argv[i+1]!="#@"):
         Mytitle+=" "
   
    i+=1
i+=1
while(sys.argv[i]!="#@"):   
    i+=1
myISBN=int(sys.argv[i+1])

driver = webdriver.Chrome(
    
    options=options, 
    # other properties...
)
Mytitle.split
Link='https://www.abebooks.com/servlet/SearchResults?kn='+Mytitle.replace(" ","%20").replace("(","%28").replace(")","%29")+'&sts=t&cm_sp=SearchF-_-topnav-_-Results'
if(myISBN<1000000000):

    driver.get('https://www.abebooks.com/servlet/SearchResults?kn='+Mytitle.replace(" ","%20").replace("(","%28").replace(")","%29")+'&sts=t&cm_sp=SearchF-_-topnav-_-Results')
else: 
    driver.get('https://www.abebooks.com/servlet/SearchResults?bi=0&bx=off&cm_sp=SearchF-_-Advs-_-Result&ds=30&isbn='+myISBN+'&recentlyadded=all&rollup=on&sortby=17&sts=t&tn='+Mytitle.replace(" ","%20").replace("(","%28").replace(")","%29")+'&xdesc=off&xpod=off')
books=[]
check=99999.99
hold=[0,0,0]
books=driver.find_elements(By.XPATH ,"//div//ul/li")
for book in books:
    
    title=book.find_elements(By.CLASS_NAME, "title")
    price=book.find_elements(By.CLASS_NAME, "item-price")
    isbn=book.find_elements(By.XPATH,"//p/a/span")
    for i in range(len(title)):
        if(title[i].text==Mytitle or int(isbn[i].text[9:])==myISBN):
            
            if(float(price[i].text[3:])<float(check)):
                hold[0]=title[i].text
                hold[1]=price[i].text
                hold[2]=isbn[i].text
                check=price[i].text[3:]
if(hold[0]!=0):
    print(hold[0],hold[1],hold[2])
    print(Link)
driver.quit()




############################


def get_title(soup):
	
	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

		# Inner NavigatableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip()

		# # Printing types of values for efficient understanding
		# print(type(title))
		# print(type(title_value))
		# print(type(title_string))
		# print()

	except AttributeError:
		title_string = ""	

	return title_string

# Function to extract Product Price
def get_price(soup):

	try:
		price = soup.find("span", attrs={'class':'a-price'}).find("span").string.strip()

	except AttributeError:

		try:
			# If there is some deal price
			price = soup.find("span", attrs={'class':'class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"'}).string.strip()

		except:		
			price = "No Price Found"	

	return price


def get_ISBN(soup):
		try:
			webpageISBN = soup.find("div", attrs={'id':'rpi-attribute-book_details-isbn10'})
			webpageISBN = webpageISBN.find("div", attrs={'class':'a-section a-spacing-none a-text-center rpi-attribute-value'})
			webpageISBN = webpageISBN.find("span").string.strip()
		except AttributeError:
			webpageISBN = "ISBN Not Available"
		return webpageISBN


	# Headers for request
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US'})
	# The webpage URL

if (myISBN == 0 or myISBN < 999999999):
    amaURL = Mytitle.replace(" ", "+")
    amaURL = "https://www.amazon.com/s?k=" + amaURL + "&ref=nav_bb_sb"
else:
	amaURL = "https://www.amazon.com/s?k=" + str(myISBN) + "&ref=nav_bb_sb"
	

# HTTP Request
webpage = requests.get(amaURL, headers=HEADERS)
	# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "lxml")
	# Fetch links as List of Tag Objects
links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

	# Store the links
links_list = []

	# Loop for extracting links from Tag Objects

if(len(links) > 5):
	for i in range(4):
		links_list.append(links[i].get('href'))
else:
	for i in links:
		links_list.append(i.get('href'))
	

ISBN_list = []
title_list = []
price_list = []
final_link_list = []
	# Loop for extracting product details from each link 
for i in range(len(links_list)):

	new_webpage = requests.get("https://www.amazon.com" + links_list[i], headers=HEADERS)

	new_soup = BeautifulSoup(new_webpage.content, "lxml")
	
	link = ("https://www.amazon.com" + links_list[i])
	ISBN_list.append(get_ISBN(new_soup))
	title_list.append(get_title(new_soup))
	price_list.append(get_price(new_soup))
	final_link_list.append(link)


count = 0
#checks the ISBN of the results and displays them
if(myISBN != 0 or myISBN < 999999999):
	for p in range(len(ISBN_list)):
		if(ISBN_list[p] == myISBN):
			print("\n" + title_list[p])
			print(price_list[p])
			print(ISBN_list[p])
			print(final_link_list[p])
			count += 1
		elif(title_list[p] == Mytitle):
			print("\n" + title_list[p])
			print(price_list[p])
			print(ISBN_list[p])
			print(final_link_list[p])
			count += 1

if (count == 0):
    for q in range(len(title_list)):
        print("\n" + title_list[q])
        print(price_list[q])
        print(ISBN_list[q])
        print(final_link_list[q])
