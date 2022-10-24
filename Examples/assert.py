# Example
# Test if a condition returns True:

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
def test_assert():
    assert x == "goodbye"
    
# test_assert()


"""Definition and Usage
The assert keyword is used when debugging code.
The assert keyword lets you test if a condition
in your code returns True, if not,
the program will raise an AssertionError.
"""

#if condition returns False, AssertionError is raised and print: "x should be 'hello'"
def test2_assert():
    assert x == "goodbye", "x should be 'hello'"

# test_assert()


try:
    print("start... 2+2 vs 5")
    assert 2 + 2 == 5
except AssertionError:
    print("must be: 4")
except:
    print("2 + 2 = 4")
