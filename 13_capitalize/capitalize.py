def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    s = ''
    for num in range(len(phrase)):
        if num == 0:
            s += phrase[num].upper()
        else:
            s += phrase[num]
    return s
print(capitalize('only first word'))