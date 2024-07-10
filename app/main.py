from fastapi import FastAPI, status
from models.models import Product


app = FastAPI()


sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2,
                   sample_product_3, sample_product_4, sample_product_5]
products: list[Product] = [Product(**item) for item in sample_products]


@app.get('/products/search', status_code=status.HTTP_200_OK)
async def product_info_by_filters(keyword: str, category: str | None = None, limit: int = 10) -> list[Product]:
    product: list[Product] = []
    for item in products:
        if len(product) == limit:
            break

        if keyword in item.name.lower():
            if category is None:
                product.append(item)
            elif category == item.category:
                product.append(item)

    return product


@app.get('/product/{product_id}', status_code=status.HTTP_200_OK)
async def product_info_by_id(product_id: int) -> Product | None:
    result = next(
        (item for item in sample_products if item['product_id'] == product_id), None)
    return result
