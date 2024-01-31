# Email Account Creation App

## Overview
This application is designed to automate the process of creating bulk email accounts. It is built with Python and utilizes various libraries to interact with web pages, handle HTTP requests, and parse HTML content. The app aims to streamline the account creation process by using automated name generation and proxy management.

## Features
- Automated bulk email account creation
- Automated name generation for new accounts
- Proxy support for account creation
- Configurable settings for customization
- Command-line interface (CLI) and optional graphical user interface (GUI)
- Comprehensive logging and error handling

## Getting Started

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-repository/email-account-creation-app.git
   ```
2. Navigate to the project directory:
   ```
   cd email-account-creation-app
   ```
3. Set up a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration
- Copy the `.env.example` file to `.env` and fill in the necessary details.
- Modify the `config.py` file to set up your preferred configurations.

### Usage
To start the application, run the `main.py` script:
```
python email_creator/main.py
```

For CLI usage, you can use the `cli.py` module:
```
python ui/cli.py
```

If GUI is implemented, you can start it with:
```
python ui/gui.py
```

## Testing
To run the tests, execute the following command:
```
pytest
```

## Documentation
For detailed setup and usage instructions, please refer to the `docs/setup_instructions.md` and `docs/usage_instructions.md` files.

## Contributing
If you wish to contribute to this project, please read the `docs/contribution_guidelines.md` for the contribution process.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
This project is for educational purposes and should be used in a controlled environment. Please adhere to the terms of service of the email service providers.