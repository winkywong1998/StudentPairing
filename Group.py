import Student


class Group:
    def __init__(self, student_list):
        self.student_list = student_list
        self.major = self.list_parser("major")
        self.purpose = self.list_parser("purpose")
        self.pref = self.list_parser("pref")

    def list_parser(self, field):
        parse_list = []
        for student in self.student_list:
            var = eval("student." + str(field))
            if var in parse_list:
                return [var]
            else:
                parse_list.append(var)
        parse_list.sort()
        return parse_list


