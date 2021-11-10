try:
    def month(n):
        months = {1:"jan",2:"feb",3: "mar",4:"apr",5:"may",6:"jun",7:"jul",8:"aug",9:"sep",10:"oct",11:"nov",12:"dec"}
        return months[n]

    print(month(7))
except:
    print("wrong input!!!")