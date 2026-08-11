# 📘 Assignment: Python Algorithms

## 🎯 Objective

Learn how to solve problems using search and sorting algorithms in Python, and practice applying those techniques to list-based challenges.

## 📝 Tasks

### 🛠️ Implement Linear Search

#### Description
Write a function called `linear_search()` that looks for a target value in a list and returns its index.

#### Requirements
Completed program should:

- Accept a list and a target value as arguments.
- Search each element in the list from left to right.
- Return the index of the first matching value, or `-1` when the target is not found.
- Example:

```python
print(linear_search([4, 7, 2, 9], 7))  # 1
print(linear_search([4, 7, 2, 9], 5))  # -1
```

### 🛠️ Implement Bubble Sort

#### Description
Write a function called `bubble_sort()` that sorts a list of numbers in ascending order using the bubble sort algorithm.

#### Requirements
Completed program should:

- Accept a list of numbers as an argument.
- Repeatedly compare and swap adjacent items until the list is sorted.
- Return a new sorted list without modifying the original list.
- Example:

```python
print(bubble_sort([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]
```

### 🛠️ Apply Algorithms to a Problem

#### Description
Write a function called `find_student_score()` that uses a search algorithm to find a student’s score from a list of records.

#### Requirements
Completed program should:

- Accept a list of student records and a student name.
- Each record should be a tuple in the form `(name, score)`.
- Return the score for the given student name, or `None` if the student is not found.
- Example:

```python
students = [('Ava', 88), ('Liam', 76), ('Mia', 92)]
print(find_student_score(students, 'Mia'))  # 92
print(find_student_score(students, 'Noah'))  # None
```
