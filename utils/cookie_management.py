```python
import json
import os
from pathlib import Path

class CookieSchema:
    def __init__(self, domain, name, value, path='/', expires=None, http_only=False, secure=False):
        self.domain = domain
        self.name = name
        self.value = value
        self.path = path
        self.expires = expires
        self.http_only = http_only
        self.secure = secure

    def to_dict(self):
        return {
            'domain': self.domain,
            'name': self.name,
            'value': self.value,
            'path': self.path,
            'expires': self.expires,
            'httpOnly': self.http_only,
            'secure': self.secure
        }

class CookieManager:
    def __init__(self, cookie_file='cookies.json'):
        self.cookie_file = Path(cookie_file)
        self.cookies = self._load_cookies()

    def _load_cookies(self):
        if self.cookie_file.exists():
            with open(self.cookie_file, 'r') as file:
                return json.load(file)
        return []

    def _save_cookies(self):
        with open(self.cookie_file, 'w') as file:
            json.dump(self.cookies, file, indent=4)

    def add_cookie(self, cookie):
        if isinstance(cookie, CookieSchema):
            self.cookies.append(cookie.to_dict())
            self._save_cookies()

    def get_cookie(self, name, domain=None):
        for cookie in self.cookies:
            if cookie['name'] == name and (domain is None or cookie['domain'] == domain):
                return cookie
        return None

    def delete_cookie(self, name, domain=None):
        self.cookies = [cookie for cookie in self.cookies if not (cookie['name'] == name and (domain is None or cookie['domain'] == domain))]
        self._save_cookies()

    def clear_cookies(self):
        self.cookies = []
        self._save_cookies()
```