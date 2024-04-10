from UnitTest.main import Person, ff
from unittest.mock import patch, MagicMock


class PatchedPerson:
    def __init__(self):
        self.name = "Evgeny"
        self.age = 32

    def print_age(self):
        return self.age

@patch("UnitTest.main.Person")
def test_ff(Person_mock):
    Person_mock_ = MagicMock()
    Person_mock_.name = "Evgeny"
    Person_mock_.print_age.return_value = 32
    Person_mock.return_value = Person_mock_
    ff()