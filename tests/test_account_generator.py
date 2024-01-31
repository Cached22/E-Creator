```python
import unittest
from unittest.mock import patch
from email_creator.account_generator import create_account
from email_creator.config import CONFIG
from email_creator.utils import save_account_details

class TestAccountGenerator(unittest.TestCase):

    @patch('email_creator.account_generator.generate_name')
    @patch('email_creator.account_generator.get_proxy')
    @patch('email_creator.account_generator.fill_form')
    @patch('email_creator.account_generator.submit_form')
    def test_create_account_success(self, mock_submit_form, mock_fill_form, mock_get_proxy, mock_generate_name):
        # Mock the generate_name function to return a fixed name
        mock_generate_name.return_value = "testuser"

        # Mock the get_proxy function to return a fixed proxy
        mock_get_proxy.return_value = None  # Assuming no proxy for simplicity

        # Mock the fill_form function to simulate form filling without errors
        mock_fill_form.return_value = True

        # Mock the submit_form function to simulate successful form submission
        mock_submit_form.return_value = True

        # Call the create_account function
        success, account_details = create_account()

        # Assert that the account creation was successful
        self.assertTrue(success)
        self.assertEqual(account_details['username'], "testuser")

    @patch('email_creator.account_generator.generate_name')
    @patch('email_creator.account_generator.get_proxy')
    @patch('email_creator.account_generator.fill_form')
    @patch('email_creator.account_generator.submit_form')
    def test_create_account_failure(self, mock_submit_form, mock_fill_form, mock_get_proxy, mock_generate_name):
        # Mock the generate_name function to return a fixed name
        mock_generate_name.return_value = "testuser"

        # Mock the get_proxy function to return a fixed proxy
        mock_get_proxy.return_value = None  # Assuming no proxy for simplicity

        # Mock the fill_form function to simulate form filling without errors
        mock_fill_form.return_value = True

        # Mock the submit_form function to simulate failed form submission
        mock_submit_form.return_value = False

        # Call the create_account function
        success, account_details = create_account()

        # Assert that the account creation failed
        self.assertFalse(success)
        self.assertIsNone(account_details)

    @patch('email_creator.account_generator.create_account')
    def test_bulk_account_creation(self, mock_create_account):
        # Mock the create_account function to simulate multiple account creations
        mock_create_account.side_effect = [
            (True, {'username': 'user1'}),
            (True, {'username': 'user2'}),
            (False, None),  # Simulate a failure in account creation
            (True, {'username': 'user3'})
        ]

        # Define the number of accounts to create
        num_accounts = 4
        created_accounts = []

        # Simulate bulk account creation
        for _ in range(num_accounts):
            success, account_details = create_account()
            if success:
                created_accounts.append(account_details)

        # Assert that the correct number of accounts were created
        self.assertEqual(len(created_accounts), 3)

if __name__ == '__main__':
    unittest.main()
```