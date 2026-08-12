import re

email = input("Enter your email: ")

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.match(pattern, email):
    print("✅ That looks like a valid email!")
else:
    print("❌ That doesn't look like a valid email.")





