# Any Pytest File starts with 'test_' , do not start the python file with anything else
# write any code within function (Test Method) which starts with 'test' keyword
# to get the HTML Report ---> py.test -v -s --html=reports.html
import pytest

@pytest.mark.xfail
def test_firstProgram():
     print("Hello , I am the Russian Hacker , i come to your House with Kalashnikov")


@pytest.mark.smoke
def test_secondProgram():
     print("Remmember my voice")
     voice = 'true'
     assert voice == 'true'


def test_crossBrowser(crossBrowser):
     print(crossBrowser)
