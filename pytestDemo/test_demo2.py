# command to run Test Cases = py.test
# run specific file py.test testcasename.py
# for detailed report add - v example py.test testcasename.py -v
# for console output add -s example
# for method level execution ass - k
#py.test -m smoke -v -s - to run groups
#@pytest.mark.skip to skip the test case

import pytest


@pytest.mark.smoke
def test_whoisthis():
    print("This is Drimitriv No1 russian Hacker")

@pytest.mark.skip
def test_CreditCard():

    age = int(input("Enter Your Age , Customer !!!"))
    if(age >= 18):
        print("You are provided with the Credit Card")
    else:
        print("You Get Shit , Go and Piss Off!!!")



def test_fixturesdata(setup):
    print("I am Executed after the first executed fixture")