from django.test import TestCase
from Cart.models import Billing_details,Shipping_info
from User.models import User

class TestCartModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        # cls.data1={
        #     'fullname':'leyla',
        #     'email':'no',
        #     'phone':'059211',
        #     'subject':'problem',
        #     'message':'no access',
        #     # 'created_at':'01/05/2022',
        #     # 'updated_at':'05/05/2022'
        # }
        # cls.contact= Contact.objects.create(**cls.data1)
        cls.data2={
            'card_number':'123456789000',
            # 'expire_date':'23/12/2025',
            'card_type':'master',
            'card_owner':'leyla',
            # 'user_id': User.objects.first(),
            # 'created_at':'01/05/2022',
            # 'updated_at':'05/05/2022'
        }
        cls.billing= Billing_details.objects.create(**cls.data2)
        cls.data3={
            'first_name':'leyla',
            'last_name': 'recipe.png',
            'company':'bank',
            'address':'baku',
            'city':'baku',
            'country':'Azerbaijan',
            'email':'leyla@gmail.com',
            'phone' :'12345',
            # 'billing_id':'01',
            # 'user_id':'01',
            # 'created_at':'01/05/2022',
            # 'updated_at':'05/05/2022'
        }
        cls.shipping= Shipping_info.objects.create(**cls.data3)
        
    
    def test_created_data(self):
        # contact=Contact.objects.first()
        billing=Billing_details.objects.first()
        shipping=Shipping_info.objects.first()
        # self.assertEqual(contact.fullname, self.data1['fullname'])
        self.assertEqual(billing.card_number, self.data2['card_number'])
        self.assertEqual(shipping.first_name, self.data3['first_name'])
        

    # def test_str_method(self):
    #     self.assertEqual(str(self.contact), self.data1['fullname'])
    #     self.assertEqual(str(self.billing), self.data2['card_number'])
    #     self.assertEqual(str(self.shipping), self.data3['first_name'])


    @classmethod
    def tearDownClass(cls):
        # Contact.objects.first().delete()
        # del cls.contact
        # del cls.data1
        Billing_details.objects.first().delete()
        del cls.billing
        del cls.data2
        Shipping_info.objects.first().delete()
        del cls.shipping
        del cls.data3