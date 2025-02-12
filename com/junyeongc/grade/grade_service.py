from com.junyeongc.grade.grade_model import GradeModel


class GradeService:
    def __init__(self):
        pass

    def execute(self, grade: GradeModel) -> GradeModel: 
        name = grade.name
        korean = grade.korean
        english = grade.english
        math = grade.math
        society = grade.society
        science = grade.science
        print("------------------")
        print("username:", name)
        print("korean:", korean)
        print("english:", english)
        print("math:", math)
        print("society:", society)
        print("science:", science)

        total = korean + english + math + society + science
        average = total / 5
        print("total:", total)
        print("average:", average)

        if average > 90:
            result = "A학점입니다."
        elif average > 80:
            result = "B학점입니다."
        elif average > 70:
            result = "C학점입니다."
        elif average > 60:
            result = "D학점입니다."
        else:
            result = "F학점입니다."
            return result
        
        grade.result = result
        grade.name = name
        return grade

        