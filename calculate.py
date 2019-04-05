def calc(target, hours, l=[]):
	results = []
	hours.sort()
	hasGoneDeeper=False
	for i in hours:
		if target - i >= 0:
			hasGoneDeeper = True
			results = results + calc(target-i, hours, l + [i])
		else:
			if not hasGoneDeeper:
				results.append(l)
				break
	return list(set([tuple(sorted(l)) for l in results]))

def tostr(result):
	l = list(result)
	s = []
	for i in set(l):
		s.append(str(result.count(i)) + "x(" + str(i) + ")")
	return " + ".join(s) + " = " + str(sum(result))
	
	
#import sys

#max_time = int(sys.argv[1])
#h = [int(i) for i in sys.argv[2::]]
max_time = 50
h = [12, 40, 32]
for i in calc(max_time, h):
	print(i, tostr(i))
