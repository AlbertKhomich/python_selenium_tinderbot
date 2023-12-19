from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Accept all cookies
def cookie():
    wait.until(EC.frame_to_be_available_and_switch_to_it("sp_message_iframe_729697"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#notice > div.message-component.message-row.box-shadow.\.container > div:nth-child(3) > div.message-component.message-row.button-row > button.message-component.message-button.no-children.focusable.button.sp_choice_type_11'))).click()
    driver.switch_to.default_content()


login = "+4915110050210"
password = os.environ['password']

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bumble.com/")

original_window = driver.current_window_handle

wait = WebDriverWait(driver, 10)

# Login
cookie()

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/a'))).click()

cookie()

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div'))).click()

wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]'))).click()

driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input').send_keys(login)
driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input').send_keys(password + Keys.ENTER)

# Like All
driver.switch_to.window(original_window)

while True:
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span'))).click()
