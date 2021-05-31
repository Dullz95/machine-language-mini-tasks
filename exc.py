import numpy as np
from numpy import *
from scipy import stats
marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

mean_of_marks = np.mean(marks_of_students)
median_of_marks = np.median(marks_of_students)
mode_of_marks = stats.mode(marks_of_students)
# print("The mean is: " + str(mean_of_marks))
# print("The median is: " + str(median_of_marks))
# print(mode_of_marks)

# dispersion

range = np.ptp(marks_of_students)
# print(range)

# number in perenthesis indicates the quartile range
twenty_five = np.percentile(marks_of_students, 25)
# print(twenty_five)

variants = np.var(marks_of_students)
# print(variants)

# convert varients into standard deviation

std = np.std(marks_of_students)
# print(std)