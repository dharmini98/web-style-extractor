from bs4 import BeautifulSoup
import requests
import time
import re

#need to scrape: color palette, typography, CTA styling (button styling), logo
#voice of webpage


def scrape_web(url):
    html_text = requests.get(url).text
    #print('Below is the html content')
    #print(html_text)
    soup= BeautifulSoup(html_text, 'html.parser')
    #tag_list=['p','h1','h2','h3','h3','h4','h5','h6','span','a','div']
    soup_style=soup.find_all(style=True)
    typography=[]
    #look for color palette, typography and elements
    for i in soup_style:
        style=i.get('style')
        font_family= re.search(r'font-family:\s*([^;]+)',style)
        font_size= re.search(r'font-size:\s*([^;]+)',style)
        font_color=re.search(r'color:\s*([^;]+)',style)

        if font_family or font_size or font_color:
            typography.append({
                'elements':i.name,
                'font_family': font_family.group(1) if font_family else None,
                'font_size': font_size.group(1) if font_size else None,
                'font_color': font_color.group(1) if font_color else None,
            })

    
    
    return typography

url='https://usemadmen.ai'
fetch_data= scrape_web(url)

for i in fetch_data:
    print(i)



