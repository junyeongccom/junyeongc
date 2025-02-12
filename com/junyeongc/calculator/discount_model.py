from dataclasses import dataclass

@dataclass
class DiscountModel:

    amount: int
    result: int

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def result(self) -> int:
        return self._result

    @result.setter
    def result(self, result):
        self._result = result