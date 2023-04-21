"""
    This is a unit test function that tests the count function from the um module with an empty string
    input.
    """

from um import count
    


def test_count_empty_string():
    assert count("") == 0