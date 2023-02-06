#key/value pairs
customer = {
    "name": 'John Smith',
    "age": 30,
    "is_verfiied": True
}

print(customer["name"])
print(customer.get("Name")) #doesn't return error if the key is not present
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1, 1993"

print(customer)