from fibonacci import fibo as F

N=11
print "Testing the identity sum_{n=1}^N F_n = F_(N+2)-1"
print "For N= {}".format(N)
print "LHS =" + str(sum([F(n) for n in range(1,N+1)]))
print "RHS =" + str(F(N+2)-1)