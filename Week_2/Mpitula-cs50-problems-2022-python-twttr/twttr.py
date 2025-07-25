vowels = ["A","E","I","O","U","a","e","i","o","u"]
string = input("Input: ")
result = ""
for i in string:
    if i not in vowels:
        result+=i
print(result)
