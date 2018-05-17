class Solution(object):
    def intToRoman(self, data):
        """
        :type num: int
        :rtype: str
        """
        A = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        B = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        D = ['','M','MM','MMM']
        #result = ''
        # d = data/1000
        # c = data%1000/100
        # b = data%100/10
        # a = data%10
        #return D[d]+C[c]+B[b]+A[a]
        return D[data/1000]+C[data%1000/100]+B[data%100/10]+A[data%10]
