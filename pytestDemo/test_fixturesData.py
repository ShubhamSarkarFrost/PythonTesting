import pytest
from pytestDemo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self,dataLoad):
        print("Your Email is : " +dataLoad[0])
        print("Your Password is :"+dataLoad[1])

