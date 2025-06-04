def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Raises:
        ValueError: If a or b is not a number or is None
    """
    if a is None or b is None:
        raise ValueError("Arguments cannot be None")

    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("Arguments must be numeric")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Arguments must be numeric")

    return a + b
