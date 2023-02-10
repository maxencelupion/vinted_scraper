# vinted_scraper
An easy functional scraper of the website Vinted. The output is stored in an MySQL database. The program will create by itself a database named ```vinted``` wich contains the table ```product```. You can find the ```price``` and ```product_id``` columns in this table.

# Requirements :

You need to install :
- MySql connector
- Selenium

# Usage :
```
python3 vinted_scraper.py
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/114016583/218108441-9719a4da-2d7b-4d53-a2b6-0d5f6485ee35.png" width="400">
</p>
Here you need to enter your MySQL localhost password (hidden by getpass) with root user, and then enter the number of times the program will run, with a delay of 60s.
<p align="center">
  <img src="https://user-images.githubusercontent.com/114016583/218109174-182cb731-e1f3-432f-973a-b2ae8f20e21d.png" width="400">
</p>

#### Now the program will run in headless mode.
