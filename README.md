# Email Sender Project

This project is a simple Python script that sends an email using the Gmail SMTP server. The script uses the `smtplib` and `ssl` libraries to securely send an email from a specified sender to a recipient.

## Prerequisites

Before you can run this script, you need to have:

1. Python installed on your machine.
2. An active Gmail account.
3. An app-specific password for your Gmail account.

## Setting Up

1. **Clone the Repository:**

   Clone this repository to your local machine.

2. **Install Required Libraries:**

   Make sure you have `smtplib` and `ssl` libraries available in your Python environment. These libraries are included in the standard Python library, so no additional installation is needed.

3. **Create a Password File:**

   Create a file named `passw.py` in the same directory as your script. This file should contain a single variable `password` that stores your app-specific Gmail password.

   ```python
   # passw.py
   password = 'your_app_specific_password'
