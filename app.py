```python
from config.settings import ConfigLoader
from config.proxy import ProxyManager
from utils.mouse_simulation import simulate_mouse_action
from utils.cookie_management import CookieManager
from utils.sms_services.durian import DurianService
from utils.sms_services.fivesims import FiveSimsService
from utils.sms_services.base_sms_service import SMSServiceFactory
from utils.captcha_bypass import bypass_bot_detection
import pyautogui

class App:
    def __init__(self):
        self.config_loader = ConfigLoader()
        self.proxy_manager = ProxyManager()
        self.cookie_manager = CookieManager()
        self.sms_service_factory = SMSServiceFactory()
        self.settings = self.config_loader.load_settings()
        self.proxy_settings = self.proxy_manager.load_proxy_settings()
        self.mouse_simulator = simulate_mouse_action
        self.captcha_bypass = bypass_bot_detection

    def add_phone_number(self, phone_number=None):
        if phone_number:
            self.settings['phone_number'] = phone_number
        else:
            self.settings.pop('phone_number', None)

    def setup_sms_service(self):
        service_name = self.settings.get('sms_service', 'durian')
        if service_name == 'durian':
            self.sms_service = DurianService()
        elif service_name == '5sims':
            self.sms_service = FiveSimsService()
        else:
            raise ValueError(f"Unsupported SMS service: {service_name}")

    def run(self):
        # Proxy setup
        if self.proxy_settings:
            self.proxy_manager.setup_proxy(self.proxy_settings)

        # Simulate mouse action
        self.mouse_simulator()

        # Manage cookies
        self.cookie_manager.load_cookies()
        
        # Setup SMS service
        self.setup_sms_service()

        # Add recovery email if specified
        recovery_email = self.settings.get('recovery_email')
        if recovery_email:
            # Code to add recovery email goes here
            pass

        # Bypass bot detection
        self.captcha_bypass()

        # Main logic of the app
        # ...

if __name__ == "__main__":
    app = App()
    app.run()
```