def even_squares(numbers):
    return {number: number**2 for number in numbers if number % 2 == 0}


if __name__ == "__main__":
    print(even_squares([-2, -1, 0, 1, 2]))
