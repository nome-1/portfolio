

def pangrams(s):
    S=s.replace(" ","")
    print(S)
    bob=(set(S.lower()))
    print(len(bob),bob)
    if len(bob)==26:
        return f"pangram"
    else:
        return f"not pangram"

s="We promptly judged antique ivory buckles for the prize"
t="NOVmETKPTbYu ftZPEykhjgF GGkdGjWGwW skjPJsea dtwdqcr DERCUgxOxrRgDQbdzL IZjyXs"
print(pangrams(t))