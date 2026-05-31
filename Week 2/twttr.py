Text = input("Input: ")

vowels = ['a' , 'e' , 'i', 'o', 'u']
k = ""

for i in range(len(Text)):
    if Text[i].lower() not in vowels:
        k += Text[i]

print("Output: ", k)