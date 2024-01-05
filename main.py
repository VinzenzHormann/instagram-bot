from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
from tkinter import *
from tkinter import messagebox
from Comment import Comment

USERNAME = ""
PASSWORD = ""
KEYWORD = ""
COMMENTS = []


def run():
    #get inputs
    #KEYWORD: without "#"
    #COMMENTS: need to be seperated by "#" (haschtags)
    USERNAME = username_entry.get()
    PASSWORD = password_entry.get()
    KEYWORD = tag_entry.get()
    COMMENTS = com_entry.get().split("#")

    # run from comment Class
    bot = Comment()
    bot.login(USERNAME, PASSWORD)
    bot.comment_like(USERNAME, COMMENTS, KEYWORD)

#UI with tkinther
window = Tk()
window.title("Hirschuwa_Insta_Bot")
window.config(padx=50, pady=50)

username_label = Label(text="IG Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=50)
username_entry.grid(column=1, row=2)


password_label = Label(text="IG Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=50)
password_entry.grid(column=1, row=3)

tag_label = Label(text="Tag to search:")
tag_label.grid(column=0, row=4)
tag_entry = Entry(width=50,)
tag_entry.grid(column=1, row=4, rowspan=2)

com_label = Label(text="Comments")
com_label.grid(column=0, row=6)
com_entry = Entry(width=50, )
com_entry.grid(column=1, row=6)

run_button = Button(text="RUN", width=44, command=run)
run_button.grid(column=1, row=7, columnspan=2)

window.mainloop()
