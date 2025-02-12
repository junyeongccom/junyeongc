from dataclasses import dataclass

@dataclass
class GugudanModel:

    number: int
    result: str

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def result(self) -> str:
        return self._result

    @result.setter
    def result(self, result):
        self._result = result