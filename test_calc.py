def multiply(a, b):
    return a * b


def test_multiply_number():
    a = 5
    b = 8
    expected = 40
    print(f'Wartości {a=} {b=} {expected=}')
    # assert multiply(a, b) == 40
    assert multiply(a, b) == expected, f'Expected {expected}'


class TestNumbers:
    def test_int_float(self):
        assert 1 == 1.0
