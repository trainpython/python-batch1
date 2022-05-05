def fact(number):
    if(number==1):
        return number
    else:
        return number*fact(number-1)

print('factorial is ',fact(4))

