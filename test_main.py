from main import add
def test_add_digits():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_add_strings():
    assert add('Hello', 'World') == 'HelloWorld'
    assert add('Hello', ' World') == 'Hello World'
    assert add('Hello', ' World!') == 'Hello World!'

def test_add_mixed_negative1():
    assert add('Hello', -1) == 'Hello1'

def test_add_mixed_negative2():
    assert add(1, 'Hello') == '1Hello'