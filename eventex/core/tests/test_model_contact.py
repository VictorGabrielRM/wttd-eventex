from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                        value='henrique@bastos.net')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE,
                                        value='5555-5555')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='b')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        self.assertEqual('henrique@bastos.net', str(contact))


class ContactManageTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Victor Gabriel',
            slug='victor-gabriel',
            website='http://vgr.link/vg-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='victorgabryel@hotmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='61-9276-8940')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['victorgabryel@hotmail.com']

        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['61-9276-8940']

        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
