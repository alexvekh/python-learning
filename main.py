def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0:
        return False

    pin_set = set()
    for pin in pin_codes:
        if not isinstance(pin, str):
            return False
        if len(pin) != 4:
            return False
        try:
            int(pin)
        except ValueError:
            return False
        if pin in pin_set:
            return False
        else:
            pin_set.add(pin)
    else:
        return True
print(is_valid_pin_codes(['1101', '9034', '0011']))