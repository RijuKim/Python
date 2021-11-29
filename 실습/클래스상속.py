class TV(object):
    def __init__(self, size, year, company):
        self.size = size
        self.year = year
        self.company = company

    def describe(self):
        print(self.company + "에서 만든", self.year + "년형",
              self.size + "인치", "UHDTV")


class MobilePhone(TV):
    def describe(self):
        print(self.company + "에서 만든", self.year + "년형",
              self.size + "인치", "갤럭시폴더폰")


Samsung_MobilePhone = MobilePhone("8", "2021", "Samsung")
Samsung_MobilePhone.describe()
