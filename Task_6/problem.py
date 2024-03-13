#1093. Statistics from a Large Sample in leetcode
# add this lib just the yellow line goes :)
from ast import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        #init value to every var
        Maxmum = float('-inf')
        Minmum = float('inf')
        Mode = 0
        freq = 0
        totalSum=0
        for i in range(len(count)):
            if count[i]!=0:

                #Max & Min
                Maxmum = max(Maxmum,i)
                Minmum = min(Minmum,i)

                #Mode
                if count[i]>count[Mode]:
                    Mode = i
                
                #Sum
                freq+=count[i]*i
                totalSum+=count[i]
        
        #Avg
        Mean = freq/totalSum

        #Median
        start=0
        mid=0

        #Odd number
        if totalSum%2 ==1:
            for i in range(len(count)):
                if start<totalSum // 2+1:
                    start+=count[i]
                else:
                    Median = i-1
                    break 
            return[Minmum,Maxmum,Mean,Median,Mode]

        #Even number
        left =0 
        right=0 
        midleft =0 
        midright = 0
        for i in range(len(count)):
            if left<totalSum//2:
                left+=count[i]
            else:
                midleft = i-1
                break
        for i in range(len(count)):
            if right<totalSum//2+1:
                right+=count[i]
            else:
                midright = i-1
                break
        return[Minmum,Maxmum,Mean,(midleft+midright)/2,Mode]
        
        




        