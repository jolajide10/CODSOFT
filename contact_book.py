import tkinter as tk
from tkinter import messagebox
import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

# Update the list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search contact
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Delete selected contact
def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        del contacts[selected_index]
        save_contacts()
        update_contact_list()
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to delete")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")

contacts = load_contacts()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack()

tk.Label(root, text="Search:").pack()
search_entry = tk.Entry(root)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack()

contact_list = tk.Listbox(root, height=10)
contact_list.pack(fill=tk.BOTH, expand=True)
update_contact_list()

tk.Button(root, text="Delete Contact", command=delete_contact).pack()

tk.Button(root, text="Exit", command=root.quit).pack()

root.mainloop()
