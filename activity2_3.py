amount=int(input("please enter your amount"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10

print("note of 100rupees",note_1)
print("note of 50rupees",note_2)
print("note of 10rupees",note_3)