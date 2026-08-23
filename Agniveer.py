print("Hi Guys I Am Trying For Making An Army Checkup Tool For Agniveer GD Male Candidates")
print("For Physical Checkup")
is_age = float(input("Enter The Age Of The Candidate:(years) "))
is_height = float(input("Enter The Height Of The Candidate:(cm) "))
is_weight = float(input("Enter The Weight Of The Candidate:(kg) "))
is_chest = float(input("Enter The Size Of The Chest:(cm) "))
is_married = input("Is The Candidate Married? (yes/no) ").lower()
print("Check The Physical Fitness Test Components PFT:-")
is_run = int(input("Enter The Time Taken For 1.6 Km Run:(seconds) "))
beams = int(input("Enter The Number Of Pushups Done By The Candidate:"))
is_pass_zigzag = input("Did The Candidate Pass The Zig-Zag Test? (yes/no) ").lower()

is_eligible =(is_age>=17.5 and is_age<=21) and (is_height>=170) and (is_weight>=52 and is_weight<=63.6) and is_chest>=77 and is_married=="no" and is_run<=345 and beams>=6 and is_pass_zigzag=="yes"
if is_eligible==True:
    print("The Male Candidate Is Eligible For Agniveer GD ")
else:
    print("The Male Candidate Is Not Eligible For Agniveer GD ")