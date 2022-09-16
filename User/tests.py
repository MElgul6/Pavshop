from django.test import TestCase
from User.models import User


class TestUserModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data1={
            'first_name':'leyla',
            'last_name':'abilzade',
            'email':'leyla@gmail.com',
            'phone' :'1234567',
            'password' :'1234',
            'addres1' :'baku',
            'addres2' :'baku',
            'country':'azerbaijan',
            'city' :'baku',
            'main_image' :'main.png'
        }
        cls.user= User.objects.create(**cls.data1)
       
 
    
    def test_created_data(self):
        user=User.objects.first()
        self.assertEqual(user.first_name, self.data1['first_name'])
       
        
    # def test_str_method(self):
    #     self.assertEqual(str(self.user), self.data1['first_name'])
        

    @classmethod
    def tearDownClass(cls):
        User.objects.first().delete()
        del cls.user
        del cls.data1