from bs4 import BeautifulSoup
import pandas as pd
from  selenium import webdriver
import re

driver=webdriver.Chrome(executable_path="C:/Users/Klaus/Downloads/software/chromedriver/chromedriver.exe")
driver.get("https://www.walmart.com/search?q=gym%20equipment&typeahead=gym")


item_rating_results=[]
item_title_results=[]
item_price_results=[]

content= driver.page_source
soup=BeautifulSoup(content,features='html.parser')
driver.quit()

for a in soup.find_all(attrs='h-100 pb1-xl pr4-xl pv1 ph1'):
    title=a.find('a')
    if title not in item_title_results:
        item_title_results.append(title.text)


for b in soup.find_all(attrs='flex flex-wrap justify-start items-center lh-title mb2 mb1-m'):
    price=b.find('div', attrs={"class": 'b black f5 mr1 mr2-xl lh-copy f4-l'})
    final_price =  b.getText()

    if final_price not in item_price_results:
        item_price_results.append(final_price)


for c in soup.find_all(attrs='mt2 flex items-center'):
    rating=c.find('span', attr={"class": 'sans-serif gray f7'})
    final_rating=c.getText()
    
    if final_rating not in item_rating_results:
        item_rating_results.append(final_rating)




k={'Rating':item_rating_results, 'Product':item_price_results, 'ProductTitle':item_title_results}
df = pd.DataFrame.from_dict(k, orient= 'index')
df.transpose()
df.to_csv('Walmartproductsurvey.csv', index=False, encoding='utf-8',header=True)


