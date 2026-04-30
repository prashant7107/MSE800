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
 


---
---

# Finance Money Exchange ER Diagram Design
ER diagram for a money exchange system. 

## Entity Breakdown:
__Branches:__ Represents physical service locations. Attributes include branchID, location, agentName, valueLimit (for cash management), and status (operational or not).  

__Customers:__ Manages client identity. Attributes include customerID, fullName, nationality, and document verification details (documentType, documentNumber).  

__Receipts:__ The central transaction log. Attributes include receiptsID, paidAmount, receivedAmount, and a timestamp. It acts as the bridge between branches and customers.  

__Currencies:__ A master list of supported global currencies. Attributes include currencyID, currencyName, unitName, minorUnitName, and boolean flag like isExchangeOk (if exchange is allowed).  

__Market Rates:__ A dynamic table for live pricing. Attributes include rateID, buyRate, sellRate, and links to the specific currency pairs being traded.

## Relationship Logic:
__serves (M:N):__ A branches interact with many customers, and customers may visit different branches.  

__issues (1:N):__ Each physical branch manages issues multiple unique receipts, while each receipt is tied to a single point of sale.  

__receives (1:N):__ Ensures all transactions are assigned to a verified customer.  

__applies (N:1):__ Multiple transactions occurring within the same price window can reference a single market rate record, maintaing consistency in the exchange calculations.  

__defines (1:N):__ A single currency (e.g., USD) can be part of many different rate definitions (USD/EUR, USD/GBP).

