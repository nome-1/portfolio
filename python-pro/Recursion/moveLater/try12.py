n = 8


class solution:
    def __init__(self, num):
        self.num = num

    def numberOfSteps(self):
        print(self.num)
        k=self.num
        step=0
        while k>0:
            step+=1
            if k%2==1:
                print(f'step {step} {k} is odd; subtract 1 and obtain {round(k-1)}.')
                k=k-1
            elif k%2==0:
                print(f'step {step} {k} is even; divide by 2 and obtain {round(k/2)}.')
                k=k/2



p = solution(n)
p.numberOfSteps()
