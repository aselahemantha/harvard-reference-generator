from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Setup Chorme Driver


def create_site(site):
    driver = webdriver.Chrome()
    driver.get("https://www.harvardreferencinggenerator.com/")
    driver.implicitly_wait(5)  # wait 5 seconds

    try:
        search_button = driver.find_element_by_id("reference-a-website-label")
        print(search_button)
        search_button.click()

        # find input point and send keys

        enter_text = driver.find_element_by_name("website")
        enter_text.send_keys(site)
        enter_text.send_keys(Keys.ENTER)

        driver.implicitly_wait(4)

        get_text = driver.find_element_by_tag_name("blockquote")
        output_text = ''
        output_text = get_text.text
        driver.close()
        return output_text
    except:
        driver.close()
        return "Automation Fail, Try Again"

