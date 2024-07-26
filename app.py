from flask import Flask, render_template, request, redirect, url_for, jsonify   
import requests
import json

app = Flask(__name__)

# Configuration
original_app_url = 'http://localhost:5001'  # URL of the original Flask app

thumbnails = open("static/data/new_thumbnails.json")
loaded_thumbnails = json.load(thumbnails)

@app.route('/')
def default_route():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    try:
        response = requests.get(f'{original_app_url}/restaurants', params={'page': page, 'per_page': per_page})
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        # Determine the previous and next page numbers
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if len(data) > 0 else None

        return render_template('index.html', restaurants=data, prev_page=prev_page, next_page=next_page, per_page=per_page, loaded_thumbnails=loaded_thumbnails)
    except:
        return "Error", 500

@app.route('/restaurant/<int:restaurant_id>')
def get_restaurant_by_id(restaurant_id):
    try:
        response = requests.get(f'{original_app_url}/restaurant/{restaurant_id}')
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        img_url = None
        for item in loaded_thumbnails:
            if item["Restaurant ID"] == int(restaurant_id):
                img_url = item["featured_image"]
                break
        # print(img_url)
        country = json.load(open("static/data/country.json"))[str(data['country_code'])]
        return render_template('detail.html', restaurant=data, country=country, img_url=img_url)
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}", 500
    
@app.route('/search', methods=['GET'])
def search():
    query_id = request.args.get('query_id').strip()
    if query_id:
        return redirect(url_for('get_restaurant_by_id', restaurant_id=int(query_id)))
    return redirect(url_for('default_route'))

@app.route('/feedbackFunction/<int:restaurant_id>', methods=['POST', 'GET'])
def feedbackFunction(restaurant_id):

    if request.method == 'GET':
        print("Args :", request.args)

        dataRecord = requests.get(f"{original_app_url}/restaurant/{restaurant_id}").json()

        reviewText = str(request.args.get('reviewText').strip())
        currentRating = float(request.args.get('rating'))

        previousCount =  dataRecord["reviewCount"]
        previousRating = float(dataRecord["aggregate_rating"])

        ##logic to update average
        updatedRating = round((previousRating*previousCount + currentRating)/(previousCount+1), 2)

        dataRecord["review_text"] = dataRecord["review_text"] +  ", " + reviewText
        dataRecord['aggregate_rating'] = updatedRating
        dataRecord['reviewCount'] +=1
        print("review Text :", reviewText)

        ##Post request 
        post_request = requests.post(f"{original_app_url}/updatedatabase/{restaurant_id}/{dataRecord['reviewCount']}/{dataRecord['review_text']}/{dataRecord['aggregate_rating']}")
        print(post_request.json())
        return render_template('reviewMessage.html')
    return "Error", 500

if __name__ == '__main__':
    app.run(debug=True)  # Run this app on port 5001
