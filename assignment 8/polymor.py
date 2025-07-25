class India():
    def capital(self):
        print("new delhi is the capital of india.")
    def langauge(self):
        print("Hindi is the widely spoken language in india.")
    def type(self):
        print("India is the developing country.")
    class USA():
        def capital(self):
            print("washington,D.C. is the capital of USA.")
        def langauge(self):
            print("English is the primary langauge of USA")
        def type(self):
            print("USA is devolped country.")
    obj_ind= India()
    obj_usa= USA()     
    for country in(obj_Ind,obj_usa):
     country.capital()
     country.langauge()
     country.type()
     