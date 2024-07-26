import pandas as pd
import mysql.connector

# Read the CSV file
csv_file = r'E:\TypePhase\ZomatoProject\task-vsatyakiran\dataset\restaurant.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file, encoding='latin1')

# Set up the database connection to MySQL
db_config = {
    'user': 'username',  
    'password': 'password',  
    'host': 'localhost',
    'database': 'zomato_db'  
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Insert data into the database
for index, row in df.iterrows():
    sql = """
    INSERT INTO restaurant (id, name, country_code, city, address, locality, locality_verbose, 
                             longitude, latitude, cuisines, average_cost_for_two, currency, 
                             has_table_booking, has_online_delivery, is_delivering_now, 
                             switch_to_order_menu, price_range, aggregate_rating, rating_color, 
                             rating_text, votes) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        row['Restaurant ID'],
        row['Restaurant Name'],
        row['Country Code'],
        row['City'],
        row['Address'],
        row['Locality'],
        row['Locality Verbose'],
        row['Longitude'],
        row['Latitude'],
        row['Cuisines'],
        row['Average Cost for two'],
        row['Currency'],
        row['Has Table booking'],
        row['Has Online delivery'],
        row['Is delivering now'],
        row['Switch to order menu'],
        row['Price range'],
        row['Aggregate rating'],
        row['Rating color'],
        row['Rating text'],
        row['Votes']
    )
    cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()
