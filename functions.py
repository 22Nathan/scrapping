import requests
from bs4 import BeautifulSoup

def scraping_bdm(url:str='https://www.blogdumoderateur.com/') -> dict:
    
    response_bdm = requests.get(url)
    soup_bdm = BeautifulSoup(response_bdm.text)
    not_found = soup_bdm.find(string="Désolé, mais rien ne correspond à vos termes de recherche. Veuillez réessayer avec d'autres mots-clés.")
    articles = soup_bdm.find_all('article')

    data = {}
    if not_found or not articles:
        return data

    for artilce in articles:
        
        try:image_link = artilce.find('img')['data-lazy-src']
        except:image_link = None
        
        title = artilce.h3.text

        try:link = artilce.find('a')['href']
        except:link = artilce.parent['href']

        try:time = artilce.time['datetime'].split('T')[0] 
        except:time = None
       
        try:label = artilce.find('span', 'favtag color-b').text
        except:
            try:label = artilce.parent.parent.parent.parent.h2.text
            except:label = None

        data[artilce['id']] = {
            'title' : title,
            'image' : image_link,
            'link'  : link,
            'label':  label,
            'time'  : time
        }
    return data