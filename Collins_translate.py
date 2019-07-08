import io
import time
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def main():

	inFile = sys.argv[1]
	out_file = sys.argv[2]

	print ("Important Note: Please check the usage policy of Collins ENG-HINDI translator")
	time.sleep(2)

	print ("Please wait while we open Google Chrome")
	driver = webdriver.Chrome('/Users/sanjanagoel/Desktop/Collins/chromedriver')
	driver.maximize_window()

	print ("Opening Collins ENG-HINDI translator")
	driver.get ('https://www.collinsdictionary.com/dictionary/english-hindi')

	print ("Reading input file")
	with open(inFile, 'r') as fin:
		for line in fin.readlines(): 
			for word in line.split():
				send_data = driver.find_element_by_name('q')
				send_data.send_keys(word)

				time.sleep(2)
				search = driver.find_element_by_xpath("//i[@class = 'icon-search icon-fw']")
				search.click()

				word_meaning = driver.find_element_by_class_name('hom')
				print(word_meaning)
				meaning = word_meaning.text

				with io.open(out_file, "a", encoding="utf-8") as fout:
					fout.write(meaning)

	print("Translated data stored in \"" + out_file + "\" file.")
	driver.close()
if __name__ == '__main__':
	main()