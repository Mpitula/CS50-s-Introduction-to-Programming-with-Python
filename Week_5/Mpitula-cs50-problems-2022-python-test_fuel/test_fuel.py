from fuel import gauge, convert

def test_E():
    assert gauge(convert("0/4")) == "E"
    assert gauge(convert("0/1")) == "E"
def test_F():
    assert gauge(convert("4/4")) == "F"
    assert gauge(convert("2/2")) == "F"

def test_otherwise():
    assert gauge(convert("3/4")) == "75%"
    assert gauge(convert("1/4")) == "25%"

