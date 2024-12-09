# Library-Management-System
**Introduction**

This is a web-based Library Management System developed using Streamlit and MySQL. It provides functionality for students and administrators to manage library operations such as viewing books, issuing books, and managing book records. The system aims to make library management efficient and reduce manual errors.

**(a) How to Run the Project**

**Prerequisites:-**

Ensure you have Python installed on your system.

**Required Libraries:-**

mysql.connector

streamlit

pandas

datetime

**MySQL Database:**

Set up a MySQL database with the required tables:-

Student: Contains student IDs and passwords.

Books: Stores book records (ID, name, author).

Issue: Tracks issued books (issue ID, book ID, student ID).

Admin: Stores admin credentials

**Running the Application:-**

Navigate to the directory containing the script.

Launch the Streamlit application:streamlit run LMS.py

Open the displayed local URL in your web browser.

**(b) Design Choices Made**

Web Framework:Streamlit was chosen for its simplicity and interactive UI capabilities, allowing quick prototyping and deployment of web applications.

Database:MySQL was used for reliable and structured data storage, with predefined schemas for scalability.

Dynamic Features:The system dynamically retrieves and displays book and issue data using SQL queries.

Modular Features:

Students: View books, issue books.

Admins: Add, delete, and view issued books.

**(c) Assumptions and Limitations**

**Assumptions:-**

Data Validity:

User IDs and passwords are valid and unique.Book IDs and names are consistent and accurate.

Fixed Database Schema:The database schema remains unchanged; modifications would require code updates.

**Limitations:-**

Security:No encryption for sensitive data such as passwords.

Scalability:The application is designed for small-scale library management; large-scale usage might require optimization.

Local Environment:The app is dependent on the local MySQL database and does not support distributed or cloud-based databases.

Static Resource Links:Images and icons are hard-coded with external URLs, which might break if the links are unavailable.
