import datetime
import actor
import unittest


class ActorTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actor_name = 'Great Cthulhu'

    def setUp(self):
        self.actor = actor.actor(ActorTestCase.actor_name)

    def test_actor_name(self):
        self.assertEqual(self.actor.name, ActorTestCase.actor_name)


class PersonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actor_name = 'Grigori Rasputin'
        cls.born = datetime.date(1869, 1, 21)
        cls.died = datetime.date(1916, 12, 30)

    def setUp(self):
        self.actor = actor.person(
            PersonTestCase.actor_name, PersonTestCase.born, PersonTestCase.died)

    def test_born(self):
        self.assertEqual(self.actor.born, PersonTestCase.born)

    def test_died(self):
        self.assertEqual(self.actor.died, PersonTestCase.died)

    def test_actor_name(self):
        self.assertEqual(self.actor.name, PersonTestCase.actor_name)

    def test_living(self):
        self.assertFalse(self.actor.is_living())


class InvalidInitTestCase(unittest.TestCase):
    def test_invalid_born(self):
        with self.assertRaises(TypeError):
            self.actor = actor.person('foo', 'bar')

    def test_invalid_died(self):
        with self.assertRaises(TypeError):
            self.actor = actor.person('foo', datetime.date.today(), 'bar')


class LivingPersonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actor_name = 'Joe Rando'
        cls.born = datetime.date(1980, 6, 6)

    def setUp(self):
        self.actor = actor.person(
            LivingPersonTestCase.actor_name, LivingPersonTestCase.born)

    def test_born(self):
        self.assertEqual(self.actor.born, LivingPersonTestCase.born)

    def test_actor_name(self):
        self.assertEqual(self.actor.name, LivingPersonTestCase.actor_name)

    def test_living(self):
        self.assertTrue(self.actor.is_living())
