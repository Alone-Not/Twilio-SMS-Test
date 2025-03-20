# Install Twilio library if you haven't already:
# pip install twilio

from twilio.rest import Client

# Twilio credentials (replace with your actual credentials)
account_sid = 'your_account_sid_here'  # Replace with your Twilio Account SID
auth_token = 'your_auth_token_here'    # Replace with your Twilio Auth Token
from_phone = 'your_twilio_phone_number'  # Replace with your Twilio phone number
to_phone = 'your_phone_number_here'     # Replace with your personal phone number

# Create Twilio client
client = Client(account_sid, auth_token)

# Send the SMS
message = client.messages.create(
    body="Hello, this is a test message from my Twilio account for personal learning purposes.",
    from_=from_phone,
    to=to_phone
)

# Print message SID (unique identifier for the message)
print(f"Message sent with SID: {message.sid}")
