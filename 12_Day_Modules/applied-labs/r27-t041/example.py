def celsius_to_fahrenheit(celsius):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return celsius * 9 / 5 + 32


def main():
    """The CLI. Only this function reads input or prints."""
    celsius = float(input("Celsius: "))
    print(f"{celsius:g} C = {celsius_to_fahrenheit(celsius):g} F")


if __name__ == "__main__":  # main guard: runs only when executed directly
    main()