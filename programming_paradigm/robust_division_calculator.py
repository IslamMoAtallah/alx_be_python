def safe_divide(numerator, denominator):
    """Safely divides two numbers with error handling."""
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please provide numeric input."
