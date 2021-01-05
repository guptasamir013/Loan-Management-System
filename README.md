# Loan-Management-System

## Installation
1. python -m venv venv
2. venv/Scripts/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Urls
1. Home: '/'
2. Register Staff: 'register_staff/'
3. Update Staff: 'upadte_staff/id/'
4. Delete Staff: 'delete_staff/id/'
5. Profile Staff: 'profile_staff/id/'
6. Register Customer: 'register_customer/'
7. Update Customer: 'upadte_customer/id/'
8. Delete Customer: 'delete_customer/id/'
9. Profile Customer: 'profile_customer/id/'
10. Create Loan Application: 'create_application/'
11. View Loan Application: 'read_application/id/'
12. Update Loan Application: 'update_application/id/'
13. Delete Loan Application: 'delete_application/id/'
14. Login: 'login/'
15. Logout: 'logout/'

## Description
- The Django based Web Application allows the staff members to keep the record of customers and their loan applications
- Groups & Permissions are used to restrict the customers’ access to only view their applications & check approval status
- Implemented Logistic Regression to predict Loan Approval with features like approval history,property,education-81% acc
