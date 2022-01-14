string = 'XUAN' 'TUNG'
print ('Tên',string)
n = len(string)
def songuyen(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
n = len(string)
print(string, "=",songuyen(n));