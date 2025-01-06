
def percentage(marks):
    sum=0
    for i in marks.values():
        sum+= i
    final_score=round(float(sum/len(marks)),2)
    print(final_score)

import random
list=['Banana','car','Pepsico']
print(random.choice(list))

x=random.randint(1,10)
print(x)
