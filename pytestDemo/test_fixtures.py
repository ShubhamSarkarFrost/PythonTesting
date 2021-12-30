import pytest
from pytestDemo.test_logging import test_logging

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("This is Fixture Demo 1")

    def test_fixtureDemo2(self):
        print("This is Fixture Demo 2")

    def test_fixtureDemo3(self):
        print("This is Fixture Demo 3")

    def test_fixtureDemo4(self):
        print("This is Fixture Demo 4")
