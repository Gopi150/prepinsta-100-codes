a=input()
n=True
if(n!=a.isalpha() and n!=a.isdigit() and n!=a.isspace()and n==a.isupper()):
    print("string is valid")
else:
    print("string is invalid")
    print("Your string must contions\natleast 1 Alphabet\natleast 1 digit\natleast 1 Symbol")
