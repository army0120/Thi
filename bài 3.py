def ThuanNghich(n):
    str1 = str(n);     
    str2 = str1[::-1]; 
    if (str1 == str2):
        return ("là số thuận nghịch");
    else:
        return ("không phải số thuận nghịch");
ho=str('nguyen')
tendem=str('xuan')
ten=str('tung')
print ('Tên',ho,tendem,ten,' N = ',len(ho),len(tendem),len(ten))
n=str(len(ho))+str(len(tendem))+str(len(ten))
print("Số", n , "là",ThuanNghich(n));
