#!/usr/bin/env python
# coding: utf-8

# In[18]:


from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import sys
import os



class InstagramBot:
    def sleeplimit():
        limit = randint(7,15)
        sleep(limit)    
        
    def scrollDown(self):
        jscommand="""
                page=document.querySelector("._aano");
                page.scrollTo(0,page.scrollHeight);
                var endofpage = page.scrollHeight;
                return endofpage;
                """
        while True:
            endofpage = self.driver.execute_script(jscommand)
            InstagramBot.sleeplimit()
            end = endofpage        
            endofpage=self.driver.execute_script(jscommand)
            InstagramBot.sleeplimit()
            if end == endofpage:
                break
    def Login(self,*,usern, passw):
#         use the option parameter for opening the current instance        
        try:
            self.driver = uc.Chrome(use_subprocess=True)     
            self.driver.maximize_window() 
            self.driver.get("https://www.instagram.com/")
            InstagramBot.sleeplimit()
            username = self.driver.find_element(By.XPATH,"//input[@aria-label='Phone number, username, or email']")
            username.send_keys(usern)
            password = self.driver.find_element(By.XPATH,"//input[@aria-label='Password']")
            password.send_keys(passw)
            InstagramBot.sleeplimit()
            loginbtn = self.driver.find_element(By.XPATH,"//button[@type='submit']/div").click()
            InstagramBot.sleeplimit()
            try:
                notnowbtn = self.driver.find_element(By.XPATH,"//button[contains(text(),'Not Now')]").click()
            except:
                pass
        except:
            InstagramBot.Login()
        
    def followersScrape(self):
        file_object = open('scrapefollowers.txt','w')
        botList = ['hello']
        for i in botList:
            self.driver.get(f'https://www.instagram.com/{i}/')
            InstagramBot.sleeplimit()
            self.driver.find_element(By.PARTIAL_LINK_TEXT,"followers").click()
            InstagramBot.sleeplimit()
            try:
                InstagramBot.scrollDown(self)
                follwersScrape = self.driver.find_elements(By.XPATH,"//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
                for i in follwersScrape:    
                    file_object.write(f'https://www.instagram.com/{i.text}/')
                    file_object.write('\n')
            except:
                pass
    def read_file_followers(self):
        file = open("scrapefollowers.txt", "r")
        lines = file.readlines()
        for l in range(len(lines)):
            lines[l] = lines[l].replace("\n", "")
        file.close()
        return lines
    
    def followLinks(self):
        followed_object = open('followed.txt','w')
        for l in InstagramBot.read_file_followers(self):
            try:
                self.driver.get(l)                
                try:
                    InstagramBot.sleeplimit()
                    self.driver.find_element(By.XPATH,'//div[text()="Follow"]').click()
                    sleep(randint(10*60, 15*60))
                    followed_object.write(l)
                    followed_object.write('\n')
                    print('Condition True')                    
                except:                
                    continue
            except:
                continue
                
    def read_file_comments(self):
        file = open("comments.txt", "r")
        lines = file.readlines()
        for l in range(len(lines)):
            lines[l] = lines[l].replace("\n", "")
        file.close()
        return lines

    def read_file_followed(self):
            file = open("followed.txt", "r")
            lines = file.readlines()
            for l in range(len(lines)):
                lines[l] = lines[l].replace("\n", "")
            file.close()
            return lines
        
    def likeStory_comments(self):
        for l in InstagramBot.read_file_followed(self):
            self.driver.get(l)
#             InstagramBot.sleeplimit()
            sleep(randint(10*60, 15*60))
            try:               
                storyAndCards = choice(["//li[@class='_acaz']","//div[@class='_aagw']",])        
                print(storyAndCards)
                try:
                    if storyAndCards == "//li[@class='_acaz']":
                        storiesLenth = len(self.driver.find_elements(By.XPATH,"//li[@class='_acaz']"))
                        InstagramBot.sleeplimit()
                        self.driver.find_elements(By.XPATH,"//li[@class='_acaz']")[randint(0,storiesLenth)].click()
                        InstagramBot.sleeplimit()
                        self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ESCAPE)
                        InstagramBot.sleeplimit()
                    else:                
                        postsLenght = len(self.driver.find_elements(By.XPATH,"//div[@class='_aagw']"))
                        self.driver.find_elements(By.XPATH,"//div[@class='_aagw']")[randint(0,postsLenght)].click() 
                        InstagramBot.sleeplimit()
                        likesComment = choice(["//span[@class='_aamw']",'//textarea[@aria-label="Add a comment…"]'])                
                        print(likesComment)
                        if likesComment == "//span[@class='_aamw']":
                            InstagramBot.sleeplimit()
                            self.driver.find_element(By.XPATH,"//span[@class='_aamw']").click()
                            InstagramBot.sleeplimit()
                            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ESCAPE)
                            InstagramBot.sleeplimit()
                        else:                   
                            commentdata = self.driver.find_element(By.XPATH,'//form[@class="_aidk"]/textarea').click()
                            InstagramBot.sleeplimit()
                            commentdata = self.driver.find_element(By.XPATH,'//textarea[@aria-label="Add a comment…"]')
                            commentdata.send_keys(choice(self.read_file_comments()))
                            InstagramBot.sleeplimit()
                            self.driver.find_element(By.XPATH,"//div[text()='Post']").click()
                            InstagramBot.sleeplimit()
                            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ESCAPE)
                except:
                    pass
            except:
                pass

def main():
    #-------------Start and end Timing-------------
    with open('stratEndTiming.txt') as file:
        file_ = file.read().split('\n')
        userStartTime = file_[0]
        userEndTime = file_[1]
        
    #-------------Setting ON/OFF-------------
    with open('processSetting.txt') as pfile:
        pfile_ = pfile.read().lower()
    
    while True:
        sleep(5)
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        if current_time>= userStartTime and current_time <= userEndTime:
            if pfile_ == 'on':
                obj = InstagramBot()
                obj.Login(usern="*****",passw="*****")
                obj.followersScrape()
                obj.followLinks()
                obj.likeStory_comments()
                
            else:            
                continue        
        else:
            continue

if __name__ == "__main__":
    pass

