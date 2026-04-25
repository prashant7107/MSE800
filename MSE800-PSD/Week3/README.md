# Student-Course Database Design

This repository contains an Entity-Relationship (ER) diagram for relationship between students and their academic courses. 

The design illustrates a Many-to-Many (M:N) relationship where:  
A Student can enroll in multiple courses.  
A Course can contain many different students.

## Entities & Attributes
Student: Contains personal details (student_id, first_name, last_name, email).  
Course: Contains course-specific information (course_code, title, credit).  
Enrolled In: Relationship that bridges Students and Courses.  

## Update
New Entity: A Lecturer entity has been introduced to track details about the teaching staff.  

Relationship: We established a M:N (Many-to-Many) relationship, Teaches, between Lecturers and Course.