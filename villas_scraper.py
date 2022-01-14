import time
import csv

from selenium import webdriver


def go_to_signup_page():
    time.sleep(3)

    myFile = open('villas.csv', 'w')

    with myFile:

        for x in range(1,124):
            villas = driverSigner.find_elements_by_xpath("/html/body/div/div/div/div[1]/main/div[2]/div/ul/li[" + str(x) + "]")
            myData = str((str(villas[0].text)).replace("\n", " "))
            writer = csv.writer(myFile)
            writer.writerow([myData])
            print(myData)

    print("Done!")


driverSigner = webdriver.Firefox(executable_path="./geckodriver")
driverSigner.get(
    "https://www.villas.co.il/region/villas-in-north/1")

go_to_signup_page()
