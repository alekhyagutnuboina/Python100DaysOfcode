class a:
    def __int__(self,name,title,gender,religion,country):
        self.name=name
        self.title=title
        self.gender=gender
        self.religion=country

def retrieve(self):
       if hasattr(self,"_company"):
           return "{0}.{1} is of {2} and he is from {3} and works in {5}".format(self.title,self.name,self.gender,self.country,self._company)
       else:
          return "{0}.{1} is of {2} and he is from {3}".format(self.title,self.name,self.gender,self.country)

def setcompany(self,company):
        self._company = company




class b:
    def __init__(self,name,title,company,religion,country):
        self.name=name
        self.title=title
        self.company=company
        self.religion=religion
        self.country=country







