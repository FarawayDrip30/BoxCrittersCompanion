from selenium import webdriver
from pypresence import Presence
import time
from tkinter import *

"""
#UI
master = Tk()

def callback():
    print("click!")

chromeimg = PhotoImage(file="Assets/Images/chrome.png")
chromebutton = Button(master, image=chromeimg, command=callback, height=50, width=50)
chromebutton.pack()

mainloop()
"""

#Get Browser & Login
osquestion = input("Type your Operating System ")
if(osquestion != "$"):
    browserquestion = input("Type your Browser ")

    if browserquestion.lower() == "chrome":
        browser_path = 'Assets/WebDrivers/' + osquestion.lower() + '/chromedriver.exe'
        browser = webdriver.Chrome(browser_path)
    elif browserquestion.lower() == "edge":
        browser_path = 'Assets/WebDrivers/' + osquestion.lower() + '/msedgedriver.exe'
        browser = webdriver.Edge(browser_path)
    elif browserquestion.lower() == "firefox":
        browser_path = 'Assets/WebDrivers/' + osquestion.lower() + '/geckodriver.exe'
        browser = webdriver.Firefox(browser_path)
else:
    browser_path = 'Assets/WebDrivers/windows/chromedriver.exe'
    browser = webdriver.Chrome(browser_path)

browser.get("https://boxcritters.com/")

login_username = browser.find_element_by_id('username')
login_username.send_keys("<ENTER YOUR BOX CRITTERS EMAIL HERE>")

login_password = browser.find_element_by_id('password')
login_password.send_keys("<ENTER YOUR BOX CRITTERS PASSWORD HERE>")

login_button = browser.find_element_by_id('loginButton')
login_button.click()

console = browser.get_log('browser')
print(console)

#Main
def Main():
    #Discord Presence Stuff
    client_id = "833288037664030720"
    RPC = Presence(client_id)
    RPC.connect()
    print(RPC.update(state="Test", details="In the Port"))
    #Main Loop
    while(True):
        time.sleep(15)
        print(console)

#Checks for if the Player is in the game
def waitUntilPlaying():
    while(True):
        if(browser.current_url == "https://boxcritters.com/play/index.html"):
            print("gottem")
            Main()
            return

waitUntilPlaying()
