# Can use dictionary to use symbols and keys then call as required 
# because we can do func=add this stores add in func so when we call 
# func it automatically calls add

def sum(n):
    n_2=input("Enter the 2nd : ")
    n_2=float(n_2) if '.' in n_2 else int(n_2)
    return n+n_2

def subs(n):
    n_2=input("Enter the 2nd : ")
    n_2=float(n_2) if '.' in n_2 else int(n_2)
    return n-n_2

def multiply(n):
    n_2=input("Enter the 2nd number : ")
    n_2=float(n_2) if '.' in n_2 else int(n_2)
    return n*n_2

def divide(n):
    n_2=input("Enter the 2nd number : ")
    n_2=float(n_2) if '.' in n_2 else int(n_2)
    return n/n_2

def remainder(n):
    n_2=input("Enter the 2nd number : ")
    n_2=float(n_2) if '.' in n_2 else int(n_2)
    return n%n_2

def power(n):
    n_2=input("Enter the 2nd number : ")
    n_2=float(n_2) if '.' in n_2 else int(n_2)
    return n**n_2


# Calculator
print("CALCULATOR\n")
n=input("Enter no. : ")
n=float(n) if '.' in n else int(n)
work=True
while work:
    op=input("Select the operation to be done on the number :\n'+' '-' '*' '/' '%' '^'\n")
    if op=='+':
        n=sum(n)
    elif op=='-':
        n=subs(n)
    elif op=='*':
        n=multiply(n)
    elif op=='/':
        n=divide(n)
    elif op=='%':
        n=remainder(n)
    elif op=='^':
        n=power(n)
    print(f"Result : {n}")
    choice=input("Press \"Y\" to continue operation with the result any other key to stop : ")
    if choice.upper()!="Y":
        work=False
    