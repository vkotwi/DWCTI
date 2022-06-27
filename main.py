import requests
import json


### USEFUL SITES
# https://www.codementor.io/@scrapingdog/10-tips-to-avoid-getting-blocked-while-scraping-websites-16papipe62


### NOTES
# Need to run tor.exe and use port 9050
# 9150 is when running the browser
# May need pysocks installed
# Made using python 3.8
# Install tor expert bundle and run tor.exe from there

### TODO
# WEBSITE PRECHECK: see if site "looks" safe, if so try and pull CSS ASCII only to check for
#   hidden links (SEE NOTE 1)
# Scrapy fastest
# Compare exit node to known bad exit nodes
# run tor.exe automatically on starting this script up

# Connectors:
# DB setup
# crawler
# ml reads site from memory and only stores scrapes of info, then if finds info
# on othersite returns url for manual verification
# Supervised and unsupervsed learning

### NOTES FOR SCRAPER
# 1. Watch out for honeypot links -> look for CSS Display: hidden and visability: none

import prerequisites.populate_db
import prerequisites.prechecks
import crawler.Tor_Crawler.run_crawler

