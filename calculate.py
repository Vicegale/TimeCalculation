def calc(target, hours, l=[]):
	results = []
	hasGoneDeeper = False
	for i in hours:
		if target - i >= 0:
			hasGoneDeeper = True
			results = results + calc(target-i, hours, l + [i])
		else:
			if not hasGoneDeeper:
				results.append(l)
	return list(set([tuple(sorted(l)) for l in results]))

for i in calc(100, [10, 20, 30]):
	print(i)