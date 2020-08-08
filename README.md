# YouTube-Data Analysis

Web-Scraping Using Python.

Scraping data from Youtube.

# Prerequisites:
--Python is required to clean the data, explore it, and build models.

--Knowledge of some basic libraries like Pandas and NumPy.

--Basic knowledge of HTML and CSS.

--Install Selenium,requests,BeautifulSoup(If required) modules.

# Scraping Data From YouTube:
--Open YouTube in your browser. Type in the Video you want to scrape data from. Copy the URL after doing this.

--Set up the driver to fetch the content of the URL from YouTube,

 " driver = webdriver.Chrome() 
   driver.get("YOUR_LINK_HERE") "
   
--Paste the link into to driver.get(“ Your Link Here ”) function and run the cell. This will open a new browser window for that link. 

--Fetch all the video links present on that particular page. We will create a “list” to store those links

--Go to the browser window, right-click on the page, and select ‘inspect element’ and locate elements like title,link,views etc.

--For instance,search for the anchor tag with id = ”video-title” and then right-click on it -> Copy -> XPath. The XPath should look something like : //*[@id=”video-title”].

--Create a dataframe with 6 columns – “link”, “views”, “likes”,"dislikes","uploaded date" and “comments”.

We are all set to scrape the video details from YouTube. Here’s the Python code to do it.

NOTE: This is a Sample Code only. The original Project dynamically Scrapes data from 500 videos from 4 different channels each
