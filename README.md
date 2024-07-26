### Zomato Restaurant Listing & Searching
 
## Key Use Cases
 
### Data Loading
Created an independent script to load the Zomato restaurant data available [here](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data) into a MySQL database. Script is provided in **script.sql**
Data is loaded into database using python **sqalchamy** , code is provided in **load_data.py** file.
 
### Web API Service
Developed a web API service with the following endpoints to serve the content loaded in the previous step:
  - **Get Restaurant by ID**: Retrieve details of a specific restaurant by its ID.
  - **Get List of Restaurants**: Fetch a list of restaurants with pagination support.
  - APIs are develoved using Flask, all the APIs code is provided in **webapi.py**
 
### User Interface
Developed a web application with the following pages, which must connect to the web API service:
  - **Restaurant List Page**: Display a list of restaurants. Clicking on a restaurant should navigate the user to the restaurant's detail page.
  - **Restaurant Detail Page**: Show details of a specific restaurant.
  - 
 <img width="918" alt="Zomato1" src="https://github.com/user-attachments/assets/5b0acbf3-144e-4f6d-ab80-9a7d07d2ed4e">

<img width="892" alt="Zomato3" src="https://github.com/user-attachments/assets/4f2c97e3-0bcb-4aa0-92ad-d54527fff1c6">

<img width="899" alt="Zomato4" src="https://github.com/user-attachments/assets/9b3bc485-e349-40b4-9b1c-edcf36e94a60">
