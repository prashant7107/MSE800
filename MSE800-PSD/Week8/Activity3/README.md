![Class diagram](Week%208%20Activity%203%20class%20diagram.drawio.png)

# Air New Zealand Flight Management System (Single Inheritance)

This project simulates backend for an Air New Zealand flight. It demonstrates **Single Inheritance**, **Encapsulation**, and **Method Overriding (Polymorphism)**.

---

## Overview

The system models differences between a international flight and a domestic flight. A subclass inherits from a parent class while modifying security, documentation, and pricing behaviors to match domestic aviation rules.

### OOP Concepts
* **Single Inheritance:** `DomesticFlight` derives directly from `Flight` (an "IS-A" relationship), sharing its fields and behaviors.
* **Encapsulation:** Attributes use private convention naming (`_variable`) to protect internal object states from unauthorized external modification.
* **Method & Attribute Overriding:** The subclass redefines specific elements inherited from the parent to adapt international travel mandates (like mandatory passports and visas) to domestic travel (valid photo ID, no visas).

---


##  Class Architecture

### 1. Parent Class: `Flight`
Represents a baseline flight configuration.
* **Private Attributes:** * `_flight_number` (String)
  * `_origin` / `_destination` (String)
  * `_aircraft_type` (String)
  * `_base_price` (Float)
  * `_required_document` (String, defaults to `"Passport"`)
  * `_scheduled_departure` / `_scheduled_arrival` (DateTime)
  * `_flight_status` (String)
  * `_total_seats` (Integer)
* **Public Methods:**
  * `display_basic_info()`: Outputs basic information.
  * `check_visa_requirement()`: Prints international warnings.
  * `verify_identity(document_type)`: Passport-only gate access.

### 2. Subclass: `DomesticFlight`
Inherits entirely from `Flight` while introducing domestric details.
* **Extended Private Attributes:**
  * `_domestic_terminal` (String)
  * `_baggage_allowance_domestic` (String)
  * `_fare_product` (String)
* **Overridden Properties & Methods:**
  * Overrides `_required_document` to `"Any Valid Photo ID"`.
  * Overrides `check_visa_requirement()` to pass local travelers.
  * Overrides `verify_identity(document_type)` to authorize local ID types (e.g., NZ Driver License).
* **Unique Subclass Method:**
  * `apply_domestic_discount()`: Applies a lcoal 15% price deduction.

---
