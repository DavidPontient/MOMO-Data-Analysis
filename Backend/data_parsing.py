import xml.etree.ElementTree as ET
import re
from datetime import datetime
import sqlite3
import os

#Eextracts overall xml data from relevant fields
def parse_xml(xml_file):
    """
    Parsing XML file (import at bottom) to get data
    """
    tree_func = ET.parse(xml_file)
    root = tree_func.getroot()
    messages = []
    for sms in root.findall("sms"):
        data = {
            'address': sms.get('address'),
            'date': sms.get('date'), 
            'type': sms.get('type'),
            'body': sms.get('body'),
            'readable_date': sms.get('readable_date')
        }
        messages.append(data)
    return messages

#2.CATEGORISES MESSAGES BASED ON KEYWORDS
def categorize_messages(messages):
    #Message categorisation. This is crucial for finding those key words later on.
    categories = {
        'Incoming-Money': ['received', 'deposit'],
        'Payment Code Holders': ['payment', 'code'],
        'Transfer to Mobile': ['transfer', 'mobile'],
        'Bank Deposit': ['bank deposit'],
        'Airtime Paymnts': ['airtime', 'bill'],
        'Money, Power & Bill Payments': ['cash power', 'bill'],
        'Third Party Transactions': ['third party', 'external'],
        'Agent Withdrawal': ['withdrawal', 'agent'],
        'Banking Transfers': ['bank transfer'],
        'Internet and Voice Bundle Purchases': ['internet', 'voice', 'bundle']
    }

    cat_messages = []
    for msg in messages:
        text = msg['body'].lower()
        msg_category = 'Uncategorized'
        for category, keywords in categories.items():
            if any(keyword in text for keyword in keywords):
                msg_category = category
                break
        msg['category'] = msg_category
        cat_messages.append(msg)
    return cat_messages

#3.Clean extracted Data for readability
def clean_data(messages):
#Clean the data and organises it

    clean_messages = []
    for msg in messages:
        body = msg['body']

        # Extracting (2000 rwf  ---2000) SAME THING
        amount_match = re.search(r'([\d,]+) RWF', body)
        msg['amount'] = int(amount_match.group(1).replace(',', '')) if amount_match else 0

        #Use regex to clean names of ("from Sipho" to Sipho)
        sender_match = re.search(r'from ([A-Za-z ]+?)(?:\s|\()', body, re.IGNORECASE)
        msg['sender'] = sender_match.group(1).strip() if sender_match else 'Unknown'

        # Improved receiver extraction
        receiver_match = re.search(r'to ([A-Za-z ]+?)(?:\s|\d+|\()', body, re.IGNORECASE)
        msg['receiver'] = receiver_match.group(1).strip() if receiver_match else 'Unknown'

        # Extract transaction ID if present
        txid_match = re.search(r'TxId[:]*\s*([\d]+)', body)
        msg['transaction_id'] = txid_match.group(1) if txid_match else 'N/A'

        # Convert timestamp
        msg['date'] = datetime.fromtimestamp(int(msg['date']) / 1000).strftime('%Y-%m-%d %H:%M:%S')

        clean_messages.append(msg)
    return clean_messages


#4.Log Unecessary messages
def log_unprocessed_messages(messages, logs):
    unprocessed = [msg for msg in messages if msg['category'] == 'Uncategorized']
    with open(logs, 'a') as f:
        f.write(f"\n\n--- Unprocessed Messages ({datetime.now().strftime('%Y-%m-%d %H:%M')}) ---\n")
        for msg in unprocessed:
            f.write(f"Date: {msg['readable_date']}\n")
            f.write(f"From: {msg['address']}\n")
            f.write(f"Content: {msg['body']}\n\n")


def insert_into_database(messages, db_connect):
    cursor = db_connect.cursor()
    for msg in messages:
        cursor.execute('''
            INSERT INTO transactions (address, date, type, body, category, amount, sender, receiver, readable_date, transaction_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            msg['address'], msg['date'], msg['type'], msg['body'],
            msg['category'], msg['amount'], msg['sender'], msg['receiver'],
            msg['readable_date'], msg['transaction_id']
        ))
    db_connect.commit()
   


# Set correct paths
xml_file = os.path.join('..', 'Data', 'modified_sms_v2.xml')
db_path = os.path.join(os.path.dirname(__file__), 'transactions.db')
log_file = os.path.join(os.path.dirname(__file__), 'unprocessed_logs.txt')

# Run the pipeline
xml_data = parse_xml(xml_file)
categorized = categorize_messages(xml_data)
cleaned = clean_data(categorized)

# Insert into DB
with sqlite3.connect(db_path) as conn:
    insert_into_database(cleaned, conn)

# Log any uncategorized messages
log_unprocessed_messages(cleaned, log_file)

print(f"✅ Processed and inserted {len(cleaned)} messages into the database.")
