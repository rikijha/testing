string="ABDCDA"


def first_rec(given_string):
    count={}
    for char in given_string:
        if char in count:
            return char
        else:
            count[char]=1


p=first_rec(string)

print(p)