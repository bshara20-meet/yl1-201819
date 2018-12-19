# class Person:
#   def __initalize__(self, first_name, last_name):
#     self.first = first_name
#     self.last = lname
#   def speak(self):
#   print("My name" + " self.fname" + "self.last")

# me = Person("Brandon", "Walsh")
# you = Person("Ethan", "Reed")

# me.speak()
# you.self.speak
import tkinter as tk
from tkinter import simpledialog
exam_one = int(simpledialog.askstring("Input","Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input","Input exam grade two: ", parent=tk.Tk().withdraw()))

exam_three=int(simpledialog.askstring("Input","input exam grade three:",parent=tk.Tk().withdraw()))

grades = [exam_one,exam_two,exam_three]
sum = 0
for grades in grades:
  sum = sum + grades

avg = sum / grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grades in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if (letter-grade) is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
