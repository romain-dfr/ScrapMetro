from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Excel import save_to_excel

def metro(driver, url):
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    title = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mfcss_article-detail--title']")))
    price_xpath_list = [
        "//table[@class='table table-striped table-condensed']//tr[last()]//td//div//div[last()]//span",
        "//span[@class='mfcss_article-detail--price-breakdown primary promotion']//span//span",
        "//span[@class='mfcss_article-detail--price-breakdown primary']//span//span"
    ]

    for xpath in price_xpath_list:
        try:
            price = driver.find_element(By.XPATH, xpath)
            save_to_excel(title.text, price.text)
            return
        except:
            pass

    driver.quit()