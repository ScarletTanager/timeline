import unittest
import event
import datetime
import actor


class DefaultDatesEventTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.event_name = 'The yuuge event'

    def setUp(self):
        self.event = event.event(DefaultDatesEventTestCase.event_name)

    def test_default_start_date(self):
        self.assertEqual(self.event.start,
                         datetime.date(datetime.MINYEAR, 1, 1))

    def test_default_end_date(self):
        self.assertEqual(self.event.end, datetime.date.today())

    def test_event_name(self):
        self.assertEqual(self.event.name, DefaultDatesEventTestCase.event_name)


class EventWithDatesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.event_name = 'The yuuge event'
        cls.start = datetime.date(1971, 11, 3)
        cls.end = datetime.date(2016, 11, 8)

    def setUp(self):
        self.event = event.event(EventWithDatesTestCase.event_name,
                                 EventWithDatesTestCase.start, EventWithDatesTestCase.end)

    def test_start_date(self):
        self.assertEqual(self.event.start, EventWithDatesTestCase.start)

    def test_end_date(self):
        self.assertEqual(self.event.end, EventWithDatesTestCase.end)

    def test_event_name(self):
        self.assertEqual(self.event.name, EventWithDatesTestCase.event_name)


class EventParticipantsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.event_name = 'Event with participants!'

    def setUp(self):
        self.event = event.event(EventParticipantsTestCase.event_name)
        self.participant = actor.actor('The FBI')
        self.assertNotIn(self.participant, self.event.participants)

    def test_add_invalid_participant(self):
        with self.assertRaises(TypeError):
            self.event.add_participant('not a participant')

    def test_add_participant(self):
        self.event.add_participant(self.participant)
        self.assertIn(self.participant, self.event.participants)


class EventLocationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.event_name = 'Event with participants!'

    def setUp(self):
        self.event = event.event(EventParticipantsTestCase.event_name)
