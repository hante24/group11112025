def is_valid_email(value: str) -> bool:
    if not value:
        return False

    if value.count("@") != 1:
        return False

    local, domain = value.split("@")

    if not local or not domain:
        return False
    if local.startswith(".") or local.endswith("."):
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False

    if "." not in domain:
        return False

    return True


def avg(values: list[float]) -> float:
    if not values:
        raise ValueError("List is empty")

    return sum(values) / len(values)


def uah_to_usd(amount: float, rate: float) -> float:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if rate <= 0:
        raise ValueError("Rate must be positive")

    return amount / rate