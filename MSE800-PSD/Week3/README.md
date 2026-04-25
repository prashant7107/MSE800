# Student-Class Database Design

This repository contains an Entity-Relationship (ER) diagram for relationship between students and their academic courses. 

The design illustrates a Many-to-Many (M:N) relationship where:  
A Student can enroll in multiple classes.  
A Class can contain many different students.

## Entities & Attributes
Student: Contains personal details (student_id, first_name, last_name, email).  
Class: Contains course-specific information (course_code, title).  
Enrolled In: Relationship that bridges Students and Classes.  