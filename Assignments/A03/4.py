n = int(input())
HPs = input()
s, t = sorted(map(int, input().split()))
operation = 0

for i in range(s, t):
	if HPs[i] == "H" and HPs[i-1] == "P":
		start = i
	elif HPs[i] == "P" and HPs[i-1] == "H":
		operation += bin(i - start).count('1')

print(operation)