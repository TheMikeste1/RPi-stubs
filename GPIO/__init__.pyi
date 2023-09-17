from typing import Callable, Sequence

# Edges
HIGH: int = ...
LOW: int = ...

# GPIO pin Modes
IN: int = ...
OUT: int = ...
HARD_PWM: int = ...
SERIAL: int = ...
I2C: int = ...
SPI: int = ...
UNKNOWN: int = ...

# GPIO module modes
BOARD: int = ...
BCM: int = ...

# Pull Up/Down modes
PUD_OFF: int = ...
PUD_UP: int = ...
PUD_DOWN: int = ...

# Edge detection
RISING: int = ...
FALLING: int = ...
BOTH: int = ...

RPI_INFO: dict[str, str | int] = ...

VERSION: str = ...

def setup(
    channel: int | Sequence[int],
    direction: int,
    pull_up_down: int = PUD_OFF,
    initial: int | None = None,
) -> None:
    """
    Set up a GPIO channel or list of channels with a direction and (optional) pull/up down control.

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :param direction: IN or OUT.
    :param pull_up_down: PUD_OFF (default), PUD_UP or PUD_DOWN.
    :param initial: Initial value for an output channel.
    """
    ...

def cleanup(channel: int | Sequence[int] | None = None) -> None:
    """
    Clean up by resetting all GPIO channels that have been used by this program to INPUT with no pullup/pulldown and no event detection.

    :param channel: Individual channel or list/tuple of channels to clean up.  Default - clean every channel that has been used.
    """
    ...

def output(
    channel: int | Sequence[int], value: int | bool | Sequence[int | bool]
) -> None:
    """
    Output to a GPIO channel or list of channels.

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :param value: 0/1 or False/True or LOW/HIGH.
    """
    ...

def input(channel: int) -> int | bool:
    """
    Input from a GPIO channel.  Returns HIGH = 1 = True or LOW = 0 = False.

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :return: 0/1 or False/True or LOW/HIGH.
    """
    ...

def setmode(mode: int) -> None:
    """
    Set up numbering mode to use for channels.

    :param mode: BOARD: Use Raspberry Pi board numbers, or BCM: Use Broadcom GPIO 00..nn numbers.
    """
    ...

def getmode() -> int:
    """
    Get numbering mode used for channel numbers.

    :return: BOARD, BCM or None.
    """
    ...

def add_event_detect(
    channel: int,
    edge: int,
    callback: None | Callable[[int], None] = None,
    bouncetime: int | None = None,
) -> None:
    """
    Enable edge detection events for a particular GPIO channel.

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :param edge: RISING, FALLING or BOTH.
    :param callback: A callback function for the event (optional).
    :param bouncetime: Switch bounce timeout in ms for callback.
    """
    ...

def remove_event_detect(channel: int) -> None:
    """
    Remove edge detection for a particular GPIO channel.

    :param channel: Either board pin number or BCM number depending on which mode is set.
    """
    ...

def event_detected(channel: int) -> bool:
    """
    Returns True if an edge has occurred on a given GPIO.  You need to enable edge detection using add_event_detect() first.

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :return: True if an event occurred.
    """
    ...

def add_event_callback(
    channel: int, callback: Callable[[int], None], bouncetime: int | None = None
) -> None:
    """
    Add a callback for an event already defined using add_event_detect().

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :param callback: A callback function.
    :param bouncetime: Time allowed between calls to allow for switchbounce
    """
    ...

def wait_for_edge(
    channel: int, edge: int, bouncetime: int | None = None, timeout: int | None = None
) -> int | None:
    """
    Wait for an edge.  Returns the channel number or None on timeout.

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :param edge: RISING, FALLING or BOTH
    :param bouncetime: Time allowed between calls to allow for switchbounce
    :param timeout: Timeout in ms
    :return: Channel number or None on timeout
    """
    ...

def gpio_function(channel: int) -> int:
    """
    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI).

    :param channel: Either board pin number or BCM number depending on which mode is set.
    :return: GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI).
    """
    ...

def setwarnings(state: bool) -> None:
    """
    Enable or disable warning messages.

    :param state: True to enable warnings, False to disable.
    """
    ...

class PWM:
    """
    Pulse Width Modulation class.
    """

    def __init__(self, channel: int, frequency: float) -> None:
        """
        Create a new PWM object.

        :param channel: Either board pin number or BCM number depending on which mode is set.
        :param frequency: Frequency in Hz.
        """
        ...
    def start(self, dutycycle: float) -> None:
        """
        Start software PWM.

        :param dutycycle: Duty cycle (0.0 to 100.0).
        """
        ...
    def ChangeFrequency(self, frequency: float) -> None:
        """
        Change the frequency.

        :param frequency: Frequency in Hz.
        """
        ...
    def ChangeDutyCycle(self, dutycycle: float) -> None:
        """
        Change the duty cycle.

        :param dutycycle: Duty cycle (0.0 to 100.0).
        """
        ...
    def stop(self) -> None:
        """
        Stop software PWM.
        """
        ...
