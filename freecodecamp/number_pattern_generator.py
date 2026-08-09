def number_pattern(n):
    num = ''
    if not isinstance(n,int):
        return "Argument must be an integer value."
    elif n<1:
        return'Argument must be an integer greater than 0.'
    else:
       for i in range(1,n+1):
        num += str(i)+' '
    return num.strip()
print(number_pattern(4))