import sys
IFSs = sys.stdin.readlines

_N_Strings = [ int(_.rstrip()) for _ in IFSs() ]
# The State Veterinary Services Department recently reported an outbreak of a newly found cow disease
# Allcows found to have affected by the disease have since euthanized because of the risk to the industry.


# print(_N_Strings)
dp = [0] * (max(_N_Strings)+1)

# Number of affected cowsincreased to 21, 34 and reached 55 after eight, nine and ten hours respectively.
dp[1], dp[2], dp[8], dp[9], dp[10]  = 1, 1, 21, 34, 55

for i in range(1, len(dp)):
    if i == (x for x in _N_Strings) :
        dp[i] = _N_Strings[i-1]
    
# print(dp)

for i in range(2, len(dp)):
    dp[i] = dp[i-1] + dp[i-2]
    
for itemAsIdx in _N_Strings:
    if itemAsIdx == -1:
        break
    else:
        print(f"Hour {itemAsIdx}: {dp[itemAsIdx]} cow(s) affected")