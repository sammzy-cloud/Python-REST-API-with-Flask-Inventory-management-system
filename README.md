## Python REST API with Flask - Inventory Management System

A Python-based inventory management system that provides a Flask REST API, a command-line interface (CLI), and integration with the OpenFoodFacts API.

The system allows users to add, view, update, and delete inventory items, as well as search for and import product information from OpenFoodFacts.

## Features

1.Add inventory items

2.View all inventory items

3.View a single inventory item

4.Update inventory prices and stock levels

5.Delete inventory items

6.Search for products using OpenFoodFacts

7.Import products from OpenFoodFacts

8.RESTful API built with Flask

9.Command-line interface for interacting with the system

10.Unit testing with pytest

11.Mocking external API requests with unittest.mock

12.Error handling for invalid inputs and API failures

## Technologies Used

1.Python

2.Flask

3.Requests

4.pytest

5.unittest.mock

6.OpenFoodFacts API

## Project Structure

Python-REST-API-with-Flask-Inventory-management-system/
│
├── api.py
├── app.py
├── cli.py
├── inventory.py
├── requirements.txt
├── README.md
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_cli.py
│   ├── test_external_api.py
│   └── test_inventory.py
│
└── venv/

## Installation and Setup

1. Clone the repository

git clone https://github.com/sammzy-cloud/Python-REST-API-with-Flask-Inventory-management-system.git

2. Navigate into the project

cd Python-REST-API-with-Flask-Inventory-management-system

3. Create a virtual environment

python3 -m venv venv

4. Activate the virtual environment

On Linux/WSL:

source venv/bin/activate

On Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt


## API Endpoints

/inventory

/inventory/<id>

## Running the CLI

With the virtual environment activated, run:

python cli.py

The CLI provides the following options:

1. Add inventory item
2. View all inventory
3. View one inventory item
4. Update inventory item
5. Delete inventory item
6. Find product on OpenFoodFacts
7. Import product from OpenFoodFacts
8. Exit


## Testing

The project uses pytest for automated testing and unittest.mock for simulating external API responses.

Run the complete test suite with:

pytest

The current test suite contains 9 tests.

Expected result:

9 passed

## Development and Maintainability

The project is separated into different modules to keep responsibilities organized:

app.py contains the Flask API routes.

api.py handles communication with the OpenFoodFacts API.

cli.py contains the command-line interface.

inventory.py contains the inventory data.

tests/ contains the automated test suite.

The project also uses meaningful function and variable names, error handling, and automated tests to make the code easier to maintain and debug.

## Running the Complete Application

### Terminal 1 - Start the Flask API

Activate the virtual environment and run:

source venv/bin/activate
python app.py

Keep this terminal running.

### Terminal 2 - Start the CLI

Open another terminal, navigate to the project directory, activate the virtual environment, and run:

source venv/bin/activate
python cli.py

The CLI will communicate with the Flask API running on:

http://127.0.0.1:5000

## Author

Samantha Ng'iela


