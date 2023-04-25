import os
from bs4 import BeautifulSoup

# Path to the HTML file to be used as a database
DB_PATH = "./index.html"


# Function to check if the database file exists and create it if it does not
def check_db() -> None:
    # Check if the database file exists
    if os.path.exists(DB_PATH):
        print(f"db '{DB_PATH}' already exists")
        with open(DB_PATH, "r") as f:
            content = f.read()
        if BeautifulSoup(content, "html.parser").find("table") == None:
            # If the file does not contain a table element, add one to the file
            with open(DB_PATH, "w") as f:
                f.write("<table><tr><th>ID</th><th>Name</th><th>Description</th><th>Price</th></tr></table>")
    else:
        # If the file does not exist, create it and add a table element to it
        with open(DB_PATH, "w") as f:
            f.write("<table><tr><th>ID</th><th>Name</th><th>Description</th><th>Price</th></tr></table>")
        print(f"db '{DB_PATH}' created")

if __name__ == '__main__':
    check_db()