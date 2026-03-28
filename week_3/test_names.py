from names import make_full_name, extract_family_name, extract_given_name
from address import extract_city
import pytest

def test_make_full_name():
    """
    Tests the make make_full_name function by using assert function
    Parameter: N/A
    Return: N/A
    """
    assert make_full_name("Sally", "Brown") == "Brown; Sally"

def test_extract_family_name():
    """
    Tests the make extract_family_name function by using assert function
    Parameter: N/A
    Return: N/A
    """
    assert extract_family_name("Brown; Sally") == "Brown"
    
def test_extract_given_name():
    """
    Tests the make extract_given_name function by using assert function
    Parameter: N/A
    Return: N/A
    """
    assert extract_given_name("Brown; Sally") == "Sally"

def test_extract_city():
    """
    Tests the make extract_city function by using assert function
    Parameter: N/A
    Return: N/A
    """
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"

pytest.main(["-v", "--tb=line", "-rN", __file__])