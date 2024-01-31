import unittest
from unittest.mock import patch
from selenium.webdriver.common.by import By
from email_creator.web_interaction import fill_form, submit_form
from email_creator.config import BASE_URL, USER_AGENT, HEADERS

class TestWebInteraction(unittest.TestCase):

    @patch('email_creator.web_interaction.webdriver')
    def test_fill_form(self, mock_webdriver):
        # Mocking the WebDriver and WebElement
        mock_driver = mock_webdriver.Chrome.return_value
        mock_element = mock_driver.find_element.return_value

        # Mocking the form data
        form_data = {
            'username': 'testuser',
            'password': 'securepassword123',
            'email': 'testuser@example.com'
        }

        # Call the fill_form function
        fill_form(mock_driver, form_data)

        # Assertions to ensure each form field is filled correctly
        mock_driver.find_element.assert_any_call(By.ID, 'username_field_id')
        mock_element.send_keys.assert_any_call(form_data['username'])

        mock_driver.find_element.assert_any_call(By.ID, 'password_field_id')
        mock_element.send_keys.assert_any_call(form_data['password'])

        mock_driver.find_element.assert_any_call(By.ID, 'email_field_id')
        mock_element.send_keys.assert_any_call(form_data['email'])

    @patch('email_creator.web_interaction.webdriver')
    def test_submit_form(self, mock_webdriver):
        # Mocking the WebDriver
        mock_driver = mock_webdriver.Chrome.return_value
        mock_element = mock_driver.find_element.return_value

        # Call the submit_form function
        submit_form(mock_driver)

        # Assertions to ensure the form is submitted
        mock_driver.find_element.assert_called_once_with(By.ID, 'submit_button_id')
        mock_element.click.assert_called_once()

if __name__ == '__main__':
    unittest.main()