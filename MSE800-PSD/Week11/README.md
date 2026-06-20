# Assessment 2: Local Food Co-op & Crop Share Network

## Project Requirements & Traceability Documentation

This repository contains the core software architecture, implementation files, and requirement specifications for the Food Redistribution Cooperative System. The platform is designed to streamline supply chains, stabilize pricing, manage inventory lifecycles, and ensure equitable access to fresh food within the community through a tiered subsidy model.

---

## 1. System Requirements Specification

### 1.1 Functional Requirements (FR)
Functional requirements define the core behaviors, services, and processing logic that the cooperative platform must perform.

| Requirement ID | Requirement Title | Description | Implementation (Files/Modules) |
| :--- | :--- | :--- | :--- |
| **FR-01** | **Harvest Registration** | Provides a secure portal for verified Growers to log real-time crop yields, quantities, and harvest dates, keeping inventory records accurate and up to date. | `views/grower_dashboard.py`<br>`controllers/harvest_controller.py`<br>`repositories/harvest_repository.py` |
| **FR-02** | **Market Price Synchronization** | Automatically integrates with external retail benchmarks and APIs to pull real-time market data, ensuring pricing remains competitive across the cooperative. | `services/price_sync_service.py`<br>`repositories/price_repository.py` |
| **FR-03** | **Box Allocation & Distribution** | Manages the entire lifecycle of food boxes, tracking stock from its initial unallocated state through to recipient claiming and final distribution. | `views/distribution_view.py`<br>`controllers/box_manager.py`<br>`repositories/box_repository.py` |
| **FR-04** | **Tiered Subsidy Application** | Algorithmic execution of discount percentages automatically calculated based on a household's verified income tier to guarantee equitable financial access. | `services/subsidy_service.py`<br>`controllers/coop_manager/` |
| **FR-05** | **Role-Based Access Control (RBAC)** | Custom, streamlined user interfaces tailored specifically for **Growers**, **Workers**, and **Recipients** to restrict data access, display relevant tools, and minimize human error. | `views/auth_view.py`<br>`services/security_service.py`<br>`decorators.py` |

---

### 1.2 Non-Functional Requirements (NFR)
Non-functional requirements specify the technical standards, quality attributes, and engineering constraints that the platform must satisfy.

| Requirement ID | Technical Attribute | Technical Strategy | Implementation (Files/Modules) | Description |
| :--- | :--- | :--- | :--- | :--- |
| **NFR-01** | **Accessibility & Inclusivity** | Thin-Client architecture / Lazy Fetching patterns. | `views/*.py`<br>`repositories/*.py` | Ensures the platform runs efficiently on older legacy hardware and in low-bandwidth or cellular environments, remaining fully accessible to all community members. |
| **NFR-02** | **Data Integrity** | Repository Pattern with strictly defined Transactional Boundaries. | `repositories/*.py` | Implements transactional safeguards to prevent database corruption during high-traffic events, ensuring concurrent operations (e.g., multiple users claiming boxes simultaneously) are either fully completed or safely rolled back. |
| **NFR-03** | **Maintainability** | 3-Tier Separation of Concerns architecture. | `views/*.py`<br>`controllers/coop_manager/*.py`<br>`repositories/*.py`<br>`services/*.py` | Organizes the codebase using a modular pattern to separate business logic from data access, allowing components to be tested in isolation and the underlying database engine upgraded seamlessly. |
| **NFR-04** | **Robustness** | Defensive Programming & Global Exception Interception. | `decorators.py` | Prioritizes graceful failure modes by intercepting runtime errors to provide users with clear, actionable feedback or default safe states rather than exposing raw system errors. |
| **NFR-05** | **Security** | One-Way Cryptographic Hashing & Verification. | `services/security_service.py` | Protects user identities, sensitive profiles, and active credentials by hashing all authentication data using the industry-standard Bcrypt protocol. |

---

## 2. Core Algorithms & Third-Party Services

To handle complex logistics and data verification safely, the system utilizes specialized core services and algorithmic processing engines:

### 📍 OpenStreetMap (OSM) & OSRM Engine (Delivery Runs)
* **Service Integrated:** **OpenStreetMap API** via the **Open Source Routing Machine (OSRM)**.
* **Algorithm Used:** **Dijkstra’s Algorithm / Contraction Hierarchies** (via OSRM backend).
* **Application Context:** Located in `services/routing_service.py`. When an allocation worker generates a "Delivery Run" for claimed food boxes, the service fetches coordinates for recipient addresses, computes a distance-destination cost matrix, and returns an ordered waypoint sequence. This eliminates manual dispatch planning and optimizes multi-stop driver paths.

### 📦 Greedy Bin-Packing Optimization Algorithm (Box Assembly)
* **Algorithm Used:** **First-Fit Decreasing (FFD) / Greedy Bin Packing**.
* **Application Context:** Located in `services/box_packing_service.py`. When building standard distribution boxes from raw harvest logs, this algorithm auto-allocates stock items by grouping incoming produce based on weight capacities (e.g., max 10kg per box), food variety categories (ensuring an even mix of greens, root vegetables, and fruits), and expiration prioritization (First-Expired, First-Out / FEFO) to maximize the utility of perishable stock.

### 🔄 Market Price Aggregation & Filtering Algorithm
* **Algorithm Used:** **Moving Average Filtering & Outlier Rejection**.
* **Application Context:** Located in `services/price_sync_service.py`. When pulling wholesale benchmark rates from external grocery/commodity endpoints, the synchronization engine runs an outlier rejection script to ignore abnormal API spikes or null returns, computing an adjusted moving average baseline to set uniform cooperative distribution rates.

### 🔐 Cryptographic Identity Service
* **Service Used:** **Bcrypt Hashing Routine**.
* **Application Context:** Located in `services/security_service.py`. Rather than relying on simple MD5 or SHA algorithms, the system implements adaptive key-stretching salts via Bcrypt to store non-reversible user passwords, preventing rainbow-table access threats during standard database audits.

---

## 3. Directory & Module Mapping Overview

The directory layout below highlights the structural separation of concerns and explicitly shows where each requirement is implemented within the system codebase:

```text
├── controllers/
│   ├── coop_manager/          # Implements Tiered Subsidy processing logic (FR-04)
│   ├── box_manager.py         # Controls lifecycle allocation workflows (FR-03)
│   └── harvest_controller.py  # Handles data verification logs for growers (FR-01)
├── repositories/
│   ├── box_repository.py      # Transactional boundaries for inventory data integrity (NFR-02)
│   ├── harvest_repository.py  # Handles core ingestion of real-time harvest records (FR-01)
│   └── price_repository.py    # Standardizes internal synced benchmark references (FR-02)
├── services/
│   ├── price_sync_service.py  # External data benchmark pull engines (FR-02)
│   ├── security_service.py    # Bcrypt cryptography and access control handling (FR-05, NFR-05)
│   └── subsidy_service.py     # Income verification matrix calculation engine (FR-04)
├── views/
│   ├── auth_view.py           # Interface routing based on user profiles (FR-05)
│   ├── distribution_view.py   # Allocation layout interfaces optimized for users (FR-03)
│   └── grower_dashboard.py    # Thin-client, responsive portal view for legacy hardware (NFR-01)
└── decorators.py              # Central exception interception and RBAC handling (NFR-04, FR-05)