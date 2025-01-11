def ask_user_input_int(msg: str, error_handling: bool = True) -> int:
    """
    Prompt the user to input an integer.

    Parameters:
    -----------
    msg : str
        The message to display to the user.
    error_handling : bool, optional
        Flag to indicate if error handling should be used (default is True).

    Returns:
    --------
    int
        The integer input by the user.
    """
    if error_handling:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("Invalid input")
            return ask_user_input_int(msg, error_handling)
    else:
        return int(input(msg))

def ask_user_input_num(msg: str, error_handling: bool = True) -> float:
    """
    Prompt the user to input a floating number.

    Parameters:
    -----------
    msg : str
        The message to display to the user.
    error_handling : bool, optional
        Flag to indicate if error handling should be used (default is True).

    Returns:
    --------
    float
        The floating number input by the user.
    """
    if error_handling:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("Invalid input")
            return ask_user_input_num(msg, error_handling)
    else:
        return float(input(msg))

def print_in_one_line(contents_to_print: list[str], delimiter: str = " ") -> None:
    """
    Print the contents of a list in one line separated by a delimiter.

    Args:
        contents_to_print (list[str]): The list of strings to print.
        delimiter (str): The delimiter to separate the strings. Default is a space.
    """
    print(delimiter.join(contents_to_print))

def convert_list_to_a_string(contents_to_print: list[str], delimiter: str = " ") -> str:
    """
    Return the contents of a list in one line separated by a delimiter.

    Args:
        contents_to_print (list[str]): The list of strings to print.
        delimiter (str): The delimiter to separate the strings. Default is a space.
    """
    return (delimiter.join(contents_to_print))

def test() -> None:
    """Test function for the tool."""
    #print_with_delimiter("Enter an integer", "*")
    contacts = []
    contacts.append("Kim")
    contacts.append("John")
    contacts.append("Denise")
    print_in_one_line(contacts)
    print_in_one_line(contacts, ">.")
    line_of_contacts = convert_list_to_a_string(contacts)
    print(f"Line of contacts: {line_of_contacts}")
    #print(contacts)
    #print(contacts, sep=", ")
    #print(contacts, end=" ")
    #print(" ".join(contacts))
    #values = [1, 2, 3, 4, 5]
    #values = [1, 2, 3, 4, 5]
    #print(' '.join(map(str, values)))

    #for value in values:
    #    print(value, end='@')


if __name__ == "__main__":
    test()