import random
import time

def print_int(x):
	if x == 0:
		return "                   0"
	result = ""
	x = str(x)
	while len(x) < 15:
		x = " " + x
	for i in range(5):
		result += " "
		for j in range(3):
			result += x[3*i+j]
	return result

def GetString(x, rdm = False):
	t = ""
	if (not rdm):
		for i in range(x):
			t += "abcdefghijklmnopqrstuvwxy0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_&:;,?./*-+=()[]{}"
	else :
		for i in range(100*x):
			t += chr(random.randrange(0,256))
	return t

initial = ""
initial2 = ""
#initial += GetString(2000, True)
#initial += GetString(2000)


def __Concat20(L,l):
	x = 20
	R = []
	tmp = l // x
	if (tmp == 0):
		result = ""
		for s in L:
			result += s
		return [result],1
	else :
		k = l - tmp * x
		while(k != 0):
			L[tmp*x-2+k] += L.pop()
			k -= 1
		for j in range(tmp):
			R.append(L[x*j] + L[x*j + 1] + L[x*j + 2] + L[x*j + 3] + L[x*j + 4] + L[x*j + 5] + L[x*j + 6] + L[x*j+7] + L[x*j + 8] + L[x*j + 9] + L[x*j + 10] + L[x*j + 11] + L[x*j + 12] + L[x*j + 13] + L[x*j + 14] + L[x*j + 15] + L[x*j + 16] + L[x*j+17] + L[x*j + 18] + L[x*j + 19])
		return R,tmp

def Concat20(L):
	t = len(L)
	if (t == 0):
		return ""
	while(t > 1):
		(L,t) = __Concat20(L,t)
	return L[0]

def __Concat10(L,l):
	x = 10
	R = []
	tmp = l // x
	if (tmp == 0):
		result = ""
		for s in L:
			result += s
		return [result],1
	else :
		k = l - tmp * x
		while(k != 0):
			L[tmp*x-2+k] += L.pop()
			k -= 1
		for j in range(tmp):
			R.append(L[x*j] + L[x*j + 1] + L[x*j + 2] + L[x*j + 3] + L[x*j + 4] + L[x*j + 5] + L[x*j + 6] + L[x*j+7] + L[x*j + 8] + L[x*j + 9])
		return R,tmp

def Concat10(L):
	t = len(L)
	if (t == 0):
		return ""
	while(t > 1):
		(L,t) = __Concat10(L,t)
	return L[0]


def __Concat2(L,l):
	x = 2
	R = []
	tmp = l // x
	k = l - tmp * x
	if (k == 1):
		L[tmp*x-2+k] += L.pop()
	for j in range(tmp):
		R.append(L[x*j] + L[x*j + 1])
	return R,tmp

def Concat2(L):
	t = len(L)
	if (t == 0):
		return ""
	while(t > 1):
		(L,t) = __Concat2(L,t)
	return L[0]


start = time.time_ns()
for i in range(1000000):
	initial += 'a'
endc = time.time_ns()

L20 = []
for i in range(1000000):
	L20.append('a')
initial20 = Concat20(L20)
end20 = time.time_ns()

L10 = []
for i in range(1000000):
	L10.append('a')
initial10 = Concat10(L10)
end10 = time.time_ns()

L2 = []
for i in range(1000000):
	L2.append('a')
initial2 = Concat10(L2)
end = time.time_ns()




print(initial == initial2 and initial2 == initial10 and initial2 == initial20)
print("Classique:                 " + print_int(endc-start) + " ns")
print("Opti 20  :                 " + print_int(end20-endc) + " ns")
print("Opti 10  :                 " + print_int(end10-end20) + " ns")
print("Opti 2   :                 " + print_int(end-end10) + " ns")
