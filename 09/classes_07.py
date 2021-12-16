class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'
        self.fullname = 'Cracow University of Economics'

    def set_name(self,name):
        self.name = name

    def set_fullname(self,fullname):
        self.fullname = fullname

    def print_fullname(self):
        print(self.fullname)

    # object bahaviors (methods)
    def print_name(self):
        print(self.name)

# uni = University()
# uni.print_name()
#
# uni2 = University()
# uni2.set_name("AGH")
# uni2.print_name()

uni3 = University()
uni3.print_name()
uni3.print_fullname()
uni3.set_name('AGH')
uni3.set_fullname("Akademia Górniczo-Hutnicza")
uni3.print_name()
uni3.print_fullname()

