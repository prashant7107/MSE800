# Overview
This class diagram illustrates the structure and relationships within a Clinic.

## User Hierarchy 
The system uses an inheritance where a  User class contains common attributes like fullName and email is inherited by four roles: Patient, Doctor, ReceptionManager, and PharmacyManager.

## Appointment Scheduling
The Patient gets an appointment through Appointment class. The ReceptionManager manages the availability of these appointments through the Slot class, ensuring that time slots are tracked and validated.

## Clinical Workflow
The Doctor reviews appointments and issues a Prescription when needed. This Prescription then links to a MedicationOrder, which is processed by the PharmacyManager to handle stock checks and medication dispatch.

## Financial Transactions
A patient makes an payment, Payment class tracks billing, payment methods, and the generation of receipts for services.