import unittest


class Base(unittest.TestCase):

    def setUp(self):
        print 'in'
        self.a = 1

    def tearDown(self):
        print 'go out'
        self.a = 0

class TestClass(Base):
    def test_1(self):

        x = 'tis'

        assert 'i' in x
        assert 0 == self.a

    def test_2(self):

        x = 'tis'

        assert 'i' in x
        assert 0 == self.a
