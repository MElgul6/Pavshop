from django.test import TestCase
from Core.models import Contact,Subscriber,Team


class TestCartModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data1={
            'fullname':'leyla',
            'email':'no',
            'phone':'059211',
            'subject':'problem',
            'message':'no access',
            # 'created_at':'01/05/2022',
            # 'updated_at':'05/05/2022'
        }
        cls.contact= Contact.objects.create(**cls.data1)
        
        
        
        
    
    def test_created_data(self):
        contact=Contact.objects.first()
        
        self.assertEqual(contact.fullname, self.data1['fullname'])
       
        

    # def test_str_method(self):
    #     self.assertEqual(str(self.contact), self.data1['fullname'])
    #     self.assertEqual(str(self.billing), self.data2['card_number'])
    #     self.assertEqual(str(self.shipping), self.data3['first_name'])


    @classmethod
    def tearDownClass(cls):
        Contact.objects.first().delete()
        del cls.contact
        del cls.data1
       



class TestCoreModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data1={
            'email':'leyla@gmail.com',
            'is_active':True,
            'created_at':'01/05/2022',
            'updated_at':'05/05/2022'
        }
        cls.subscriber= Subscriber.objects.create(**cls.data1)
        cls.data2={
            'fullname':'leyla',
            'job_title':'analyst',
            'image':'ikunjcda.png',
            'created_at':'01/05/2022',
            'updated_at':'05/05/2022'
        }
        cls.team= Team.objects.create(**cls.data2)
        
        
    
    def test_created_data(self):
        subscriber=Subscriber.objects.first()
        team=Team.objects.first()
        self.assertEqual(subscriber.email, self.data1['email'])
        self.assertEqual(team.fullname, self.data2['fullname'])
      
        

    # def test_str_method(self):
    #     self.assertEqual(str(self.subscriber), self.data1['email'])
    #     self.assertEqual(str(self.team), self.data2['fullname'])
   

    @classmethod
    def tearDownClass(cls):
        Subscriber.objects.first().delete()
        del cls.subscriber
        del cls.data1
        Team.objects.first().delete()
        del cls.team
        del cls.data2