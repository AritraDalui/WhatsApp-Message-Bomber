from selenium import webdriver

driver =  webdriver.Chrome('/home/aritra/Desktop/python/chromedriver')
driver.get("https://web.whatsapp.com/")


print("Login now...\n")

name = input("Enter name:")
count = int(input("Count: "))
msg = input("Message: ")


user = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]'.format(name))
user.click()

msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msgBox.send_keys(msg)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    sendButton.click()


print("Mission Successful")
print(f"{count} messages were sent to {name}")