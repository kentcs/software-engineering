"""Turn the text typed into a spreadsheet cell into a number."""


def parse(text):
    sign = 1.0
    if text.startswith(("-", "+")):
        if text[0] == "-":
            sign = -1.0
        text = text[1:]
    parts = text.split(".")
    if (len(parts) > 2 or
            not any(parts) or
            any(c < "0" or c > "9" for part in parts for c in part)):
        raise ValueError("Expected digits with an optional decimal point")
    value = 0.0
    place = 0.1
    after_point = False
    for digit in text:
        if digit == ".":
            after_point = True
        elif after_point:
            value += (ord(digit) - ord("0")) * place
            place /= 10
        else:
            value = value * 10 + ord(digit) - ord("0")
    return sign * value
