class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_student_grades(self):
        sql = '''SELECT students.first_name, students.second_name, grades.grade, grades.grade_date, subjects.name
        FROM grades LEFT JOIN students ON grades.student_id=students.id
        LEFT JOIN subjects ON grades.subject_id=subjects.id'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            print(res)
            if res:
                return res
        except:
            return []
