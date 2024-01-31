```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Email service provider's signup page URL
    BASE_URL = os.getenv('BASE_URL', 'https://example.com/signup')

    # Common user agent string for web requests
    USER_AGENT = os.getenv('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    # The maximum number of retries for failed account creation attempts
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', '5'))

    # List of proxies to be used by the proxy_manager.py
    PROXY_LIST = os.getenv('PROXY_LIST', 'proxies.txt').split(',')

    # Default headers for web requests
    HEADERS = {
        'User-Agent': USER_AGENT
    }

    # ID names of DOM elements
    DOM_ELEMENTS = {
        'signup_form_id': 'signup-form',
        'username_field_id': 'username',
        'password_field_id': 'password',
        'email_field_id': 'email',
        'submit_button_id': 'submit'
    }

    # Messages
    MESSAGES = {
        'SUCCESS_MESSAGE': 'Account successfully created.',
        'ERROR_MESSAGE': 'An error occurred during account creation.',
        'RETRY_MESSAGE': 'Retrying account creation.'
    }

    # Configuration for account details
    ACCOUNT_DETAILS = {
        'min_username_length': 8,
        'max_username_length': 15,
        'password_length': 12
    }

    # Configuration for the proxy manager
    PROXY_CONFIG = {
        'proxy_file': 'proxies.txt',
        'test_url': 'https://www.google.com'
    }

    # Configuration for the name generator
    NAME_GENERATOR_CONFIG = {
        'name_list_file': 'names.txt',
        'surname_list_file': 'surnames.txt'
    }

    # Configuration for logging
    LOGGING_CONFIG = {
        'log_file': 'email_creator.log',
        'log_level': 'INFO'
    }

    # Define any other configuration parameters here
    # ...

# Optionally, you can load additional configuration from a file
def load_additional_config(config_file='additional_config.py'):
    # Implement loading of additional configuration if necessary
    pass
```