# Airlines-management-system-DBMS

## Overview
This project is an Air Reservation System built using Python's Tkinter for the GUI and MySQL for the database management. It allows users to manage flights, tickets, passengers, and additional essentials associated with air travel.

## Features
- **User Authentication**: Admin login with validation.
- **Passenger Management**: Add, view, and delete passenger details.
- **Ticket Management**: Book and delete tickets.
- **Flight Management**: Add and remove flight details.
- **Essentials Management**: Manage food and drink orders associated with flights.

## Technologies Used
- Python
- Tkinter (for GUI)
- PyMySQL (for MySQL database connection)

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)
- PyMySQL (install via pip)
- MySQL Server

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/AirReservationSystem.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install pymysql
   ```
3. **Set Up MySQL Database**:
   - Create a database named `airlines`.
   - Create the following tables with appropriate fields:
     - `Passenger`
     - `Ticket`
     - `Flight`
     - `Essential`

4. **Configure Database Connection**:
   Update the database connection details in the code:
   ```python
   db = pymysql.connect(host='localhost', user='root', passwd='your_password', db='airlines', autocommit=True)
   ```

5. **Run the Application**:
   Execute the main script:
   ```bash
   python main.py
   ```

## Usage
1. Launch the application.
2. Log in with the following credentials:
   - Username: `admin`
   - Password: `login@123`
3. Use the navigation buttons to manage passengers, tickets, flights, and essentials.

## Contributing
Feel free to contribute to this project by forking the repository and submitting a pull request. Please make sure to update tests as appropriate.


