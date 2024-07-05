def make_slug(s):
    special = ["!", "@", "#", "%", "^", "*", "(", ")","+"," "]
    if s[0] in special:
        s.strip(s[0])
    if s[-1] in special:
        s.strip(s[-1])

    for i in s:
        if i in 

s = "nizam"