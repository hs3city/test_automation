from dataclasses import dataclass
from decimal import Decimal

#klasa do parsowania elementów w koszyku.
@dataclass
class CartTableItem:
    #item_class:
    name: str
    price: Decimal
    quantity: int


class CartTable:
    @property
    def xpath(self):
        # "//table[contains(@class, 'cart')]"
        return f'//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[2]/a'


class CartPage:
    pass
