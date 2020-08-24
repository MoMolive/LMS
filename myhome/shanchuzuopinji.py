# coding = utf - 8
from selenium import webdriver
from time import sleep
# 删除前十条作品集
def sczpj():
    driver = webdriver.Chrome()
    driver.get('https://learn.dev.longan.eliteu.xyz/manage/portfolio/')
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="normal_login_username"]').send_keys('abc')
    sleep(1)
    driver.find_element_by_xpath('//*[@id="normal_login_password"]').send_keys('123456')
    sleep(1)
    driver.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[1]/div[2]/div[1]/div/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolioItem"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]').click()
    sleep(4)
    driver.refresh()

    sleep(3)
    driver.quit()