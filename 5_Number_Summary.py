thomas = [33, 40, 55, 80, 85, 88, 90, 93, 99]
#         0    1   2   3   4   5   6   7   8
grades = [2, 33, 40, 55, 80,80,81,79,95,84,84,85,79,82,87, 85, 88, 90, 93, 99]
p = [1,2,3]
def set_sum(grades):
	total = 0
	for grade in grades: 
		total += grade
	return total
	
def set_average(grades):
	sum_of_grades = set_sum(grades)
	average = sum_of_grades / float(len(grades))
	return average

def set_variance(scores):
	variance = 0
	average = set_average(scores)
	for score in scores:
		variance += (average - score) ** 2
	variance = variance/len(scores)
	return variance

def set_std_deviation(scores):
	variance = set_variance(scores)
	return variance ** 0.5

def set_median(scores):
	s = sorted(scores)
	if len(s) % 2 == 0:
		return (s[len(s)/2-1] + s[len(s)/2]) * 0.5
	else:
	  return s[len(s)/2]

def set_max(scores):
	return sorted(scores)[-1]
def set_min(scores):
	return sorted(scores)[0]

#Improve: figure out 1 equation to handle sets of 3 or 7
def set_Q1(scores):
	s = sorted(scores)
	q1 = []
	if len(range(0, len(s)/2)) % 2 == 0:
		for i in range(0, len(s)/2):
			q1.append(s[i])
		return set_median(q1)
	elif len(s) == 3:
		return (s[0]+s[1]) * 0.5
	else:
		return s[1]

def set_Q3(scores):
	s = sorted(scores)
	q3 = []
	if len(s) == 3:
		return (s[1]+s[2]) * 0.5
	elif len(s) == 7:
		return s[5]
	elif len(s) % 2 == 0:
		for i in range(len(s)/2, len(s)):
			q3.append(s[i])
		return set_median(q3)
	else:
		for i in range(len(s)/2+1, len(s)):
			q3.append(s[i])
		return set_median(q3)

def five_number_summary(set):
	print "===Five Number Summary==="
	print "Min:", set_min(set)
	print "Lower Quartile:", set_Q1(set)
	print "Median:", set_median(set)
	print "Upper Quartile:", set_Q3(set)
	print "Max:", set_max(set)
	print ""
	print "Standard Deviation:", set_std_deviation(set)
	
five_number_summary(grades)