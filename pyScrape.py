from urllib.request import urlopen
from bs4 import BeautifulSoup
article = 'NG SHIT'
blamNum = 0
deleteNum = 0
for num in range(730000, 730905):
    url = "https://www.newgrounds.com/portal/view/" + num.__str__()
    try:
        page = urlopen(url)
    except:
        print("DELETED")
        deleteNum += 1
        continue
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div', {"class": "pod-head"})

    for i in content.findAll('h2'):
        if i.text == "Author Comments":
            article = article + "\n" + "BLAMMED"
            blamNum += 1
            print("BLAMMED")
        else:
            article = article + '\n' + i.text + " " + num.__str__()
            print(i.text + ' https://www.newgrounds.com/portal/view/' + num.__str__())
else:
    article = article + "\nBLAMS: " + blamNum.__str__() + "\nDELETES: " + deleteNum.__str__()
    with open('scraped_text.txt', 'w', encoding='utf-8') as file:
        file.write(article)