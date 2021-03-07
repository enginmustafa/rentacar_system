import decimal
import string


class RentResult:

    def __init__(self, success: bool, sum_to_collect: decimal, discount: float, error_message: string):
        self.success = success
        self.sum_to_collect = sum_to_collect
        self.discount = discount
        self.error_message = error_message

    def sum_with_applied_discount(self):
        return self.sum_to_collect * self.discount
