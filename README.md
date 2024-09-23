# VDTest_ProjectWork

# Technical Assessment 

## Overview

This repository contains various tasks such as web scraping, data processing, and implementing features in Django.

## Table of Contents

- [Requirements](#requirements)
- [Dependencies:](#Dependencies:)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)



## Requirements

All the installed packages and their versions are listed in the requirements.txt file, which serves as a record of the project dependencies.

### Dependencies:

- asgiref==3.8.1
- beautifulsoup4==4.12.3
- certifi==2024.8.30
- charset-normalizer==3.3.2
- Django==5.1.1
- djangorestframework==3.15.2
- idna==3.10
- psycopg2-binary==2.9.9
- python-dotenv==1.0.1
- requests==2.32.3
- soupsieve==2.6
- sqlparse==0.5.1
- typing_extensions==4.12.2
- urllib3==2.2.3


## Setup and Installation


1. Clone the Repository:

    ```bash
   git clone https://github.com/sangeeta-math15/VDTest_ProjectWork.git

2. Navigate to the root directory of your Django project using the terminal or command prompt.

    ```bash
   cd myproject

3. Create and Activate a Virtual Environment
   ```bash 
   python3 -m venv venv
   source venv/bin/activate

4. Install the dependencies from the requirements.txt file:

    ```bash
    pip install -r requirements.txt


5. Database Configuration:

   Open the settings.py file in your Django project and update the DATABASES setting with your Postgresql database credentials.
    ```bash
   python DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',

           'NAME': 'database name',     # Replace with your database name
           'USER': 'your username',     # Replace with your MySQL server username
           'PASSWORD': 'your password', # Replace with your database password
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }


7. Apply migrations:

    ```bash
       python manage.py migrate
    

8. Run the server:

    ```bash 
        python manage.py runserver
   
# Running- Python Scripts
1. **Web Scraper** :-
This script scrapes the latest news articles (titles and URLs) from a news website using BeautifulSoup and requests.

Run the script:

```bash
python python_script/web_scraping.py
```
2. **CSV Data Processor**:- This script processes a CSV file with user data:
Removes duplicate entries based on user_id.
Filters out rows with invalid email formats.
Writes cleaned data to a new CSV file.
- Run the script:

```bash
python python_script/cleaned_users.csv 
```
the clean data to new CSV file is located in the ```python_script/cleaned_users.csv``` .


3. **Top 5 Customers Query** :- 
The Django model Order contains fields such as customer, order_date, status, and total_amount. The method retrieves the top 5 customers who spent the most in the last 6 months.

To test this:

- Run the Django server:

```bash
python manage.py runserver
```

- **URL**:  `http://127.0.0.1:8000/api/top-customers/`
- **Method**: `GET`
- **Explanation**: This response Accessing the top customers


4. **Rate Limiter**
This Python script implements a rate limiter that limits each user to a maximum of 5 requests per minute.

- Run the script:

```bash
python  python_script/rate_limit.py
```

5. **Data Aggregator**
The script aggregates values from a list of dictionaries based on a provided key and applies an aggregator function. The function takes in:
- data: A list of dictionaries.
- key: The key by which to group the data.
- aggregator: The function to aggregate the values.

- Run the script:

```bash
python  python_script/aggregate_data.py
```

6. **Finding Duplicate in Array**
This Python script finds the duplicate number in an array with O(1) extra space.

- Run the script:

```bash
python scripts/find_duplicate.py
```

   
