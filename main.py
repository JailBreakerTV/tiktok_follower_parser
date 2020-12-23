import os
import random
import time
from win10toast import ToastNotifier

from selenium import webdriver

notifier = ToastNotifier()


def run():
    checker = FollowerChecker()
    counter = 29
    while counter <= 31:
        if counter == 30:
            checker.check_follower_amount_change()
            counter = 0
        time.sleep(1)
        counter = counter + 1


def find_follower_amount(username) -> int:
    current_path = os.getcwd()
    path = current_path + "/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(path, options=chrome_options)

    driver.get("https://www.tiktok.com/@" + username)

    time.sleep(random.randint(3, 6))

    driver.find_element_by_id("verify-bar-close").click()

    time.sleep(2)

    follower = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/header/h2[1]/div[2]/strong")

    time.sleep(1)

    amount = int(follower.text)

    time.sleep(2)

    driver.quit()

    return amount


class FollowerChecker:
    followerAmount = 0

    def check_follower_amount_change(self):
        new_follower = find_follower_amount("jailbreakereu")
        if new_follower != self.followerAmount:
            self.followerAmount = new_follower
            notifier.show_toast("FOLLOWER CHANGE", "Du hast nun " + str(new_follower) + " Follower!")


if __name__ == "__main__":
    run()
