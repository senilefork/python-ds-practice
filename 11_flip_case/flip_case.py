def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    s = ''
    to_swap = to_swap.lower()

    for letter in phrase:
        if letter.lower() == to_swap:
            s += letter.swapcase()
        else:
            s += letter
    return s

print( flip_case('Aaaahhh', 'A'))
