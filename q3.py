def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n/2)+1):  #using int(n/2)+1 to check for factors up to half of n because a larger factor of n must be a multiple of a smaller factor that has been already checked
        if n%i==0:
            break
    else: 
        return True
    return False

# print(isPrime(11))
# print(isPrime(4))

N = int(input("enter number upto which prime numbers are to be printed: "))
for i in range(2,N):
    if isPrime(i):
        print(i, end=" ")
    else:
        continue
