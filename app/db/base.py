from sqlalchemy.orm import Session

from app.db.base_class import Base
from app.models.cart import Cart
from app.models.cart_item import Cart_Item
from app.models.category import Category
from app.models.order import Order
from app.models.order_product import Order_Product
from app.models.payment_details import PaymentDetails
from app.models.product import Product
from app.models.product_category import Product_Category
from app.models.product_sku import ProductSku
from app.models.product_wishlist import Product_Wishlist
from app.models.shop import Shop
from app.models.user import User
from app.models.wishlist import Wishlist


def save(db: Session, data: Base):
    db.add(data)
    db.commit()
    db.refresh(data)
