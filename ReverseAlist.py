#Reversing A List Without Using The reverse Function
nums= [10, 20, 30, 40, 50]
print(f"Original List= {nums}")
print(f"After Reversing= {nums[::-1]}")


#Reversing A List Without Using The reverse Function And Slice Method
num= [100, 200, 300, 400, 500]
for i in range(len(num)-1, -1, -1):
    print(num[i], end=" ")