# POINTS                      RECURSION      ITERATION
# Space Efficient?              NO              YES         No stack memory require in case of iteration 


# Time Efficient?               NO              YES         In case of recursion system needs more time 
#                                                           for pop and push elements to stack memory which 
#                                                           makes recursion less time efficient


# Easy to code?                  YES             NO          we use recursion especially in the cases we know that 
#                                                             a problem can be divided into similar sub problems



def powerofTwo(n):
    if n==0:
        return 1
    else:
        return 2*powerofTwo(n-1)
    
print(powerofTwo(4))

