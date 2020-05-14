#Item 37 - Classes vs Nesting levels
class SimpleGradebook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grades(self, name, score):
        self._grades[name].append(score)
    
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grades('Isaac Newton', 90)
book.report_grades('Isaac Newton', 95)
book.report_grades('Isaac Newton', 85)

print(book.average_grade('Isaac Newton'))
print(book._grades)

#Overextending Classes
from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
    
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book_subject = BySubjectGradebook()
book_subject.add_student('Albert Einstein')
book_subject.report_grade('Albert Einstein', 'Math', 65)
book_subject.report_grade('Albert Einstein', 'Math', 75)
book_subject.report_grade('Albert Einstein', 'Gym', 90)
book_subject.report_grade('Albert Einstein', 'Gym', 95)
print(book_subject._grades)
print(book_subject.average_grade('Albert Einstein'))
            
class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grades(self, name, subject, grade, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((grade, weight))        

    def average_grade(self, name):
        by_subject = self._grades[name]
        
        sum_grades, count_grades = 0, 0
        for subject, grades in by_subject.items():
            subject_avg, total_weight = 0, 0
            for grade, weight in grades:
                subject_avg += grade * weight
                total_weight += weight
                
            sum_grades += subject_avg / total_weight
            count_grades += 1
            
        return sum_grades / count_grades

book_weight = WeightedGradebook()
book_weight.add_student('Albert Einstein')
book_weight.report_grades('Albert Einstein', 'Math', 65, 0.15)
book_weight.report_grades('Albert Einstein', 'Math', 75, 0.05)
book_weight.report_grades('Albert Einstein', 'Math', 70, 0.80)
book_weight.report_grades('Albert Einstein', 'Gym', 100, 0.40)
book_weight.report_grades('Albert Einstein', 'Gym', 85, 0.60)
print(book_weight._grades)
print(book_weight.average_grade('Albert Einstein'))

#Solution - Refactoring to classes
#starting from the bottom of the tree using tuples for grades and weights
grades = []
grades.append((95, 0.45))
grades.append((85, 0.55))
grades

total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight

#to add info to the grades i need to rewrite (problem)
grades = []
grades.append((95, 0.45, 'great job'))
grades.append((84, 0.55, 'better next time'))
total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight for _, weight, _ in grades)
average_grade = total / total_weight

#solution
from collections import namedtuple

Grade = namedtuple('Grade', ('score', 'weight'))

#creating the class again, now using our new variable
class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
    
    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)
    
    def get_subject(self, name):
        return self._subjects[name]
    
    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)
    
    def get_student(self, name):
        return self._students[name]
    
book = Gradebook()
albert = book.get_student('Albert Einstein')
math = albert.get_subject('Math')
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
albert.average_grade()