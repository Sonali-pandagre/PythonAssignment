num=10
if num>1:
    for i in range(2,int(num/2)+1):
        if (num % i) == 0:
              print("It is not a prime number",n)
        break
    else:
            print("It is prime no.",num)
else:
    print("it is not a prime no.",num)
