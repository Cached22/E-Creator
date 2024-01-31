```python
from pydantic import BaseModel, EmailStr, validator

class SettingsSchema(BaseModel):
    use_proxy: bool
    proxy_url: str = None
    use_mouse_simulation: bool
    use_cookie_management: bool
    recovery_email: EmailStr = None
    use_sms_service: bool
    sms_service_name: str = None
    phone_number: str = None
    bypass_bot_detection: bool

    @validator('proxy_url', always=True)
    def check_proxy_url(cls, v, values, **kwargs):
        if values.get('use_proxy') and not v:
            raise ValueError('Proxy URL must be provided if use_proxy is enabled')
        return v

    @validator('sms_service_name', always=True)
    def check_sms_service_name(cls, v, values, **kwargs):
        if values.get('use_sms_service') and not v:
            raise ValueError('SMS service name must be provided if use_sms_service is enabled')
        return v

    @validator('phone_number')
    def check_phone_number_format(cls, v):
        if v and not v.isdigit():
            raise ValueError('Phone number must contain only digits')
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
```