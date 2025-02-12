# URL Shortener

A simple URL shortener built with Flask and SQLite.

## Features
- Shorten long URLs into 6-character short links
- Store URLs in an SQLite database
- Redirect users to the original URL when they visit the short link
- Simple web interface

## Installation
### Prerequisites
Make sure you have **Python 3** installed.

### Clone the Repository
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up the Database
```bash
python -c "from app import init_db; init_db()"
```

### Run the Application
```bash
python app.py
```

Visit **http://localhost:5000** in your browser.

## Usage
1. Enter a long URL in the input field.
2. Click the "Shorten" button.
3. Copy and use the generated short link, which appears on the same page.

## Folder Structure
```
url-shortener/
│── templates/
│   └── index.html
│── app.py
│── urls.db
│── README.md
│── .gitignore
│── requirements.txt
```

## Future Improvements
- Custom short URLs
- User authentication
- Analytics for link tracking


