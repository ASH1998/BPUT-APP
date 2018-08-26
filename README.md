# BPUT-APP
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)  [![HitCount](http://hits.dwyl.io/ASH1998/android-digit-recogniser.svg)](http://hits.dwyl.io/ASH1998/android-digit-recogniser)

This app is for bput students only!!
It uses Selenium as main Scrapper.
# Disclaimer
The BPUT site has changed recently. I dont have time to modify it further.
So in order to use this script, change the `find_elements_by_ID` throughout the `scrapper.py`. You can get these by inspecting the BPUT results site. OR you can just develop your own script. GOOD LUCK.

# Dependencies
1. Python
2. Selenium
3. No head/ ghost browser : [link](https://github.com/ASH1998/BPUT-APP/blob/master/phantomjs.exe)
4. BS4

# Usage
## Step 1.
The results will be gathered in the filename in line 7 of`scrapper.py`.
Open `scrapper.py` to modify line 17 `select.select_by_visible_text('Odd (2016-17)')`. Change it to whichever result you want.
These can be changed manually.
## Step 2.
Run `get_rolls.py`
Set arguements at the end, the roll number i.e registration number and total number of students to get results for.
## Step 3.
Results will be gathered in same repo of `get_rolls.py `, with as both text and json files.

# TODO:
1. ~~Multiprocessing~~
