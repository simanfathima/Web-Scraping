import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_youtube(links):

	#Initialising a list to store data extracted from the URLs	
	
	result =[]

	#Example range- 3 videos

	for link in range(2):
 

		#Converting Video IDs to URLs

		url="https://www.youtube.com/watch?v="+links[link]

		#initialising a dictionary to store the data extracted from each URL

		data={}


		like=""
		dislike=""
		comment_section=[]

		#opening the URL in a chrome Window
	
		driver=webdriver.Chrome()
		driver.get(url)
		
		
		#Section 1- Scraping Link,views,likes,dislikes

		#Extracting video-id

		data['link']=url[32:]
		
		#Extracting video-views

		data['views']=(driver.find_element_by_class_name("view-count").text[:-6])
		
		#Extracting likes and dislikes data from top-level-buttons (like,dislike,share,save)

		buttons=driver.find_element_by_id("top-level-buttons").text[:-11]

		for i in range(len(buttons)):
			if buttons[i] =="\n":
				like=buttons[0:i]
				dislike=buttons[i+1:]
		
		#Storing Likes into the dictionary

		data['likes']=like
		
		#Storing dislikes into the dictionary
				
		data['dislikes']=dislike

		#Extracting video-uploaded date

		data['uploaded_date']=driver.find_element_by_id("date").text[1:]


		#Section 2 - Extracting Dynamic contents(comments)

		#Scrolling down on the page to reach comments

		driver.execute_script('window.scrollTo(1, 100);')

		#wait till the comments are loaded
		
		time.sleep(5)
		
		#Scroll down further		
				
		driver.execute_script('window.scrollTo(1, 3000);')

		#Locating the contents element
		
		comment_div=driver.find_element_by_xpath('//*[@id="contents"]')

		#Scraping only the comments text		
		
		comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')

		for comment in comments:
		    comment_section.append(comment.text)
		
		#Appending comments to the data dictionary

		data['comments']=comment_section

		#Appending 'data' dictionary into 'result' list
				
		result.append(data)
		
		#Leaving the Chrom window		
		
		driver.close()

	return result

if __name__ == "__main__":
	
	#Extracting Video URLs from a csv file

	#Example- Scraping data from three videos 

	df = pd.read_csv("marvel.csv", skiprows=1,usecols=[0])
	links_list=df.values.tolist()
	links = []

	#Converting 2D list (links_list) to 1D list (links)	

	for sublist in links_list:
		for item in sublist:
			links.append(item)
	for i in links:
		i.replace("'","")
	

	#Converting the result list of dictionaries into a DataFrame

	scraped_df=pd.DataFrame(scrape_youtube(links))
	
	#Writing the Scraped data into a csv file

	scraped_df.to_csv('marvel_scraped_data.csv', index=False)















