from django.test import TestCase
from django.test import client
from .models import Order, Item


# Create your tests here.
class TestCaseDoShowOrderDetail(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            username="abc",
            first_name="bc",
            last_name="a",
            order_num="123",
            total_expenses=500.0
        )
        self.order_id = self.order.id

        self.item = Item.objects.create(
            order=self.order,
            item_name="Candy",
            purchase_number=1
        )

        self.client = client.Client()

    def tearDown(self):
        Order.objects.all().delete()

    def test_do_show_order_detail(self):
        response = self.client.post(
            path="/do_show_order_detail/",
            data={"orderId": self.order_id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Candy")

    def test_do_del_order(self):
        response = self.client.post(
            path="/do_del_order/",
            data={"orderId": self.order_id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ord_mng_pge.html")

