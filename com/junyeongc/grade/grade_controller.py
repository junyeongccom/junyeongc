from com.junyeongc.grade.grade_model import GradeModel
from com.junyeongc.grade.grade_service import GradeService


class GradeController:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.korean = kwargs.get("korean")
        self.english = kwargs.get("english")
        self.math = kwargs.get("math")
        self.society = kwargs.get("society")
        self.science = kwargs.get("science")
        print("username:", self.name)
        print("korean:", self.korean)
        print("english:", self.english)
        print("math:", self.math)
        print("society:", self.society)
        print("science:", self.science)

    def getresult(self) -> GradeModel:
        service = GradeService()
        grade = GradeModel()
        grade.name = self.name
        grade.korean = self.korean
        grade.english = self.english
        grade.math = self.math
        grade.society = self.society
        grade.science = self.science
        return service.execute(grade)