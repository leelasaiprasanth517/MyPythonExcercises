def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
class Solution():
    def Gcdofstrings(self,str1,str2):
        res=[]
        if (str1+str2)==(str2+str1):
            l=gcd(len(str1),len(str2))
            res.append(str1[:l])
        return ''.join(res)
sol=Solution()
print(sol.Gcdofstrings('Leela','LeelaLeelaLeelaLeelaLeela'))