Test your knowledge.
** Answer the following questions **

Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

Double Click HERE to edit this markdown cell and write answers.

Numbers:

Strings:

Lists:

Tuples:

Dictionaries:

Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
(60 + (10 ** 2) / 4 * 7) - 134.75
Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

 
Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)
44
What is the value of the expression 4 * 6 + 5 
29
What is the value of the expression 4 + 6 * 5 
34
What is the type of the result of the expression 3 + 1.5 + 4?
Floating point number

What would you use to find a number’s square root, as well as its square?

# Square root:
100 ** 0.5
10.0
# Square:
10 ** 2
100
Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
s[1]
'e'

Reverse the string 'hello' using slicing:
s ='hello'
# Reverse the string using slicing
s[::-1]
'olleh'

Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
# Print out the 'o'
# Method 1:
s[-1]
# Method 2:
s[4]


Lists
Build this list [0,0,0] two separate ways.
# Method 1:
[0]*3
[0, 0, 0]
# Method 2:
list2 =[0,0,0]
[0,0,0]

Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
Sort the list below:
list3[2][2] = 'goodbye'
list3
[1,2, [3, 4, 'goodbye']]

list4 = [5,3,4,6,1]
# Method 1:
sorted(list4)
# Method 2:
list.4sort()
list4

Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
d['k1'][0]['nest_key'][1][0]

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]


Can you sort a dictionary? Why or why not?
no, normal dictionaries are mappings not a sequence

Tuples
What is the major difference between tuples and lists?
Tuples are immutable

How do you create a tuple?
t = (1,2,3)

Sets
What is unique about a set?
They dont allow for duplicate items

Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)
{1, 2, 3, 4, 11, 22, 33}

Booleans
For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3
false
# Answer before running cell
3 <= 2
false
# Answer before running cell
3 == 2.0
false
# Answer before running cell
3.0 == 3
true
# Answer before running cell
4**0.5 != 2
false 

Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

false