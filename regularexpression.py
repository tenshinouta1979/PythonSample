#https://docs.python.org/3/library/functions.html
#regular expression
import re

# Sample text with emails and phone numbers
text_to_search = """
Hello, please contact us at support@example.com or sales@example.net.
For urgent queries, call +1-555-1234 or (555) 123-4567.
"""

# Regular expression pattern for matching email addresses
# where r'' escapes back slash to avoid \\\\\\\\\
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Regular expression pattern for matching phone numbers
phone_pattern = r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

# Find all email addresses
emails = re.findall(email_pattern, text_to_search)
print("Email Addresses Found:")
for email in emails:
    print(email)

# Find all phone numbers
phones = re.findall(phone_pattern, text_to_search)
print("\nPhone Numbers Found:")
for phone in phones:
    print(phone)

#other functions good to know
#s = 'foo123bar'
#'123' in s
#True

#s = 'foo123bar'
#s.find('123')
#3
#s.index('123')
#3

#https://regex101.com/
#https://pythex.org/