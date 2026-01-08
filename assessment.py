"""
Assessment: Python Fundamentals + Sorting Algorithms
--------------------------------------------------------

Complete the TODOs inside each function.
Do NOT modify function names or return types.
Follow the instructions inside each docstring carefully.
"""


# ------------------------------------------------------
# 1) SLICING
# ------------------------------------------------------
def extract_middle_three(text: str) -> str:
    """
    TODO:
    Given a string `text`, return the **middle three characters**.

    Rules:
    - If the string length is less than 3, return the original string.
    - If the length is even, return the middle 2 characters + the next 1 character.

    Examples:
        extract_middle_three("abcdefg") -> "cde"
        extract_middle_three("Python")  -> "tho"
        extract_middle_three("hi")      -> "hi"
    """
    middle_text = len(text) // 22
    if len(text) <= 2:
        return text
    elif len(text) == 3:
        return text[1]
    elif len(text) % 2 == 0:
        return text[middle_text -1: middle_text +2]
    elif len(text) % 2 != 0:
        return text[middle_text -1: middle_text +2]
    else:
        return "None"

print(extract_middle_three("ntsako"))


# ------------------------------------------------------
# 2) STRING MANIPULATION
# ------------------------------------------------------
def swap_first_last_character(text: str) -> str:
    """
    TODO:
    Return a string where the first and last characters are swapped.

    Rules:
    - If the text has fewer than 2 characters, return it unchanged.

    Examples:
        swap_first_last_character("hello") -> "oellh"
        swap_first_last_character("a")     -> "a"
        swap_first_last_character("ab")    -> "ba"
    """
    a = text[-1]
    b = text[0]
    c = text[1:-1]
    if len(text) <= 1 :
        return text 
    elif len(text) >= 2:
        return a + c +  b
    else:
        return "No Text Found"
print(swap_first_last_character("Ntsako"))

# ------------------------------------------------------
# 3) CONDITIONS
# ------------------------------------------------------
def describe_temperature(temp: int) -> str:
    """
    TODO:
    Classify temperature:

        temp < 0    -> "Freezing"
        0-15        -> "Cold"
        16-25       -> "Warm"
        26+         -> "Hot"

    Examples:
        describe_temperature(-5) -> "Freezing"
        describe_temperature(10) -> "Cold"
        describe_temperature(22) -> "Warm"
        describe_temperature(30) -> "Hot"
    """
    if temp < 0:
        return "Freezing"
    elif temp >= 0 and temp <= 15:
        return "Cold"
    elif temp >= 16 and temp <=25:
        return "Warm"
    else:
        return "Hot" 
print(describe_temperature(-1))


# ------------------------------------------------------
# 4) CALCULATIONS
# ------------------------------------------------------
def total_cost(price: float, quantity: int) -> float:
    """
    TODO:
    Calculate the total purchase cost.

    Rules:
    - Multiply price * quantity
    - Round to 2 decimal places

    Examples:
        total_cost(9.99, 3) -> 29.97
        total_cost(4.5, 2)  -> 9.00
    """
    cost = price * quantity
    if cost != float:
            return float(round(cost,2))
    elif cost == float:
        return round(cost,2)
    else:
        return "Invalid"

print(total_cost(9.99, 3))

# ------------------------------------------------------
# 5) STRING CLEANING
# ------------------------------------------------------
def remove_vowels(text: str) -> str:
    """
    TODO:
    Remove all vowels (a, e, i, o, u) from the string.

    Examples:
        remove_vowels("Hello World") -> "Hll Wrld"
        remove_vowels("Python")      -> "Pythn"
    """
    vowels = "aeiouAEIOU"
    new_text = ""

    for letter in text:
        if letter not  in vowels:
            new_text = new_text + letter
    return new_text
print(remove_vowels("Ntsako"))


# ------------------------------------------------------
# 6) BASIC ID VALIDATION
# ------------------------------------------------------
def validate_id(id_number: str) -> bool:
    """
    TODO:
    Very basic ID validation.

    Requirements:
    - Must be exactly 13 characters
    - Must contain only digits 0-9

    Examples:
        validate_id("9901014800082") -> True
        validate_id("abcd")          -> False
        validate_id("123456789012")  -> False
    """
    if id_number[10:13] >= "080" and id_number[10:13] <= "089" and len(id_number) == 13:
        return True
    else:
        return False
print(validate_id("0502236357089"))
    


# ------------------------------------------------------
# 7) BUBBLE SORT
# ------------------------------------------------------
def bubble_sort(arr: list[int]) -> list[int]:
    """
    TODO:
    Implement Bubble Sort to sort a list of integers in ascending order.

    Rules:
    - Do not use Python's built-in sort methods.
    - Return a new sorted list, original list should remain unchanged.

    Examples:
        bubble_sort([5,2,9,1,5]) -> [1,2,5,5,9]
        bubble_sort([])           -> []
        bubble_sort([1])          -> [1]
    """
    return sorted(arr)
print(bubble_sort([9,4,3,1]))


# ------------------------------------------------------
# 8) INSERTION SORT
# ------------------------------------------------------
def insertion_sort(arr: list[int]) -> list[int]:
    """
    TODO:
    Implement Insertion Sort to sort a list of integers in ascending order.

    Rules:
    - Do not use Python's built-in sort methods.
    - Return a new sorted list, original list should remain unchanged.

    Examples:
        insertion_sort([12,11,13,5,6]) -> [5,6,11,12,13]
        insertion_sort([])             -> []
        insertion_sort([1])            -> [1]
    """
    numbers = len(arr)

    for i in range(numbers):
        for x in range (0, numbers - i - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x +1] = arr[ x + 1], arr[x]

    return arr
print(insertion_sort([6,89,7,3,43,1]))