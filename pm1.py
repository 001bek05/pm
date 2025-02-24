import sqlite3

# Initialize Database
def init_db():
    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            location TEXT,
            date_found TEXT,
            claimed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Add a found item
def report_item():
    name = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location found: ")
    date_found = input("Enter date found (YYYY-MM-DD): ")

    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, category, location, date_found) VALUES (?, ?, ?, ?)",
                   (name, category, location, date_found))
    conn.commit()
    conn.close()
    print("Item reported successfully!")

# Search for lost items
def search_items():
    search = input("Search by name, category, or location: ")
    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE name LIKE ? OR category LIKE ? OR location LIKE ?",
                   (f"%{search}%", f"%{search}%", f"%{search}%"))
    results = cursor.fetchall()
    conn.close()

    if results:
        for item in results:
            print(item)
    else:
        print("No matching items found.")

# View unclaimed items
def view_unclaimed():
    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE claimed = 0")
    results = cursor.fetchall()
    conn.close()

    if results:
        for item in results:
            print(item)
    else:
        print("No unclaimed items available.")

# Claim an item
def claim_item():
    item_id = input("Enter the ID of the item to claim: ")
    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET claimed = 1 WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    print("Item claimed successfully!")

# Main menu
def main():
    init_db()
    while True:
        print("\nLost & Found System")
        print("1. Report a Found Item")
        print("2. Search for a Lost Item")
        print("3. View All Unclaimed Items")
        print("4. Claim an Item")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            report_item()
        elif choice == "2":
            search_items()
        elif choice == "3":
            view_unclaimed()
        elif choice == "4":
            claim_item()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
