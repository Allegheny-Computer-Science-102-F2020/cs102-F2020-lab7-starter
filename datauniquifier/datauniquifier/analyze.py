"""Analyze the results from the uniquification process."""


def format_bytes(size):
    """Format an output value in bytes in a human-readable fashion."""
    # Reference:
    # https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778
    power = 2 ** 10
    n = 0
    power_labels = {0: "", 1: "kilo", 2: "mega", 3: "giga", 4: "tera"}
    while size > power:
        size /= power
        n += 1
    return str(size) + " " + power_labels[n] + "bytes"


def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    # TODO: See the README file for how to calculate the reduction


def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    # TODO: See the README file for how to calculate percent reduction
