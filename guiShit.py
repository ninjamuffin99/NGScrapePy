from appJar import gui
import pyScrape

app = gui("Newgrounds Scraper 2000", "960x540")
app.addLabel("title", "Newgrounds Scraper 2000 by ninjamuffin99")
app.addNumericLabelEntry("Min Project Num")
app.addNumericLabelEntry("Max Project Num")


def press(button):
    if button == "Exit":
        app.stop()
    else:
        
        usr = app.getEntry("Min Project Num")
        pwd = app.getEntry("Max Project Num")
        print("User: ", usr.__int__(), "Pass: ", pwd.__int__())
        pyScrape.scrapeDates(usr.__int__(), pwd.__int__())

def checkDate(button):
    usr = app.getEntry("Min Project Num")
    pwd = app.getEntry("Max Project Num")
    print(pyScrape.scrapeSimple(usr.__int__(), pwd.__int__()))

app.addButton("Check Dates", checkDate)
app.addButtons(["Submit", "Exit"], press)
app.addAppJarMenu()

app.go()