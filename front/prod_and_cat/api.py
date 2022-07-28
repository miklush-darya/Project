from flask import session
import requests

from config import Config
# from app.utils import check_response_errors
from prod_and_cat.models import ProductsAdd, CategoryAdd, ShopProductsAdd

CREATE_PRODUCTS_URL = f"{Config.API_URL}/products/"
CREATE_CATEGORY_URL = f"{Config.API_URL}/category/"
CREATE_SHOPPRODUCT_URL = f"{Config.API_URL}/shopproduct/"


def add_product(*args, **kwargs) -> ProductsAdd:
    add_product = ProductsAdd(**kwargs)
    res = requests.post(CREATE_PRODUCTS_URL, json=add_product.dict())
    product = ProductsAdd(**res.json())
    return product

def add_category(*args, **kwargs) -> CategoryAdd:
    add_category = CategoryAdd(**kwargs)
    res = requests.post(CREATE_CATEGORY_URL, json=add_category.dict())
    category = CategoryAdd(**res.json())
    return category

def add_shopproduct(*args, **kwargs) -> ShopProductsAdd:
    add_shopproduct = ShopProductsAdd(**kwargs)
    res = requests.post(CREATE_SHOPPRODUCT_URL, json=add_category.dict())
    shopproduct = ShopProductsAdd(**res.json())
    return shopproduct