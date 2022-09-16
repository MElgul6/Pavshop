from django.test import TestCase
from Product.models import Product
from Product.models import Product_image
from Product.models import Wish_list
from Product.models import Review
# Create your tests here.
class TestProductModel(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'product_name':'Elgul',
            'price':'211',
            'color':'red',
            'description':'ElgulElgul',
            'is_new':True,
            'is_popular':True,
        }
        cls.Product = Product.objects.create(**cls.data1)
    
    def test_created_data(self):
        product = Product.objects.first()
        self.assertEqual(product.product_name, self.data1['product_name'])
        self.assertEqual(product.price, self.data1['price'])
        self.assertEqual(product.color, self.data1['color'])
        self.assertEqual(product.description, self.data1['description'])
        self.assertEqual(product.is_new, self.data1['is_new'])
        self.assertEqual(product.is_popular, self.data1['is_popular'])
    
    # def test_str_method(self):
    #     self.assertEqual(str(self.Product),self.data1['product_name'])


    @classmethod
    def tearDownClass(cls):
        Product.objects.first().delete()
        del cls.Product
        del cls.data1
    

    @classmethod
    def setUpClass(cls):
        cls.data2 = {
            # 'product_image':'Elgul',
            'product':'211',
            
        }
        cls.Product_image = Product_image.objects.create(**cls.data2)
    
    def test_created_data(self):
        Product_image = Product_image.objects.first()
        # self.assertEqual(Product.product_image, self.data2['product_image'])
        self.assertEqual(Product.product, self.data2['product'])
        

    @classmethod
    def tearDownClass(cls):
        Product_image.objects.first().delete()
        del cls.Product_image
        del cls.data2



    @classmethod
    def setUpClass(cls):
        cls.data3 = {
            # 'Product_id':'123', 
        }
        cls.Wish_list = Wish_list.objects.create(**cls.data3)
    
    def test_created_data(self):
        Wish_list = Wish_list.objects.first()
        # self.assertEqual(Wish_list.Product_id, self.data3['Product_id'])

    @classmethod
    def tearDownClass(cls):
        Wish_list.objects.first().delete()
        del cls.Wish_list
        del cls.data3


    
    @classmethod
    def setUpClass(cls):
        cls.data4 = {
            'full_name':'Elgul', 
            'email':'mehdixanli.elgul@gmail.com',
            'review_text':'Elgulelgul',
            # 'product':'elgul'
        }
        cls.Review = Review.objects.create(**cls.data4)
    
    def test_created_data(self):
        review = Review.objects.first()
        self.assertEqual(review.full_name, self.data4['full_name'])
        self.assertEqual(review.email, self.data4['email'])
        self.assertEqual(review.review_text, self.data4['review_text'])
        # self.assertEqual(Review.product, self.data3['product'])

    @classmethod
    def tearDownClass(cls):
        Review.objects.first().delete()
        del cls.data4

