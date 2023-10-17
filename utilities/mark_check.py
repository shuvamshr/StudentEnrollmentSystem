def grade_check(marks):
    if marks >= 85:
        return "HD"
    elif marks >= 75:
        return "D"
    elif marks >= 65:
        return "C"
    elif marks >= 50:
        return "P"
    else:
        return "F"


def status_check(marks):
    if marks >= 50:
        return "PASS"
    else:
        return "FAIL"
