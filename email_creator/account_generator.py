```python
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from .config import CONFIG
from .proxy_manager import get_proxy
from .name_generator import generate_name
from .web_interaction import fill_form, submit_form
from .logger import log_event

class AccountGenerator:
    def __init__(self):
        self.driver = None
        self.setup_driver()

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        proxy_details = get_proxy()
        if proxy_details:
            options.add_argument(f'--proxy-server={proxy_details["ip"]}:{proxy_details["port"]}')
        self.driver = webdriver.Chrome(options=options)

    def create_account(self):
        try:
            account_details = generate_name()
            self.driver.get(CONFIG['BASE_URL'])
            fill_form(self.driver, account_details)
            submit_form(self.driver)
            log_event(f"Account created successfully: {account_details['username']}")
            return account_details
        except WebDriverException as e:
            log_event(f"Error creating account: {str(e)}", error=True)
            return None
        finally:
            time.sleep(random.uniform(1, 3))  # Random sleep to mimic human behavior

    def create_bulk_accounts(self, number_of_accounts):
        created_accounts = []
        for _ in range(number_of_accounts):
            account = self.create_account()
            if account:
                created_accounts.append(account)
            if len(created_accounts) % 10 == 0:
                log_event(f"Created {len(created_accounts)} accounts so far.")
            time.sleep(random.uniform(1, 5))  # Random sleep to avoid rate limiting
        return created_accounts

    def close(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    generator = AccountGenerator()
    try:
        accounts = generator.create_bulk_accounts(CONFIG['TARGET_ACCOUNTS'])
        log_event(f"Total accounts created: {len(accounts)}")
    finally:
        generator.close()
```