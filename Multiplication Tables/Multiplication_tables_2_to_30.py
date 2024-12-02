# Write a program to generate multiplication tables from 2 to 30 and write it to the different files. Place these files in a folder for a 13 – year old.

def generate_table(n):
    value=''
    # print(f"Multiplication table of {n} is:\n {'-'*30}")
    # print("-"*30)
    for i in range(1,11):
        value +=f"{n} X {i} = {n*i}\n"

    with open(f"Multiplication Tables/table_of_{n}.txt",'w' ) as f:
        f.write(f"Multiplication table of {n} is:\n{'-'*30}\n{value}")
for n in range(2,31):
    generate_table(n)
