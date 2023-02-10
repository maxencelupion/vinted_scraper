import pickle
import time
import mysql.connector
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("MySQL Password : "),
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS vinted;")
mycursor.execute("USE vinted;")
mycursor.execute("CREATE TABLE IF NOT EXISTS product (price VARCHAR(10), product_id VARCHAR(500) PRIMARY KEY);")
options = Options()
options.headless = True
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))

try:
    value=int(input("How much time we scrape ? "))
except ValueError:
    print("This is not a whole number.")

for u in range(value):
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
        driver.set_window_size(2520, 1680)
        driver.get('https://www.vinted.fr/vetements?search_text=&catalog[]=79&size_id[]=207&size_id[]=208&size_id[]=209&brand_id[]=88&brand_id[]=4273&price_to=10.00&currency=EUR&order=newest_first')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "onetrust-accept-btn-handler")
            )
        )

        button = driver.find_element(By.ID,"onetrust-accept-btn-handler")
        button.click()
        time.sleep(10)
        price_list = []
        id_list = []

        for i in range(1, 8):
            element = driver.find_element("xpath", f'/html/body/main/div/section/div/div[2]/section/div/div/div[15]/div/div[{i}]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/h3[1]')
            price_list.append(element.text)
            id_list.append(element.get_attribute('data-testid'))

        time.sleep(0.5)
        values = [(item) for item in price_list]
        values2 = [(item) for item in id_list]
        for item, item2 in zip(values, values2):
            mycursor.execute(f"INSERT IGNORE INTO product (price, product_id) VALUES ('{item}', '{item2}')")

        driver.quit()
        print(u)
        if (u + 1 != value):
            time.sleep(60)

print("Done !")
