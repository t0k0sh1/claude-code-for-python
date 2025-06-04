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

    if not (isinstance(a, (int, float)) and not isinstance(a, bool)) or not (
        isinstance(b, (int, float)) and not isinstance(b, bool)
    ):
        raise ValueError("Arguments must be numeric")

    return a + b
