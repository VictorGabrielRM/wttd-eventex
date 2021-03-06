from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Victor",
            cpf="12345678901",
            email="victorgabryel@hotmail.com",
            phone="6192768940"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """ Subscription must have an auto created_at attr. """
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Victor', str(self.obj))

    def test_paid_default_to_False(self):
        """ By default paid must to be false """
        self.assertEqual(False, self.obj.paid)