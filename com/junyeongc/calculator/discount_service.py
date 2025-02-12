
from .discount_model import DiscountModel
    
class DiscountService:
    def execute(self, discount: DiscountModel) -> DiscountModel:
        amount = discount.amount
        if amount >= 100000:
            result = amount * 0.1
        elif amount >= 50000:
            result = amount * 0.05
        elif amount >= 10000:
            result = amount * 0.03
        else:
            result = amount * 0.01
        discount.result = result
        return discount