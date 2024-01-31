import pyautogui
import random
import time

def simulate_mouse_action(start_pos, end_pos, duration=1.0):
    """
    Simulates a mouse action from start_pos to end_pos over the specified duration.
    The movement includes some randomness to mimic human-like cursor movement.

    :param start_pos: Tuple (x, y) as the starting position of the mouse.
    :param end_pos: Tuple (x, y) as the ending position of the mouse.
    :param duration: Float, the time taken to move the mouse from start to end.
    """
    pyautogui.moveTo(start_pos[0], start_pos[1], duration=0.0)  # Instantly move to start position

    # Calculate the number of steps
    steps = int(duration * 100)
    step_duration = duration / steps

    # Calculate step-wise x and y increments
    x_increment = (end_pos[0] - start_pos[0]) / steps
    y_increment = (end_pos[1] - start_pos[1]) / steps

    for step in range(steps):
        # Add some randomness to each step
        x_jitter = random.uniform(-0.5, 0.5)
        y_jitter = random.uniform(-0.5, 0.5)

        # Calculate next position
        next_x = start_pos[0] + (step * x_increment) + x_jitter
        next_y = start_pos[1] + (step * y_increment) + y_jitter

        # Move to the next position
        pyautogui.moveTo(next_x, next_y, duration=step_duration)

    # Ensure the cursor ends exactly at the end_pos
    pyautogui.moveTo(end_pos[0], end_pos[1], duration=0.0)

def simulate_click(position, clicks=1, interval=0.25, button='left'):
    """
    Simulates a mouse click at the specified position.

    :param position: Tuple (x, y) as the position to click.
    :param clicks: Integer, the number of times to click.
    :param interval: Float, the time between clicks.
    :param button: String, the button to click, either 'left' or 'right'.
    """
    pyautogui.click(position[0], position[1], clicks=clicks, interval=interval, button=button)

def simulate_random_movement(duration=5.0):
    """
    Simulates random mouse movement for a specified duration.

    :param duration: Float, the time during which the mouse will move randomly.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        # Generate a random position on the screen
        screen_width, screen_height = pyautogui.size()
        random_pos = (random.randint(0, screen_width), random.randint(0, screen_height))

        # Move to the random position
        simulate_mouse_action(pyautogui.position(), random_pos, duration=random.uniform(0.5, 1.5))