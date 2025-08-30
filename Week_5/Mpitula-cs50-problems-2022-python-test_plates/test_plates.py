from plates import is_valid

def test_length():
    # Too short or too long
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    # Valid length within 2–6
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True

def test_starting_letters():
    # Must start with two letters
    assert is_valid("1ABC") == False
    assert is_valid("A1BC") == False
    assert is_valid("AB123") == True

def test_numbers():
    # Numbers must be at the end
    assert is_valid("AB12C") == False
    assert is_valid("ABC1D") == False
    # First number can’t be 0
    assert is_valid("AB012") == False
    # Valid number section
    assert is_valid("AB123") == True

def test_alphanumeric():
    # No punctuation, spaces, or special characters
    assert is_valid("AB 12") == False
    assert is_valid("AB!23") == False
    assert is_valid("AB@C") == False
    assert is_valid("ABC123") == True

def test_edge_cases():
    # Just letters
    assert is_valid("ABC") == True
    # Just letters up to 6
    assert is_valid("ABCDEF") == True
    # Letters + numbers valid
    assert is_valid("XY99") == True

