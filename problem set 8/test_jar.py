# Problem Set 8 Question 2
# To create a Jar class and implement cookie related methods

# Importing pytest and "Jar" class to test
import pytest
from jar import Jar

# To test for correct initialization
def test_init():
    jar = Jar()
    assert jar.capacity == 12

#To test for correct number of cookies outputted
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪"

# To test for correct size of deposits
def test_deposit():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(200)

# To test for correct size of withdrawals
def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(100)