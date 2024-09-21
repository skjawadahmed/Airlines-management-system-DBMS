# Airlines-management-system-DBMS ✈

## Overview 🛫
This project is an Air Reservation System built using Python's Tkinter for the GUI and MySQL for the database management. It allows users to manage flights, tickets, passengers, and additional essentials associated with air travel. 
This project was developed to enhance understanding of database management system (DBMS) concepts using MySQL. It serves as a practical application for managing airline reservations, focusing on CRUD operations, user authentication, and data integrity.

## Features 🛫
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
   git clone https://github.com/skjawadahmed/Airlines-management-system-DBMS.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install pymysql
   ```
3. **Set Up MySQL Database**:
   - Use the Queries for MySQL file to Create a database named `airlines`.
   - and also create the following tables with appropriate fields use the txt file which has the queries:
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
   python project.py
   ```

## Usage
1. Launch the application.
2. Log in with the following credentials:
   - Username: `admin`
   - Password: `login@123`
3. Use the navigation buttons to manage passengers, tickets, flights, and essentials.

## Contributing
Feel free to contribute to this project by forking the repository and submitting a pull request. Please make sure to update tests as appropriate.

## Screenshots
### login Page:
![Screenshot 2024-09-21 225941](https://github.com/user-attachments/assets/867fb385-e8fb-419e-a814-c3d78eb344a8)
### Main Home Page:
![Screenshot 2024-09-21 230000](https://github.com/user-attachments/assets/d7a78774-8aba-494f-9ca2-c1848be2896b)
### User Details Entering Page:
![Screenshot 2024-09-21 230119](https://github.com/user-attachments/assets/86e078c7-6203-48d1-830a-b12fc9d4a949)
### User Details Deleting Page:
![Screenshot 2024-09-21 230309](https://github.com/user-attachments/assets/6bdec936-94b9-40d4-93c0-1e86dc44f782)
### DATABASE TABLES & DETAILS ENTERED BY USER :
![Screenshot 2024-09-21 231353](https://github.com/user-attachments/assets/02e59d8e-38f2-448b-9784-a2813b2092e5)
![Screenshot 2024-09-21 231427](https://github.com/user-attachments/assets/c077b980-3f19-4d64-b85c-eb31ec5f8333)

### Future Improvements

1. **User Authentication**: Implement password hashing for security.
2. **Input Validation**: Add checks for user inputs to prevent errors.
3. **Error Handling**: Enhance handling of database and SQL errors.
4. **UI Enhancements**: Redesign the interface for better usability.
5. **Search Functionality**: Enable searching and filtering of records.
6. **Data Export**: Add options to export data to CSV or Excel.
7. **Logging**: Introduce logging for monitoring and debugging.
8. **Unit Testing**: Write tests for critical functions.
9. **Documentation**: Improve inline comments and documentation.
10. **Multi-user Support**: Expand roles with varying permissions.
11. **Performance Optimization**: Optimize queries and use connection pooling.
12. **Mobile Responsiveness**: Ensure usability on mobile devices.


