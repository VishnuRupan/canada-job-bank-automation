from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime


def getJobEmail(browser):
    email_link = browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/div[2]/div/p/a').get_attribute('href')
    email_link = email_link[7:]
    return email_link


def getJobTitle(browser):
    title = browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/h2/span[1]').text
    return title.title()


def getJobPosted(browser):
    posted = browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/p/span[3]/span[2]/span/strong').text    
    return posted.title()

def getJobPostingInfo(browser):
    all_posting_info = browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/ul').text
    posting_info_list = list(all_posting_info.split('\n')) 
    return posting_info_list



def openScraper():
    job_url_list = []
    job_url = 'https://www.jobbank.gc.ca/'

    source = requests.get('https://www.jobbank.gc.ca/jobsearch/jobsearch?d=120&fage=2&fn=1311&fn=1431&fn=1432&fn=4411&fn=4412&fn=6211&fn=6311&fn=6322&fn=6622&fn=6711&fn=7611&mid=22437&sort=M&fsrc=16#results-list-content').text
    soup = BeautifulSoup(source, 'lxml')


    browser = webdriver.Chrome(ChromeDriverManager().install())

    for info in soup.find_all('article'):
        job_url_list.append(info.a['href'])

    return job_url, source, soup, browser, job_url_list


def scrapePrimary(browser):
    primary_info = []
    date = datetime.today().strftime('%Y-%m-%d')
    primary_info.append(getJobTitle(browser))
    primary_info.append(getJobPosted(browser))
    primary_info.append(getJobEmail(browser))
    primary_info.append((getJobPostingInfo(browser)[-1:])[0][9:])

    if getJobPostingInfo(browser)[4][0] == '$':
        salary = getJobPostingInfo(browser)[4]
    else:
        salary = getJobPostingInfo(browser)[6]
    primary_info.append(salary)
    primary_info.append(date)

    if len(primary_info) >= 4:
        print('Title:   ', primary_info[0])
        print('Posted:  ', primary_info[1])
        print('Email:   ', primary_info[2])
        print('Job ID:  ', primary_info[3])
        print('Salary:  ', primary_info[4])
    
    return primary_info