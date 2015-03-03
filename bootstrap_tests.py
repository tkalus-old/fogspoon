# -*- coding: utf-8 -*-

from collections import namedtuple
from unittest import TestCase

from bootstrap_db import LocationNormalfier

class LocationNormalfierTestCase(TestCase):

    def test_location_range(self):
        TestData = namedtuple('TestData', ['location', 'expected'])
        test_data = [
            TestData(location=u'Café Trieste',
                     expected=(u'Café Trieste',)),

            TestData(location=u'2000 Folsom',
                     expected=(u'2000 Folsom',)),

            TestData(location=u'2413 Harrison St.',
                     expected=(u'2413 Harrison St.',)),

            TestData(location=u"Starbucks at 333 O'Farrell St.",
                     expected=(u"333 O'Farrell St.",)),

            TestData(location=u'24th and Church St. ',
                     expected=(u'24th and Church St.',)),

            TestData(location=u'24th & Church St. ',
                     expected=(u'24th and Church St.',)),
            TestData(location=u'Pier 7',
                     expected=(u'Pier 7',)),

            TestData(location=u'1298 Sacramento Street at Jones',
                     expected=(u'1298 Sacramento Street',)),

            TestData(location=u'at 820 Mission',
                     expected=(u'820 Mission',)),

            TestData(location=u'near Potrero and Cesar Chavez Streets',
                     expected=(u'Potrero Street and Cesar Chavez Street',)),

            TestData(location=u'Corner of Van Ness & Mission Street',
                     expected=(u'Van Ness and Mission Street',)),

            TestData(location=u'Mark Hopkins Intercontinental Hotel (1 Nob Hill Circle, Nob Hill)',
                     expected=(u'1 Nob Hill Circle',)),

            TestData(location=u"McDonald's Restaurant (701 3rd Street, SOMA)",
                     expected=(u'701 3rd Street',)),

            TestData(location=u'Leavenworth from Filbert & Francisco St',
                     expected=(u'Leavenworth and Filbert',
                               u'Leavenworth and Francisco St',)),

            TestData(location=u'Lombard Street between Hyde & Leavenworth',
                     expected=(u'Lombard Street and Hyde',
                               u'Lombard Street and Leavenworth',)),

            TestData(location=u'Off Bush Street, between Powell and Stockton Streets',
                     expected=(u'Bush Street and Powell Street',
                               u'Bush Street and Stockton Street',)),

            TestData(location=u'23rd & Iowa Streets (Dogpatch)',
                     expected=(u'23rd Street and Iowa Street',)),
        ]
        for td in test_data:
            self.assertEqual(td.expected, LocationNormalfier(td.location).normalfy)
