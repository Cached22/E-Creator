```python
import sys
from email_creator.config import CONFIG
from email_creator.account_generator import create_account
from email_creator.logger import log_event
from email_creator.utils import setup_environment, save_account_details

def main():
    # Set up the environment and load configuration
    setup_environment()
    account_creation_count = CONFIG.get('target_account_count', 10)

    # Start the account creation process
    created_accounts = []
    for _ in range(account_creation_count):
        try:
            account_details = create_account()
            if account_details:
                log_event(f"Account created successfully: {account_details['email']}")
                created_accounts.append(account_details)
                save_account_details(account_details)
            else:
                log_event("Failed to create account. No details returned.", error=True)
        except Exception as e:
            log_event(f"An error occurred during account creation: {str(e)}", error=True)

    # Finalize the process
    log_event(f"Total accounts created: {len(created_accounts)}")
    if len(created_accounts) < account_creation_count:
        log_event("Some accounts could not be created. Check logs for details.", error=True)

    return created_accounts

if __name__ == "__main__":
    created_accounts = main()
    sys.exit(0 if len(created_accounts) == CONFIG.get('target_account_count', 10) else 1)
```