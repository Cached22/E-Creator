```python
import random
from email_creator.config import PROXY_LIST

class ProxyManager:
    def __init__(self):
        self.proxy_list = PROXY_LIST
        self.used_proxies = set()

    def get_proxy(self):
        """
        Retrieves an unused proxy from the proxy list.
        If all proxies are used, it resets the list and starts over.
        """
        available_proxies = [proxy for proxy in self.proxy_list if proxy not in self.used_proxies]
        if not available_proxies:
            self.used_proxies.clear()
            available_proxies = self.proxy_list

        selected_proxy = random.choice(available_proxies)
        self.used_proxies.add(selected_proxy)
        return selected_proxy

    def format_proxy(self, proxy_details):
        """
        Formats the proxy details into a dictionary suitable for requests or Selenium.
        """
        proxy_format = {
            'http': f"http://{proxy_details['username']}:{proxy_details['password']}@{proxy_details['ip']}:{proxy_details['port']}",
            'https': f"https://{proxy_details['username']}:{proxy_details['password']}@{proxy_details['ip']}:{proxy_details['port']}"
        }
        return proxy_format

    def remove_proxy(self, proxy):
        """
        Removes a proxy from the used list, typically done if the proxy is not working.
        """
        if proxy in self.used_proxies:
            self.used_proxies.remove(proxy)

# Example usage:
# proxy_manager = ProxyManager()
# proxy = proxy_manager.get_proxy()
# formatted_proxy = proxy_manager.format_proxy(proxy)
# print(formatted_proxy)
```