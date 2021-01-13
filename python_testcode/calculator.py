class Calculator():
    def add(self,a,b):
        noCarry = a^b #不需要进位的
        carry = (a&b)<<1 #需要进位的
        while carry != 0:
            a = noCarry
            b = carry
            noCarry = a^b
            carry = (a&b)<<1

        sum =  noCarry
        return sum

    def sub(self,a,b):
        # a-b = a+(-b)
        b = ~b
        b = self.add(b,1)
        sub = self.add(a,b)
        return sub


    def mul(self,a,b):
        flag = 0
        if (a < 0 and b > 0 ) or (a> 0 and b < 0):
            flag = 1
        if a < 0:
            a = self.sub(0,a)
        if b < 0:
            b = self.sub(0,b)
        ans = 0
        while(b != 0 or a != 0):
            if b&1 != 0 :
                ans = self.add(ans,a);
            a = a<<1
            b = b>>1

        if flag :
            ans = self.sub(0,ans);
        return ans

    def div(self,a,b):
        restult_flag = 0
        mod_flag = 0
        if(a<0 and b>0) or (a>0,b<0):
            restult_flag = 1
        if a < 0:
            a = self.sub(1,a)
        if b < 0:
            mod_flag = 1
            b = self.sub(1,b)
        result = 0
        i = 31
        while(i >= 0):
            j = a >> i
            if j >= b:
                result = self.add(result,1<<i)
            a = self.sub(a,b<<1)
            if a < b:
                break;

        mod = a;
        if restult_flag:
            result = self.sub(0,result)
        if mod_flag:
            mod = self.sub(0,mod)
        return result
