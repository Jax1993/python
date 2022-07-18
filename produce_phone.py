with open('/Users/wh/Downloads/phone.txt', 'w') as f:    
    for i in range(90000,110000):
        phone = '628' + str(i).zfill(10)
        f.write(phone)
        f.write('\r')
    