@ECHO OFF 
TITLE AZ Lyrics Crawler
ECHO Please wait... Updating Selenium
pip install selenium
PAUSE
python azlyrics_scraper.py songs_artists.txt results.csv
PAUSE
ECHO DONE!
