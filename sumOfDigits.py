def sumOfDigits(n):
    if(n< 0):
        print("Number should be positive");
        return '';
    
    if n == 0:
        return 0;
    else:
        return int(n%10) + sumOfDigits(int(n/10));

print(sumOfDigits(-41));