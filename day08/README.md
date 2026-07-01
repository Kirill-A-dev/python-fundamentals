# Day 08 — Python File Handling

## What I practiced

Today I practiced working with files in Python.

I learned how to:

- write text to a file
- read text from a file
- append new text to an existing file
- generate a report from structured data
- use `with open()` safely
- combine lists, dictionaries, loops, conditions, and file writing

## Files

- `file_write.py` — creates and writes text to `report.txt`
- `file_read.py` — reads content from `report.txt`
- `file_append.py` — adds a new line to `report.txt`
- `student_report.py` — generates a student average report
- `report.txt` — simple text report
- `students_report.txt` — generated student report

## Student report logic

The program uses a list of dictionaries.

Each student has:

- a name
- a list of grades

The program calculates the average grade and assigns a status:

- `excellent` if the average grade is 4.5 or higher
- `good` if the average grade is 3.5 or higher
- `needs improvement` otherwise

## Example output

```text
Alex: average grade = 4.67, status = excellent
Maria: average grade = 5.00, status = excellent
John: average grade = 3.33, status = needs improvement
