from urllib.request import urlopen
from bs4 import BeautifulSoup

article = 'NG SHIT'
blamNum = 0
deleteNum = 0
eRated = 0
tRated = 0
mRated = 0
aRated = 0


totalLoops = 0

theDate = 'Jan 1'

def scrapeDates(minProj, maxProj):

    global article
    global blamNum
    global deleteNum
    global eRated
    global tRated
    global mRated
    global aRated
    global totalLoops
    global theDate

    article = 'NG SHIT'
    blamNum = 0
    deleteNum = 0
    eRated = 0
    tRated = 0
    mRated = 0
    aRated = 0
    totalLoops = 0
    for num in range(minProj, maxProj):
        totalLoops += 1
        scrapeProject(num)
    else:
        article = article + "\nE RATED: " + eRated.__str__() + "\nT RATED: " + tRated.__str__() + "\nM RATED: " + mRated.__str__() + "\nA RATED: " + aRated.__str__()
        article = article + "\n\nBLAMS: " + blamNum.__str__() + "\nDELETES: " + deleteNum.__str__() + "\nTOTAL SUBMISSIONS SCRAPED: " + totalLoops.__str__()
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
    global eRated
    global tRated
    global mRated
    global aRated
    global totalLoops
    global theDate

    url = "https://www.newgrounds.com/portal/view/" + projID.__str__()

    try:
        page = urlopen(url)
    except:
        print("DELETED " + url)
        deleteNum += 1
        return
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div', {"class": "pod-head"})

    for i in content.findAll('h2'):
        if i.text == "Author Comments":
            article = article + "-------\nBLAMMED\n-------"
            blamNum += 1
            print("BLAMMED " + url)
        else:
            article = article + '\n' + i.text + " " + url
            print(i.text + " " + url)

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
                
                ##DATE AND TIME
                sideStatsBaby = soup.find_all('dl', {'class':'sidestats'})
                if (sideStatsBaby.__str__() == "None"):
                    print("Dead date???")
                else:
                    print("whatever")
                    rowShit = 0
                    for row in sideStatsBaby:
                        if (rowShit > 0):
                            moreRow = row.find_all('dd')
                            print(moreRow)
                            print("CLEANED SHIT")
                            str_cells = str(moreRow)
                            cleaned = BeautifulSoup(str_cells, 'html.parser').get_text()
                            cleaned = cleaned[1:]
                            cleaned = cleaned[:-1]
                            cleanedArray = cleaned.split(',')

                            article = article + "Posted: " + cleanedArray.__str__()

                            print(cleanedArray[0] + cleanedArray[2])
                        rowShit += 1
                
                article = article + '\n'
                ratingShit = soup.find_all('div', {'id': 'embed_header'})
                for shit in ratingShit:
                    moreShit = shit.find_all('h2')
                    theRating = moreShit.__str__()[18]
                    article = article + "RATING: " + theRating

                    if (theRating == 'e'):
                        eRated += 1
                    if (theRating == 't'):
                        tRated += 1
                    if (theRating == 'm'):
                        mRated += 1
                    if (theRating == 'a'):
                        aRated += 1

                    print("RATED: " + moreShit.__str__()[18])
                