def is_palindrome(s):
    """Check whether a string reads the same forwards and backwards.

    :param s: The string to check.
    :type s: str
    :return: True if ``s`` is a palindrome, otherwise False.
    :rtype: bool
    """
    return s == s[::-1]


def count_words(text):
    """Count the whitespace-separated words in a text string.

    :param text: The text whose words should be counted.
    :type text: str
    :return: The total number of words in ``text``.
    :rtype: int
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    :param c: The temperature in degrees Celsius.
    :type c: int or float
    :return: The equivalent temperature in degrees Fahrenheit.
    :rtype: float
    """
    return (c * 9 / 5) + 32
