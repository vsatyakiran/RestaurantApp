from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
import random
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

app = Flask(__name__)

# Database configuration
db_url = f'mysql+mysqlconnector://{username}:{password}@localhost/zomato_db'  # Replace with your actual MySQL credentials and database name
engine = create_engine(db_url)
metadata = MetaData()
metadata.reflect(bind=engine)
restaurants = metadata.tables['restaurants']
# print(restaurants.)
Session = sessionmaker(bind=engine)
session = Session()

# get columns
columns = tuple(restaurants.columns.keys())

# API Endpoints
@app.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant_by_id(restaurant_id):
    result = session.query(restaurants).filter_by(id=restaurant_id).first()
    if result:
        zip_result = dict(zip(columns, result))
        return jsonify(zip_result) 
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    page = request.args.get('page', 1, type=int)
    # print("Page :", page)
    per_page = request.args.get('per_page', 10, type=int)
    offset = (page - 1) * per_page
    results = session.query(restaurants).offset(offset).limit(per_page).all()
    return jsonify([dict(zip(columns, r)) for r in results])

@app.route('/random', methods=['GET'])
def random_restaurant():
    
    #query all ids from database
    all_ids = session.query(restaurants.columns.id).all()
    random_id = random.choice(all_ids)[0]
    result = session.query(restaurants).filter_by(id=random_id).first()
    if result:
        zip_result = dict(zip(columns, result))
        return jsonify(zip_result) 
    else:
        return jsonify({'error': f'Restaurant {random_id} not found'}), 404


# POST request to update review of a restaurant
@app.route('/updatedatabase/<int:restaurant_id>/<int:review_count>/<string:review_text>/<float:updated_rating>', methods=['POST'])
def update_review(restaurant_id, review_count, review_text, updated_rating):
    result = session.query(restaurants).filter_by(id=restaurant_id).first()
    print("Function Called")
    if result:
        session.query(restaurants).filter_by(id=restaurant_id).update({'reviewCount': review_count, 'review_text': review_text, 'aggregate_rating': updated_rating})
        session.commit()
        return jsonify({'message': 'Review updated successfully'})
    else:
        return jsonify({'error': 'Restaurant not found'}), 404


# @app.route("/check/<int:restaurant_id>/<int:review_count>/<string:review_text>/", methods=['POST', 'GET'])
# def check(restaurant_id="", review_count=1, review_text=""):
#     return jsonify({'message': 'Review updated successfully'})

if __name__ == '__main__':
    app.run(debug=True,  port=5001)
