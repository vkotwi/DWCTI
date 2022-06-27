### INFO
# Categorise by loading in model
# Extract info of revelvant models

import re 
import string 
import nltk 
import spacy 
import pandas as pd 
import numpy as np 
import math 
from tqdm import tqdm 

from spacy.matcher import Matcher 
from spacy.tokens import Span 
from spacy import displacy 

pd.set_option('display.max_colwidth', 200)

# requires: py -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


string = """ AN0NYM0US'z F0RUM AN0NYM0US'z F0RUM ....White Hats & Black Hats.... Index Search Register Login You are not logged in. Topics: Active | Unanswered Administrative Forum Topics Posts Last post 1 Announcements Description of
your first forum. 0 0 Never White Hat Forum Topics Posts Last post 1 General Discussion This forum is for General Discussion etc. 0 0 Never 2 Apps, Warez, Legal Softwarez This forum is for legal soft and etc. 2 2 2014-10-22 21:13:37
by neo 3 Virus Removal, Anti Virus And File Analysis This forum is for virus removal discussion and help also for file Analysis. 0 0 Never 4 Securing Your Server And Websites This forum is for help/Discussion and tutorials on how to
keep your website and server secure. 0 0 Never 5 Security Encryptions etc. Encrypt user's soft, mails, im's etc. 0 0 Never Black Hat Forum Topics Posts Last post 1 Beginner Hacking This is for the entry level hacker wishing to learn
more about the art of Hacking. 1 1 2016-04-16 10:48:29 by Ludwig_marrie 2 Website and Forum Hacking DDos, Deface, SQL Injection, what not ?! take down! 2 3 2016-01-18 23:32:49 by RAF 3 RATs, Keyloggers, Malwares the classics hacking
methods & tools on this section. 0 0 Never 4 Botnets, IRC Bots, and Zombies age of electronic zombies... 0 0 Never 5 Cryptors, Encryptions, and Decryptions Encryption is the art of concealing data and code, includes hash cracking 0 0
Never 6 Wireless Hacking Wifi WPA WEP Bluetooth 4G LTE Wireless Hacking 0 0 Never 7 Mobile, Android, PDA Hacking iOS, Android, PDA, GPS hacking topics 0 0 Never 8 VPN, Proxies, Settings, Socks & Safety after all, we all need to spoof
identity. 0 0 Never 9 Newbie Questions never feel less, start at something, clear your hacking doubts here 0 0 Never 10 SEO & Marketing Search Engine Optimization, Internet Marketing and more. 1 1 2016-08-23 22:30:47 by gnosis Board
information Board statistics Total number of registered users: 86 Total number of topics: 6 Total number of posts: 7 User information Newest registered user: Twoure42 Registered users online: 0 Guests online: 1 Board footer Jump to
Announcements General Discussion Apps, Warez, Legal Softwarez Virus Removal, Anti Virus And File Analysis Securing Your Server And Websites Security Encryptions etc. Beginner Hacking Website and Forum Hacking RATs, Keyloggers, Malwares
Botnets, IRC Bots, and Zombies Cryptors, Encryptions, and Decryptions Wireless Hacking Mobile, Android, PDA Hacking VPN, Proxies, Settings, Socks & Safety Newbie Questions SEO & Marketing Powered by FluxBB """

text = "GDP in developing countries such as Vietnam will continue growing at a high rate." 
doc = nlp(string)

for tok in doc: 
  print(tok.text, "-->",tok.dep_,"-->", tok.pos_)

# New virus affecting windows 7 update 8
# 'virus' VERB NOUN NOUN
# Find then pull sentence

# Barclays bank was hacked
# 'hack' NOUN <- reduced already e.g. hacked x

# New vulnerability for x
# New vulnerability found for x
# New exploit created for x
# I made an 'exploit' that can be used to bypass 'x system'


pattern = [{'POS':'virus'}, 
           {'LOWER': 'VERB'}, 
           {'LOWER': 'as'}, 
           {'POS': 'PROPN'} #proper noun]
