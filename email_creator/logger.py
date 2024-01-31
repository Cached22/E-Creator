```python
import logging
import os
from datetime import datetime

# Define the format for the logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# Create a directory for logs if it doesn't exist
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Define the filename for the log file with a timestamp
log_filename = datetime.now().strftime(f"{log_directory}/email_creator_%Y-%m-%d_%H%M%S.log")

# Configure the logger
logging.basicConfig(filename=log_filename,
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')

# Create a logger object
logger = logging.getLogger()

def log_event(message, level=logging.INFO):
    """
    Log an event at the specified level.
    :param message: The message to log.
    :param level: The logging level (e.g., logging.INFO, logging.ERROR).
    """
    if level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.INFO:
        logger.info(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.CRITICAL:
        logger.critical(message)
    else:
        logger.info(message)  # Default to INFO level if level is unspecified

# Example usage:
# log_event("This is an info message")
# log_event("This is a warning message", level=logging.WARNING)
# log_event("This is an error message", level=logging.ERROR)
```