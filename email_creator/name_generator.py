```python
import random
import string

def generate_name(length=6):
    """
    Generates a random name for the email account. The name will not contain numbers
    to meet the requirement of the application.

    :param length: The length of the generated name, default is 6 characters.
    :return: A string representing the generated name.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

if __name__ == "__main__":
    # Example usage
    print(generate_name())
```