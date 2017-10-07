from destryseuler import p1

def test_p1_answer():
    assert p1.answer(10) == 23

def test_brute():
    assert p1.natural_3and5_brute(10) == 23

def test_lambda():
    assert p1.natural_3and5_lambda(10) == 23
    assert p1.natural_3and5_lambda(1000) == 233168
