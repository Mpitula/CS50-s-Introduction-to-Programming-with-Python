def convert(faces):
    #convert then return value
    return faces.replace(":)","🙂").replace(":(","🙁")

def main():
    #print input from the user and convert the  string
    print(convert(input()))

main()
