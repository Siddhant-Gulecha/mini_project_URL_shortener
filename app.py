from flask import Flask, request, jsonify, render_template, redirect  

app = Flask(__name__)

shortened_urls = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    if not long_url:
        return jsonify({'error': 'No URL provided'}), 400

    short_code = str(hash(long_url))[:6]  
    shortened_urls[short_code] = long_url

    full_short_url = f"http://localhost:5000/{short_code}" 
    return jsonify({'short_url': full_short_url})

@app.route('/<short_code>')
def redirect_url(short_code):
    long_url = shortened_urls.get(short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
