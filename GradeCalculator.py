#Create a list of test scores for a student.
#Use floor division to calculate the average score.
#Use comparison operators to determine the grade based on the average score.
#Use assignment operators to update the student's grade.
#Use membership operators to check if a specific score exists in the list of scores.
#Use identity operators to compare objects.
#Use bitwise operators to perform bitwise operations on the scores.

print("============================================================")
print("==================Student Grade Calculator==================")
#list of scores for the grade calculator
scores = [50, 97,80,45,23,76,65,32,59]
#Find the sum of the scores, the number of test scores, the average of the scores using floor division
total_score = sum(scores)
number_score = len(scores)
average_score = total_score // number_score
highest_score = max(scores)
print("The average Student Score:",average_score)
print("The Total number of Students:",number_score)
print("The sum of the Students Scores:",total_score)
print("The higest test score is:",highest_score)
print("============================================================")

#Assign grades using comparision operators
if average_score >= 90:
    grade = 'A+'
elif average_score >= 80:
    grade = 'A'
elif average_score >= 70:
    grade = 'B'
elif average_score >= 60:
    grade = 'C'
elif average_score >= 50:
    grade = 'D'
else:    
    grade = 'F'
print ("The Average Test Grade is:\n",grade)
# upate the score with an assignment operator
if average_score % 10 >= 5:
    grade += "+"
print("Average Test Grade:",grade)

#check if the score is one of the scores in the list
check_score = 90
if check_score in scores:
    print(f"A Test score of {check_score} is in the list!")
else:
    print(f"The Test score of {check_score} does not exist!")

#compare objects/lists using identity operators
average_copy=average_score
if average_score is average_copy:
    print("The Average and the Copy are the same Object!")
else:
    print("The Average and the Copy are not the same Object!")

# Perform bitwise operations on the scores in the list

#print(bin(scores[0]))#50 score at position 0 in the list
#print(bin(scores[1]))#97 score at position 1 in the list
bitwise_result=scores[0] & scores[1] 
bitwise_result2=scores[0] | scores[1] 
print(bin(bitwise_result)) 
print(bin(bitwise_result2)) 
print(bitwise_result2)
#print(bin(0b00100000))
#print(int(0b00100000))
print(f"The Bitwise AND of the first two scores equals: {bitwise_result}")
#Display the Students Final Grade
print("============================================================")
print(f"The Student's Average score is {average_score} and their Grade is {grade}.")
print("============================================================")

