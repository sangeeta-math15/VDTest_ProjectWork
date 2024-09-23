import csv
import re


def is_valid_email(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)


def clean_data(input_file, output_file):
    users_dict = {}

    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row['user_id']
            email = row['email']
            if user_id not in users_dict and is_valid_email(email):
                users_dict[user_id] = row

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=users_dict[user_id].keys())
        writer.writeheader()
        for user in users_dict.values():
            writer.writerow(user)


clean_data('user_data.csv', 'cleaned_users.csv')
