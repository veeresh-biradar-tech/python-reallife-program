# Able to vote

age= int(input("Enter Your Age : "))
if age>= 18 :
    print("Able To Vote")
else:
    print("Not Able To Vote")

# Able To vote Code Using Function

def can_vote(age):
    if age>= 18:
        return "Able To Vote"
    else:
        return "Not Able To Vote"

age= int(input("Enter Your Age : "))
print(can_vote)

# Using try and except Block
def vote(gae):
    return "Able To Vote"

while True:
    try:
        age= int(input("Enter Age : "))
        print(vote(age))
        break
    except ValueError:
        print("Please Enter Valid Age")
        continue