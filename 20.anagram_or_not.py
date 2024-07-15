n1=input()
n2=input()
if len(n1)==len(n2):
    if sorted(n1)==sorted(n2):
        print("anagram")
    else:
        ptint("not a anagram")
else:
    print("length is not match")
