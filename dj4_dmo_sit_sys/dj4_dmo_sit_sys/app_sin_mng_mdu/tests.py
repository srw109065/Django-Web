from django.test import TestCase
from django.test import client
from django.contrib.auth.models import User


# Create your tests here.
class TestCaseDoSignin(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="abc",
            password="123"
        )

        self.user = User.objects.get(username="abc")
        self.client = client.Client()

    def tearDown(self):
        User.objects.all().delete()

    def test_go_signin_page(self):
        response = self.client.get(path="/go_signin_page/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "acc_sig_pge.html")

    def test_do_signin(self):
        response = self.client.post(
            path="/do_signin/",
            data={"username": "abc", "password": "123"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/go_ord_mng_page/")

