```python
import pytest
from email_creator.proxy_manager import ProxyManager, ProxyDetails

class TestProxyManager:
    def setup_method(self):
        self.proxy_manager = ProxyManager(PROXY_LIST)

    def test_get_proxy(self):
        proxy = self.proxy_manager.get_proxy()
        assert isinstance(proxy, ProxyDetails), "get_proxy should return an instance of ProxyDetails"

    def test_proxy_format(self):
        proxy = self.proxy_manager.get_proxy()
        assert all(hasattr(proxy, attr) for attr in ['ip', 'port', 'username', 'password']), \
            "ProxyDetails should have ip, port, username, and password attributes"

    def test_proxy_rotation(self):
        first_proxy = self.proxy_manager.get_proxy()
        second_proxy = self.proxy_manager.get_proxy()
        assert first_proxy != second_proxy, "get_proxy should rotate proxies and not return the same one consecutively"

    def test_proxy_list_exhaustion(self):
        for _ in range(len(PROXY_LIST)):
            self.proxy_manager.get_proxy()
        with pytest.raises(IndexError):
            self.proxy_manager.get_proxy(), "get_proxy should raise IndexError when all proxies have been used"

    def test_proxy_replenish(self):
        for _ in range(len(PROXY_LIST)):
            self.proxy_manager.get_proxy()
        self.proxy_manager.replenish_proxies()
        assert self.proxy_manager.get_proxy(), "After replenishing, get_proxy should return a proxy"

    def test_proxy_removal(self):
        initial_proxy = self.proxy_manager.get_proxy()
        self.proxy_manager.remove_proxy(initial_proxy)
        assert initial_proxy not in self.proxy_manager.proxies, "remove_proxy should remove the specified proxy from the list"

    def test_proxy_removal_with_replenish(self):
        initial_proxy = self.proxy_manager.get_proxy()
        self.proxy_manager.remove_proxy(initial_proxy)
        self.proxy_manager.replenish_proxies()
        assert initial_proxy not in self.proxy_manager.proxies, \
            "After replenishing, removed proxy should not reappear in the list"

# Shared dependencies and constants
PROXY_LIST = [
    ProxyDetails(ip='192.168.1.1', port=8080, username='user1', password='pass1'),
    ProxyDetails(ip='192.168.1.2', port=8080, username='user2', password='pass2'),
    # Add more proxies as needed
]
```