import pytest


@pytest.fixture()
def setup():
    print("I will be executing First")
    yield
    print("I am executed at last")


@pytest.fixture()
def dataLoad():
    print("User Profile To Load Data")
    return ["shubhampandora123@gmail.com", "IFuckYou@23"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
