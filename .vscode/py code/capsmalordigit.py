a = input()
b = ord(a)

if 48 <= b <= 57:
    print("IS DIGIT")
elif 65 <= b <= 90:
    print("ALPHA\nIS CAPITAL")
elif 97 <= b <= 122:
    print("ALPHA\nIS SMALL")
