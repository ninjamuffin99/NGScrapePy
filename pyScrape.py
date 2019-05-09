from urllib.request import urlopen
from bs4 import BeautifulSoup

article = 'NG SHIT'
blamNum = 0
deleteNum = 0
totalLoops = 0

theDate = 'Jan 1'

def scrapeDates(minProj, maxProj):

    global article
    global blamNum
    global deleteNum
    global totalLoops
    global theDate

    article = 'NG SHIT'
    blamNum = 0
    deleteNum = 0
    totalLoops = 0
    for num in range(minProj, maxProj):
        totalLoops += 1
        scrapeProject(num)
    else:
        article = article + "\nBLAMS: " + blamNum.__str__() + "\nDELETES: " + deleteNum.__str__() + "\nTOTAL SUBMISSIONS SCRAPED: " + totalLoops.__str__()
        with open('scraped_text.txt', 'w', encoding='utf-8') as file:
            file.write(article)

def scrapeSimple(minProj, maxProj):

    scrapeProject(minProj)
    date1 = theDate
    scrapeProject(maxProj)
    date2 = theDate
    return date1

def scrapeProject(projID):
    global article
    global blamNum
    global deleteNum
    global totalLoops
    global theDate

    url = "https://www.newgrounds.com/portal/view/" + projID.__str__()

    try:
        page = urlopen(url)
    except:
        print("DELETED")
        deleteNum += 1
        return
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div', {"class": "pod-head"})

    for i in content.findAll('h2'):
        if i.text == "Author Comments":
            article = article + "-------\nBLAMMED\n-------"
            blamNum += 1
            print("BLAMMED")
        else:
            article = article + '\n' + i.text + " " + projID.__str__()
            print(i.text + ' https://www.newgrounds.com/portal/view/' + projID.__str__())

            stats = soup.find('div', {"id":"sidestats"})

            if stats.__str__() == "None":
                print("SOMETHIN BUSTED, SKIPPED")
                continue
            else:
                someVotes = soup.find('span', {"id":"score_number"})
                if (someVotes.__str__() == "None"):
                    article = article +'\nVOTES: UNDER JUDGEMENT???'
                else:
                    article = article + "\nVOTES: " + someVotes.text + "\n"
                    
                someTags = soup.find('dd', {"class":"tags momag"})
                if someTags.__str__() == "None":
                    print("NO TAGS")
                    article = article + '\nTAGS: NONE'
                else:
                    article = article + '\nTAGS: '
                    for tags in someTags.findAll('li'):
                        article = article + tags.text + " "
                article = article + '\n\n'
                
                sideStatsBaby = soup.find('dl', {'class':'sidestats'})
                if (sideStatsBaby.__str__() == "None"):
                    print("Dead date???")
                else:
                    print(sideStatsBaby.findAll("dd"))
                    ##theDate = sideStatsBaby.findAll("dd")[0] + " "
                    ##theDate = theDate + sideStatsBaby.findAll("dd")[1]
                    ##print(sideStatsBaby.findAll('dd'))

                ##for daStats in stats.findAll('dd'):
                ##    article = article + " " + daStats.text  
    