def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)

    return has_digit and has_upper and has_lower


def has_duplicates(your_list: list[int | float | str | bool]) -> bool:
    return len(your_list) != len(set(your_list))


def is_warm_outside(temp_celsius: float) -> bool:
    return temp_celsius > 20


print(is_strong_password("Qwerty123"))
print(has_duplicates([1, 2, 3, 3]))
print(is_warm_outside(25))



