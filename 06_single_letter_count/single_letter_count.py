def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0
    for x in word:
        if x.lower() == letter.lower():
            count = count + 1
    
    return count

print(single_letter_count("HeLlo World", 'z'))