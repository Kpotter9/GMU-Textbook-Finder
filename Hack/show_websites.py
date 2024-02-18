from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys

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



