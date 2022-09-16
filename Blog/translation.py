from modeltranslation.translator import translator, TranslationOptions
from Blog.models import Category,Blog


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'short_description', 'content',)


translator.register(Blog, BlogTranslationOptions)
translator.register(Category, CategoryTranslationOptions)