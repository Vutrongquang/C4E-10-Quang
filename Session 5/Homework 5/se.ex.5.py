s = input("Enter a string with the dollar symbols:  ")

def remove_dollar_sign (s):
    s = s.replace("$", "")
    return s

print(remove_dollar_sign(s))
