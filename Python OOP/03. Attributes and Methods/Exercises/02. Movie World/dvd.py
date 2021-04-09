class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, name, id, date, age_restriction):
        _, creation_month, creation_year = date.split(".")
        creation_month = int(creation_month)
        creation_year = int(creation_year)
        if creation_month == 1:
            creation_month = "January"
        elif creation_month == 2:
            creation_month = "February"
        elif creation_month == 3:
            creation_month = "March"
        elif creation_month == 4:
            creation_month = "April"
        elif creation_month == 5:
            creation_month = "May"
        elif creation_month == 6:
            creation_month = "June"
        elif creation_month == 7:
            creation_month = "July"
        elif creation_month == 8:
            creation_month = "August"
        elif creation_month == 9:
            creation_month = "September"
        elif creation_month == 10:
            creation_month = "October"
        elif creation_month == 11:
            creation_month = "November"
        elif creation_month == 12:
            creation_month = "December"
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has " \
               f"age restriction {self.age_restriction}. Status: {status}"