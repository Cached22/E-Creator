```python
from pydantic import BaseModel, validator

class ProxySettingsSchema(BaseModel):
    http_proxy: str = None
    https_proxy: str = None
    ftp_proxy: str = None
    no_proxy: str = None

    @validator('http_proxy', 'https_proxy', 'ftp_proxy', 'no_proxy', pre=True, always=True)
    def validate_proxy(cls, v):
        if v is not None and not v.startswith('http://') and not v.startswith('https://'):
            raise ValueError('Proxy URL must start with http:// or https://')
        return v

    class Config:
        env_prefix = 'proxy_'

def load_proxy_settings() -> ProxySettingsSchema:
    return ProxySettingsSchema()

if __name__ == "__main__":
    # Example usage
    proxy_settings = load_proxy_settings()
    print(f"HTTP Proxy: {proxy_settings.http_proxy}")
    print(f"HTTPS Proxy: {proxy_settings.https_proxy}")
```