# Del Keyword
# del keyword is use for deleting object property or entire object like

class item:
    def __init__(self,item_id,name):
        self.item_id=item_id
        self.name=name

i1=item(1,'Fruits')       #i1,i2,i3 are objects 
i2=item(2,'Vegetables')
i3=item(3,'Cold Drinks')
print(i1.item_id,i1.name)  
print(i2.item_id,i2.name)  
print(i3.item_id,i3.name)  

del i1.item_id,i1.name
print(i1.item_id,i1.name)# shows error because in previous line we deleted item_id



# --------------------------------PRIVATE ATTRIBUTE--------------------------------


# public and private attributes & methods 
# private karne par hum us attr ko uss class ke bahar access nahi kar pate example

class Account:
    def __init__(self,Account_no,Password):
        self.Account_no=Account_no
        self.Password=Password
        
acc1=Account(123456,'abcd')
print(acc1.Account_no,acc1.Password)
# here password attribute taken is public so it can be access from anywhere but if we make it private by simply giving __ before calling it, password can be made private which can be only accessed inside the class 



class Account_new:
    def __init__(self,Account_no,Password):
        self.Account_no=Account_no
        self.__Password=Password

        print (Password)   # It can be called because is called inside the class
        
acc1=Account_new(123456,'abcd')
print(acc1.Account_no,acc1.__Password)   # shows error while calling aac1.__Password