from django.test import TestCase
from Blog.models import Category,Tag,Blog,Comment

class TestBlogModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data1={
            'title':'chair',
            'image':'chair.png',
            'created_at':'01/05/2022',
            'updated_at':'05/05/2022'
        }
        cls.category= Category.objects.create(**cls.data1)
        cls.data2={
            'title':'tag1',
            'created_at':'01/05/2022',
            'updated_at':'05/05/2022'
        }
        cls.tag= Tag.objects.create(**cls.data2)
        cls.data3={
            'title':'recipe',
            'image': 'recipe.png',
            'short_description':'recipe of something',
            'content':'blah blah',
            # 'category':'chair',
            'price':12,
            # 'tags':'tag',
            # 'created_at':'01/05/2022',
            # 'updated_at':'05/05/2022'
        }
        cls.blog= Blog.objects.create(**cls.data3)
        cls.data4={
            'fullname':'leyla',
            'email': 'leyla@gmail.com',
            'subject':'hello',
            'comment':'thank you',
            # 'created_at':'01/05/2022',
            # 'updated_at':'05/05/2022'
            # 'recipe_id':'1'
        }
        cls.comment= Comment.objects.create(**cls.data4)

    
    def test_created_data(self):
        category=Category.objects.first()
        tag=Tag.objects.first()
        blog=Blog.objects.first()
        comment=Comment.objects.first()
        self.assertEqual(category.title, self.data1['title'])
        self.assertEqual(tag.title, self.data2['title'])
        self.assertEqual(blog.title, self.data3['title'])
        self.assertEqual(comment.fullname, self.data4['fullname'])

    # def test_str_method(self):
    #     self.assertEqual(str(self.category), self.data1['title'])
    #     self.assertEqual(str(self.tag), self.data2['title'])
    #     self.assertEqual(str(self.recipe), self.data3['title'])
    #     self.assertEqual(str(self.comment), self.data4['fullname'])


    @classmethod
    def tearDownClass(cls):
        Category.objects.first().delete()
        del cls.category
        del cls.data1
        Tag.objects.first().delete()
        del cls.tag
        del cls.data2
        Blog.objects.first().delete()
        del cls.blog
        del cls.data3
        Comment.objects.first().delete()
        del cls.comment
        del cls.data4

