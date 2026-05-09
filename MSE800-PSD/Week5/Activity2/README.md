![Screenshot](<usecase diagram (figure 6.2).png>)

# Overview
This usecase diagram for the NexGen system illustrates the functions of the system. It shows interaction between actors and the use cases the system performs.

* Actors :  
    - Primary Actors : **Cashier, System Administrator, Sales Activity System**. These actors initiate use cases to achieve a goal.
    - Secondary Actors : **Payment Authorization Service, Tax Calculator, Accounting System, HR System**. The system relies on these actors to complete a use case.

* System Boundary : 
The large rectangle **NextGen** defines the scope of the system. Everyting in it is a function that the system performs.

* Use Cases :
The oval shapes represent sequence of actions the system performs to generate a result.

* Communication Lines :
The solid lines represent interactions between actors and use cases. For example : a __Cashier__ interacts with __Process Sales__, which communicates with __Tax Calculator__ and __Accounting System__.

# Recommendation for improvement.
### 1. Uniform notaion
The diagram uses two different notaions for computer systems : a stick figure for __Payment Authorization Service__, and rectangle for __Tax Calculator__, __Accounting System__.

_Improvement_ : A consistent notation for all computer systems (non-human actors) makes the diagram clearer. Stick figures can be used for human actors and __<\<actor>>__ for computerized systems.

### 2. Relationship
The system uses many external systems for use cases but it dosent show how they relate to each other.

_Improvement_ : A use case Process Sale requries a tax calculator and payment authorization service. These external tasks can be represented as a use case (inside a ovel) and then an __<\<include>>__ relationship can be used amongst these.