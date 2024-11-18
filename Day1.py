
def get_line_number(string):
    digits = list(filter(str.isdigit, string))
    return int(digits[0] + digits[-1])
    
def get_calibration_value(text):
    lines = text.split("\n")
    calibration_values = list(map(get_line_number, lines))
    return sum(calibration_values)
