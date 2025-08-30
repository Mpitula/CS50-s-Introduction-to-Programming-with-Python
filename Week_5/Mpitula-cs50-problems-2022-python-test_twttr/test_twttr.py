from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_mixed():
    assert shorten("YouTuBe") == "YTB"

def test_numbers():
    assert shorten("h3ll0") == "h3ll0"

def test_punctuation():
    assert shorten("what?!") == "wht?!"

