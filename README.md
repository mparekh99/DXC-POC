# Gilded Rose Refactoring Kata Solution

## Overview

This project is a solution to the [Gilded Rose Refactoring Kata](https://kata-log.rocks/gilded-rose-kata). The challenge involved refactoring an existing system that manages inventory for a fictional inn called "Gilded Rose." The system tracks the quality and sell-by dates of various items, with special rules for certain types of items:

- **Aged Brie**: Increases in quality as it ages.
- **Backstage passes**: Increases in quality as the sell-by date approaches, with specific rules for different time frames.
- **Sulfuras**: A legendary item that never decreases in quality.

Additionally, the challenge required adding functionality for **Conjured items**, which degrade in quality twice as fast as normal items.

In this solution, I enhanced the system by allowing users to:
- Upload bulk inventory data through a JSON file.
- Track inventory items dynamically by simulating how their values change over a given number of days.

## Proof of Concept

This project was also built as a practice for **CI/CD (Continuous Integration/Continuous Deployment)** and includes the following steps:

1. **Test Driven Developement**: Created unit tests to illicit the behavior of inventory items, and code accordingly to pass all tests
2. **Code Optimization**: Refactored the code by removing excessive `if-else` statements, improving maintainability, and organizing logic into classes.
3. **Web Application (Django)**: Developed a web app using **Django** to provide a dynamic and interactive interface, allowing users to upload inventory, view, sell, and project item values based on time.

## Technologies Used

- **Django**: For building the web application.
- **Python**: Core programming language for backend development.
- **CI/CD**: Followed the framework, next steps would be moving into Docker and using some sort of automated testing like Jenkins. 
- **JSON**: For handling bulk inventory uploads.
- **Selenium**: For testing UI interactions and ensuring the web app's frontend works as expected.

## Features

- **Bulk Inventory Upload**: Upload a JSON file containing inventory, which will be processed by the system.
- **Dynamic Inventory Tracking**: Enter a number of days to simulate and project how the quality of items changes over time.
- **Interactive GUI**: View and manage inventory items directly from the Django web application interface.
- **Admin Interface**: Use Django’s built-in admin interface to manage inventory with ease.

## Setup and Installation
### Clone Repository
```
git clone https://github.com/mparekh99/DXC-POC.git
cd DXC-POC
```

### Set up an environment
```
python -m venv venv
.\venv\Scripts\activate
```
### Install the required dependencies
```
pip install -r requirements.txt
```
### Apply Migrations to setup Database
```
python manage.py migrate
```
### Create Superuser to access the Django Admin
```
python manage.py createsuperuser
```
### Run the development server
```
python manage.py runserver
```

### Open Server 
```
http://127.0.0.1:8000/
```