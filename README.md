<div align="center" style="display: flex; align-items: center; justify-content: center;">
  <img src="https://drive.google.com/uc?export=view&id=1niorO4NvSKA-j6YI4OcgTNHztAXMWv8S" alt="Pet Clinic Logo" width="150" margin-right: 10px;>
  <h1>PetVet - Veterinary Clinic Management System</h1>
</div>




PetVet - Veterinary Clinic Management System is a comprehensive web-based solution designed to streamline operations for veterinary clinics. The system caters to pet owners and veterinary staff, ensuring efficient management of appointments, pet health records, billing, and more.

## 🐾 Project Overview

The PetVet - Veterinary Clinic Management System is designed to simplify the management of both administrative and medical tasks within a veterinary clinic. The system provides a seamless experience for both pet owners and veterinary staff to manage appointments, access medical records, and process payments.

### Key Features:

- **Pet Owners**: Book appointments, view pet health records, and access billing history.
- **Veterinary Staff**: Manage appointments, update pet health records, and generate invoices.

The system is built using **Django** for the backend and **HTML** for the frontend, providing a robust platform for managing clinic operations.

## 🛠️ Technologies Used

### Frontend:
- **HTML**: For the structure of web pages.
- **Bootstrap CSS** and **Tailwind CSS**: For styling and layout of the frontend.
- **JavaScript**: For dynamic client-side functionality and interactivity.

### Backend:
- **Python**: The primary language for backend development.
- **Django**: The web framework for building the backend and managing the database.

## 💾 Database

We are using **SQLite** as the local database for this project. By default, Django comes with SQLite as the backend database, which is lightweight and easy to configure. It is suitable for development and testing purposes. You don't need to install any additional database management systems to get started with this project.

## ⚙️ Features

### User Side (Pet Owners)
- **Owner Registration**: The owner can create an account and update their personal information.
- **Pet Registration**: The owner can register his/her pet/s.
- **Book Appointments**: Schedule consultations for their pets online.
- **Access Medical Records**: View their pets’ vaccination schedules and health history.
- **Billing and Payments History**: Check past appointment bills.

### Vet Side (Management):
- **Vet Profile**: A vet can update his/her profile.
- **Appointment Management**: Track, update, and confirm bookings.
- **Pet Health Records**: Store and manage detailed medical records and procedures.
- **Billing Management**: Generate invoices for completed appointments.
- **Dashboard**: Displays today's appointments, pending appointments, recent medical records, and pending bills. 

## 🚀 Installation

To get started with the Pet Veterinary Clinic System, follow these steps:

### 1. Clone the repository to your local machine:

    git clone https://github.com/karl2522/PetVet-Final.git

### 2. Navigate to the project directory:

    cd PetVet-Final # (Skip this if you're already in the project root)

### 3. Install the dependencies from `requirements.txt`:

    pip install -r requirements.txt

### 4. Apply Database Migrations:

    python manage.py migrate

### 5. Run the Development Server:

    python manage.py runserver








