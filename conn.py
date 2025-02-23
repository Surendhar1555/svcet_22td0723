import pyodbc

# Define connection string
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DJ_WORKSTATION;"
    "DATABASE=data.py;"
    "UID=your_username;"
    "PWD=your_password;"
    "Trusted_Connection=yes;"
)

# Create a cursor
cursor = conn.cursor()