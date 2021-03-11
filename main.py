from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
import re
import time

from send_check_email import send_mail
from jobbank_spreadsheet import createSpreadsheet
from scraper_jobbank import *
from basic_cli_gui import *
from selecting_files import getResume
######################################     GET DATA FROM CANADA JOB BANK     ######################################


# Global 
job_url_list = []
primary_info = []
final_data = []
detailed = 'Unfortunately, I can only work part-time. I can only work in late afternoon or evenings and no Tuesday/Wednesday. I understand the nature of my responsibilities may require me to come in person but if possible, I hope you can accommodate my request of working from home.'
simple = 'Please accept my resume for the job position'
msg = 0

# flags
counter = 0
login_flag = 0
app_flag = 0
speed = 0
email_flag = 0
date = datetime.today().strftime('%Y-%m-%d')

print('\n\n--- Canada Job Bank Automation ---\n----------------------------------\n')
print('WARNING: This program uses Gmail.\n         Please have "Less secure app access" enabled and disable "2-Step Verification".\n         Please close all other background applications if possible.\n')



name = str(input("Please enter your email sign-off: ")  )
keyword = str(input("\nPlease enter one(1) keyword to exclude from the search results and press ENTER (eg. 'chef'): ")  )
pathname = str(getResume())

while msg == 0:
    mainHeaderPrint(keyword, name, pathname)
    msg = getMsg()
    if msg == 2:
        sall = str(input('Password to use detailed: '))
        if sall == 'sall':
            print('verfied...')
            time.sleep(2)
        else:
            msg = 0

while speed == 0:
    mainHeaderPrint(keyword, name, pathname)
    speed = getTimeSpeed()

while email_flag == 0:
    mainHeaderPrint(keyword, name, pathname)
    email_flag = dontDoIt()


while login_flag == 0 :
    mainHeaderPrint(keyword, name, pathname)
    login_flag,username,beans = login_email(send_mail,pathname)
    if( login_flag == 1):
        break


mainHeaderPrint(keyword, name, pathname)
start = input('\nPlease press enter to start the automated process:  ')

job_url,source,soup,browser, job_url_list = openScraper()
browser.minimize_window()
mainHeaderPrint(keyword, name, pathname)

for posting in job_url_list:

    job_url_combined = 'https://www.jobbank.gc.ca/' + posting

    try:
        browser.get(job_url_combined)
        browser.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/div[2]/section/p/button').click()
        time.sleep(speed)
        mainHeaderPrint(keyword, name, pathname)

        try:
                primary_info = scrapePrimary(browser)
                final_data.append(primary_info)
                counter = counter + 1
        except:
            print("")
        
    except:
        mainHeaderPrint(keyword, name, pathname)
        print('Error retrieving posting. \n')
    

    if counter < 2:
        print('\n... ', counter, ' posting retrieved')
    else:
        print('\n... ', counter, ' postings retrieved')


if len(final_data) < 1:
        app_flag = 1


######################################     SAVE DATA ONTO CSV/SPREADSHEET     ######################################
mainHeaderPrint(keyword, name, pathname)
if app_flag == 0:
    createSpreadsheet(final_data)
    print('Spreadsheet Created')
    time.sleep(1)
else:
    print('')

counter = 0
if email_flag == 1:
######################################     EMAILING JOBS     #####################################
    for i in range(len(final_data)):
        excluded = re.findall(r'\b{0}\b'.format(keyword),final_data[i][1], re.IGNORECASE)

        if (excluded and excluded[0] != ""):
            print('\nEmail not sent to ' + final_data[i][1] + ' because it matches the excluded word: "' + keyword + '"\n')
        else:
            try:

                if msg == 1:
                    send_mail(username, final_data[i][2], 'Job Application', 'Dear Hiring Manager,\n\n{1}{2}.\n\nThanks,\n{0}\n'.format(name, simple, final_data[i][0]), pathname, 'smtp.gmail.com', '587', username, beans)

                else:
                    send_mail(username, final_data[i][2], 'Job Application', 'Dear Hiring Manager,\n\n{1}\n\nThanks,\n{0}\n'.format(name, detailed), pathname, 'smtp.gmail.com', '587', username, beans)
                mainHeaderPrint(keyword, name, pathname)
                counter = counter + 1
                print('\nEmail sent to: ' + final_data[i][1] + '')
                print('Emails sent:  ', counter)
                time.sleep(3)

            except:
                mainHeaderPrint(keyword, name, pathname)
                print('\nAn error occured while emailing ' + final_data[i][1] + '. This employeer will not be emailed.')
                time.sleep(3)

else:
    print('')


browser.close()        
mainHeaderPrint(keyword, name, pathname)
print('')
if app_flag == 0:
    print('The data has been saved in a file called table_{0}.xlsx in the directory of this program.'.format(date))
    print('Emails sent: ', counter)
else:
    print('The program did not find any postings. Please try again at a later time.')
print("\n.................................\nThe program is complete. Please stay hydrated and close the application.\n\n")