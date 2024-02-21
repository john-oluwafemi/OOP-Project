

from datetime import datetime

class Student:
    def __init__(self, student_id, name, dob, classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__classification = classification

    def calc_age(self):
        today = datetime.now()
        birth_date = datetime.strptime(self.__dob, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def reg_dates(self):
        if self.__classification == "Sr":
            return "Seniors - 4/1 thru 4/3"
        elif self.__classification == "Jr":
            return "Juniors - 4/4 thru 4/6"
        elif self.__classification == "S":
            return "Sophomores - 4/7 thru 4/9"
        elif self.__classification == "F":
            return "Freshmen - 4/10 thru 4/12"
        else:
            return "Invalid classification"

    def get_age(self):
        age = self.calc_age()
        return age

    def get_regDate(self):
        dates = self.reg_dates()
        return dates
    
    def get_name_n_studID(self):
        return self.__name, self.__student_id


