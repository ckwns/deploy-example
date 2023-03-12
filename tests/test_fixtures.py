import pytest

# basic test case to add required build checks and statuses
@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1

# project related test cases    
def test_with_fixture1(example_fixture):
    assert example_fixture == 1
