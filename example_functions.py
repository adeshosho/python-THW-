numerical = 36
letter = "F"

def calculate_grade(grade):
	if grade > 80:
		letter = "A"
	elif grade > 70:
		letter = "B"
	elif grade > 60:
		letter = "C"
	elif grade > 50:
		letter = "D"
	return letter
def calculate_grade2(grade):
    if grade > 80:
        letter = "A"
    elif grade > 70:
        letter = "B"
    elif grade > 60:
        letter = "C"
    elif grade > 50:
        letter = "D"
    else:
        letter = "F"
    return letter

print(calculate_grade2(numerical))