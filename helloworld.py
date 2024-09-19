#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
driver = webdriver.Firefox()   



#Functions
def OpenWebPage(URL): driver.get(URL)

def QuitWebPage(): driver.quit()

def Login(Username, Password):
    #Intialise Elements
    UsernameInput = driver.find_element(By.ID, "session_key")
    PasswordInput = driver.find_element(By.ID, "session_password")

    #Input Text and Click "Sign In"
    time.sleep(random.randint(1, 8)) #sleep to not spam the sysytem
    UsernameInput.send_keys(Username)
    time.sleep(random.randint(1, 8))
    PasswordInput.send_keys(Password)
    time.sleep(random.randint(1, 8))
    PasswordInput.send_keys(Keys.RETURN)
    
def Search(SearchTerm):
    time.sleep(random.randint(1, 8)) #sleep to not spam the system
    #Intialise Elements
    SearchBar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")

    #Do Actions
    SearchBar.send_keys(SearchTerm)
    time.sleep(random.randint(1, 8))
    SearchBar.send_keys(Keys.RETURN)

def ClickOnTabNavbar(TabToSelect):
    time.sleep(random.randint(5, 15)) #sleep to not spam the system 
     #Intialise Elements\
    TopNavBar = driver.find_elements(By.CLASS_NAME, "global-nav__primary-link")
    
    #Store Default Vars
    TabsAvailable = ["Home", "My Network", "Jobs", "Messaging", "Notifications"]
    print(TabsAvailable.index(TabToSelect))
    MyNetworkButton = TopNavBar[TabsAvailable.index(TabToSelect)]

    #Do Actions
    time.sleep(random.randint(1, 8))#sleep to not spam the sysytem
    MyNetworkButton.click()

def FollowPeople(AmountOfPeopleToFollow):
    time.sleep(random.randint(5, 15)) #sleep to not spam the system 
    #Intialise Elements\
    AllAvailablePeople = driver.find_elements(By.CLASS_NAME, "discover-entity-type-card__container-bottom")

    #Store Default Vars
    for i in range(AmountOfPeopleToFollow):
        PersonToFollow = AllAvailablePeople[i]
        FollowButton = PersonToFollow.find_element(By.CLASS_NAME, "artdeco-button")

        #Do Actions
        time.sleep(random.randint(1, 4))#sleep to not spam the sysytem
        FollowButton.click()    

#Set Some Defaults
URL = "https://www.linkedin.com/" 
Username = "REDACTED@gmail.com"
Password = "REDACTED"
SearchTerm = "#Software"

#Main  
OpenWebPage(URL)    
time.sleep(random.randint(1, 8))
Login(Username, Password)
ClickOnTabNavbar("My Network")
FollowPeople(8)
#Search(SearchTerm)
QuitWebPage()

