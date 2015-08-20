lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):   # Takes a list of numbers
    total = sum(numbers)        
    total = float(total)
    mean   = total/len(numbers)
    return mean					# We're left with the average of numbers in a list

def get_average(student): # Takes a single student, which is a dictionary
    homework = average(student["homework"]) 
    quizzes  = average(student["quizzes"])  
    tests    = average(student["tests"])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6
    
def get_letter_grade(score): # Takes a single number
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students): # Takes in a list of students
    results = [] # Creates a list to store each student's average
    for student in students:  # Traverses the passed list. Passes a single student to the next statement
    	results.append(get_average(student)) # send the student to get_average(), which gets the average of each scored thing and then combines them all. After that, it appends the resulting number to the `results` list
    return average(results) # Now that the results list is full, we average the whole thing

roster = [lloyd,alice,tyler]

print get_class_average(roster)
print get_letter_grade(get_class_average(roster))

"""
### average()
This average simply describes a straightforward mathematical process of creating a mean
in the way we want. It accepts a list and averages it. Very straight forward.

### get_average()
This function takes a dictionary directly. we don't need to use a loop or anything 
because we're not doing the same thing to multiple like-items. The function gets the 
dictionary and says, "Alright, I've got this thing. It has 4 key-value pairs for me to 
do stuff to. The following statements are what I'll do to those." Ultimately, what happens
is that we do some math to the value of each key, store them as variables, and then combine
them together after weighting them.

### get_class_average()
Basically, this function does three things:
  1. It accepts the class roster (which is a list of dictionaries) and sends each name 
  	 to the get_average() function
  2. It uses the .append() method to store the average of each student (dictionary) in a 
     newly defined list
  3. It takes the completed list, and feeds it to the simple average() function, thus giving
  	 us the full class average

"""
