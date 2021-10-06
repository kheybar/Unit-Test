# pytest fixturs
import pytest
import time
from E6 import Person


class TestPerson():
    # fixturs 
    # setup
    @pytest.fixture
    def setup(self):
        self.p1 = Person('Mahdi', 'Zarepour')
        self.p2 = Person('Rose', 'Ziba')
        # tear down
        yield 'setup'
        time.sleep(1)


    def test_fullname(self, setup):
        assert self.p1.fullname() == 'Mahdi Zarepour'
        assert self.p2.fullname() == 'Rose Ziba'

    def test_email(self, setup):
        assert self.p1.email() == 'MahdiZarepour@gmail.com'
        assert self.p2.email() == 'RoseZiba@gmail.com'
