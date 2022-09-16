from modeltranslation.translator import translator, TranslationOptions
from Product.models import Product


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Product, ProductTranslationOptions)