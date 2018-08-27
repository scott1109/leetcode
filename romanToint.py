#this is my first leetcode
def romanToint(s):
    L={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if len(s) == 1:
        return L[s[0]]
    else:
        add = 0
        sub_add = 0
        for i in range(len(s)-1):     #这里如果不是-1的话，就会在if中out of range,但是这样最后一位就肯定没有算上
            if L[s[i]] >= L[s[i+1]]:  #这里如果不是>=，那么罗马数字III就会被-1-1+1=-1，但是理论上应该是3，所以等于也是加和
                sub_add = L[s[i]]
            else:
                sub_add = -L[s[i]]
            add = add + sub_add
        return add + L[s[-1]]   #因为循环没有到最后一个，所以最后一位肯定是+，因此要加上最后一个数
