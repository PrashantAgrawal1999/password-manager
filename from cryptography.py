import sqlite3
from cryptography.fernet import Fernet

# Generate a key instantiate a Fernet instance
key =  Fernet.generate_key()
cipher_suite = Fernet(key)
def encrypt_password(password: str) -> bytes:
    return cipher_suite.encrypt(password.encode())

def decrypt_password(encrypted_password: bytes) -> str:
    return cipher_suite.decrypt(encrypted_password).decode()

def store_password(service: str, username: str, password: str):
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)',
              (service, username, encrypted_password))
    conn.commit()
    conn.close()

    def retrieve_passwords(service: str, username: str) -> str:
     conn = sqlite3.connect('passwords.db')
     c = conn.cursor()
     c.execute('SELECT password FROM passwords WHERE service = ? AND username = ?', (service, username))
    result = c.fetchone()
    conn.close()
    if result:
        return decrypt_password(result[0])
    else:
        return None
    
    
    
    
def main():
    while True:
        print("Password Manager")
        print("1. Store a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            store_password(service, username, password)
            print("Password stored successfully!")
        elif choice == '2':
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = retrieve_password(service, username) # type: ignore
            if password:
                print(f"Password for {username} on {service} is: {password}")
            else:
                print("No password found for the given service and username.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "  main  ":
  main()


