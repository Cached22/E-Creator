from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .config import BASE_URL, USER_AGENT, HEADERS
from .utils import random_delay
from .logger import log_event

def initialize_browser(proxy=None):
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={USER_AGENT}')
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=options)
    return driver

def navigate_to_signup_page(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'signup_form_id'))
    )

def fill_form(driver, account_details):
    try:
        username_field = driver.find_element(By.ID, 'username_field_id')
        password_field = driver.find_element(By.ID, 'password_field_id')
        email_field = driver.find_element(By.ID, 'email_field_id')

        username_field.send_keys(account_details['username'])
        password_field.send_keys(account_details['password'])
        email_field.send_keys(account_details['email'])

        log_event('Form filled with account details')
    except Exception as e:
        log_event(f'Error filling the form: {e}', level='ERROR')
        raise

def submit_form(driver):
    try:
        submit_button = driver.find_element(By.ID, 'submit_button_id')
        submit_button.click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), SUCCESS_MESSAGE)
        )
        log_event('Form submitted successfully')
        return True
    except TimeoutException:
        log_event('Timeout waiting for success message', level='ERROR')
        return False
    except Exception as e:
        log_event(f'Error submitting the form: {e}', level='ERROR')
        raise

def create_account(account_details, proxy=None):
    driver = initialize_browser(proxy)
    try:
        navigate_to_signup_page(driver)
        fill_form(driver, account_details)
        success = submit_form(driver)
        return success
    finally:
        random_delay()
        driver.quit()