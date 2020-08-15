from selenium import webdriver
import schedule
import time
import datetime

driver = webdriver.Chrome()


def next_run(self):
    if not self.jobs:
        return None
    return min(self.jobs).next_run


def idle_seconds(self):
    return next_run(schedule) - datetime.datetime.now()

# set username license_pate_number phone email the_day_you_stay and the date
def parking_order():
    driver.get('https://www.youparking.com.tw/booking-calendar.php')
    name = "username"
    license_number = "CAR-1234"
    phone = "09123456789"
    email = "test@github.com"
    stay_day = "3"
    driver.find_element_by_id('name').send_keys(name)
    driver.find_element_by_id('carno').send_keys(license_number)
    driver.find_element_by_id('tel').send_keys(phone)
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('staydays').send_keys(stay_day)
    # set the day you order
    js = """var selday='2020-08-29';document.getElementById("bookingday").innerHTML = "預定停車日期 ： " + selday;document.forms["contactform"].elements["parkingdate"].value = selday;"""
    driver.execute_script(js)
    time.sleep(0.5)
    driver.find_element_by_id('submitbtn').click()
# set timer
schedule.every().day.at("00:00").do(parking_order)


while True:
    schedule.run_pending()
    print('剩下時間: ' + str(idle_seconds(schedule))[:7])
    time.sleep(1)