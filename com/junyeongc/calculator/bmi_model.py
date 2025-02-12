from dataclasses import dataclass

@dataclass
class BmiModel:

    height: int
    weight: int
    result: str

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def result(self) -> int:
        return self._result

    @result.setter
    def result(self, result):
        self._result = result