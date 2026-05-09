# Overview
This is an activity diagram to demonstrate workflow in a clinic system that allows patients to book appointment and order medications. It illustrates interaction between Patient, Doctor, Reception and Pharmacy. 

### Appointment Booking and Consultaion
* Initiation : The process begins with patient starting an appointment booking.
* Scheduling : The receptionist verifies if the the slot is available, if its not available the system provides alternative available dates, once the patient is ok a date is confirmed.
* Payment : A booking is confirmed once the payment is made, any issues during transaction is handled and processed accordingly.
* Consultaion : Doctor examins and consults during the booked time slot.
* End : If nmedicine is required, the flow moves towards medication , else the process ends.

### Meidcation
* Order : An order for medication can be placed either by doctor's or directly by a patient. Reception records the order placed.
* Inventory and prescription verification :  The pharmacy processes order and confirms weather stock is available and the prescription is valid.
* Medication Dispense : Only if both condition is verified, the pharmacy places the order and proceed to payment.
