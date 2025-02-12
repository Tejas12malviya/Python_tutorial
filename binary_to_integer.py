mystr=str(input("Enter the binary number you want to convert :"))

def binary_to_int(mystr):
    for x in mystr:
        if x not in '01':
            return "Error, String with non-binary"
    
    num=int(mystr,2)
    return num
print(f"binary : {mystr} , its conversion in number is : {binary_to_int(mystr)}")
