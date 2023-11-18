import json

# Read phone book data from a file
def read_phone_book(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Write phone book data to a file
def write_phone_book(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Add a contact to the phone book
def add_contact(phone_book, name, number):
    contact = {'name': name, 'number': number}
    phone_book.append(contact)

# Delete a contact from the phone book
def delete_contact(phone_book, name):
    for contact in phone_book:
        if contact['name'] == name:
            phone_book.remove(contact)
            break

# Update a contact in the phone book
def update_contact(phone_book, name, new_number):
    for contact in phone_book:
        if contact['name'] == name:
            contact['number'] = new_number
            break

"""# Example usage
phone_book_file = 'phone_book.json'
phone_book = read_phone_book(phone_book_file)

add_contact(phone_book, 'John Doe', '1234567890')
add_contact(phone_book, 'Jane Smith', '9876543210')

delete_contact(phone_book, 'John Doe')

update_contact(phone_book, 'Jane Smith', '5555555555')

write_phone_book(phone_book, phone_book_file)
"""