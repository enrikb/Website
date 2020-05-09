from django.test import TestCase

from .models import Account

class CreateAccountTest(TestCase):

    def setUp(self):
        self.user = Account.objects.create_user('user@mail.com', 'user', 'pwd', 'title', 'first', 'last', 'street',
                                                '1', '12345', 'city', 'de')

    def testBasic(self):
        self.assertEqual(self.user.email, Account.objects.normalize_email('user@mail.com'))
        self.assertEqual(self.user.username, 'user')
        self.assertEqual(self.user.title, 'title')
        self.assertEqual(self.user.first_name, 'first')
        self.assertEqual(self.user.last_name, 'last')
        self.assertEqual(self.user.street, 'street')
        self.assertEqual(self.user.housenumber, '1')
        self.assertEqual(self.user.plz, '12345')
        self.assertEqual(self.user.city, 'city')
        self.assertEqual(self.user.country, 'de')
        # make sure pwd is not saved in plain text
        self.assertNotEqual(self.user.password, 'pwd')
        # make sure that not admin
        assert self.user.is_admin is False

class CreateAdminTest(TestCase):

    def setUp(self):
        self.admin = Account.objects.create_superuser('user@mail.com', 'user', 'pwd', 'title', 'first', 'last', 'street',
                                                '1', '12345', 'city', 'de')

    def testBasic(self):
        assert self.admin.is_admin is True