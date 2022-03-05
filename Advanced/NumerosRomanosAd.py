def traductor(x):
        romVal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(x)):
            if i > 0 and romVal[x[i]] > romVal[x[i - 1]]:
                res += romVal[x[i]] - 2 * romVal[x[i - 1]]
            else:
                res += romVal[x[i]]
        return res
print(traductor("CCCXXXVI"))
    
    