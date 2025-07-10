## Step 1 

- Clone repository
- Create virtual environment
- Replace host, user and password in **config.py** file with your data

## Step 2 - Installs🔧 
**Before running**, please ensure you have the following installed *(Can also be found in requirements.txt)* :
- python-dotenv
- mysql-connector-python
- requests
- flask

## Step 3 - Environment variable
- Create a `.env` file in the directory
- Create a variable called **API_URL** and store your api's base url as shown ->
<code> API_URL = "Insert your api base url here" </code>

## Step 4 - Database Setup
- Make sure you have the **'affirmations_db'** set up in your mysql *(This SQL file can be found in this Assignment 4 directory)*

## Step 5 - Running the files
1. run db_utils.py
2. run app.py
3. Then run main.py

Follow the prompts to enjoy your daily affirmation, add a new affirmation or view affirmation categories
