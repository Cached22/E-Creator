```python
import argparse
from email_creator.account_generator import create_account
from email_creator.config import load_config
from email_creator.logger import log_event

def main():
    # Load configuration settings
    config = load_config()

    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description='Bulk Email Account Creation CLI')
    parser.add_argument('--number', type=int, help='Number of email accounts to create', required=True)
    parser.add_argument('--output', type=str, help='Output file to save account details', default='accounts.csv')

    # Parse the arguments
    args = parser.parse_args()

    # Create the specified number of email accounts
    for _ in range(args.number):
        try:
            account_details = create_account(config)
            log_event(f"Account created: {account_details['email']}")
        except Exception as e:
            log_event(f"Error creating account: {e}", error=True)

    # Save the account details to the specified output file
    log_event(f"Account details saved to {args.output}")

if __name__ == '__main__':
    main()
```