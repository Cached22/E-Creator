```python
from .cli import main as cli_main
from .gui import main as gui_main

def start_interface(mode='cli'):
    """
    Start the user interface based on the selected mode.
    
    :param mode: The mode of the user interface to start ('cli' or 'gui').
    """
    if mode == 'cli':
        cli_main()
    elif mode == 'gui':
        gui_main()
    else:
        raise ValueError("Invalid mode selected. Choose 'cli' or 'gui'.")
```