def calc(a,b,s):
    if sym ==  "+":
        print("(",a,"+",b,") =",a + b)
    elif sym == "-":
        print("(",a,"-",b,") =",a - b)
    elif sym == "*":
        print("(",a,"*",b,") =",a * b)
    elif sym == "/":
        print("(",a,"/",b,") =",a / b)   
 
    
first = int(input("첫번째 수를 입력하세요"))
second = int(input("두번째 수를 입력하세요"))
sym = input("사칙연산중 하나를 입력하세요")

calc(first, second, sym)
    
