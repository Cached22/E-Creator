# Application Setup and Usage Guide

Welcome to our application. This document will guide you through the setup and usage of the application.

## Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```
git clone <repository-url>
```

## Step 2: Install Dependencies

Navigate to the cloned directory and install the required dependencies:

```
pip install -r requirements.txt
```

## Step 3: Configure Application Settings

Edit the `config/settings.py` file to configure the application settings. You can specify general settings such as the option to add a phone number.

```python
# Example setting to add a phone number
PHONE_NUMBER = "+1234567890"  # Uncomment to use a phone number
```

## Step 4: Set Up Proxy

If you need to use a proxy, configure the proxy settings in `config/proxy.py`.

```python
# Example proxy configuration
PROXY = {
    "http": "http://yourproxy:port",
    "https": "https://yourproxy:port"
}
```

## Step 5: Simulate Mouse Actions

The application can simulate mouse actions using `utils/mouse_simulation.py`. This is handled automatically by the `MouseSimulator` function in `app.py`.

## Step 6: Manage Cookies

To manage cookies, edit the `utils/cookie_management.py` file. The `CookieManager` class will handle the storage and retrieval of cookies.

## Step 7: Set Up SMS Services

Configure the SMS services like Durian and 5sims in their respective files:

- `utils/sms_services/durian.py`
- `utils/sms_services/5sims.py`

You can select the service you want to use in `app.py` using the `SMSServiceFactory`.

## Step 8: Bypass Bot-Detection

The `utils/captcha_bypass.py` file contains the `CaptchaBypass` class to help bypass bot-detection mechanisms.

## Step 9: Run the Application

Run the application using the following command:

```
python app.py
```

Follow the on-screen instructions to proceed with the application's functionality.

## Support

For any issues or questions, please refer to the issue tracker on the repository or contact the support team.

Thank you for using our application!