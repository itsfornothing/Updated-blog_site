Flask Blog Website
This is a simple blog website built using Flask and i have updated using bootstrap, a lightweight Python web framework. The website allows users to browse blog posts, learn about the author, and send messages through a contact form. The blog content is fetched from an external API.

Table of Contents
Installation
Usage
Features
Project Structure
Environment Variables
Contributing
License
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/flask-blog-website.git
cd flask-blog-website
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory and add your environment variables:

plaintext
Copy code
MY_EMAIL=your_email@gmail.com
PASSWORD=your_email_password
API_ENDPOINT=https://api.example.com/blogs
Run the application:

bash
Copy code
python main.py
The website will be accessible at http://127.0.0.1:5001.

Usage
Home Page: Displays a list of blog posts fetched from an external API.
About Page: Learn more about the author or the website.
Contact Page: Send a message to the author using the contact form. Messages will be sent via email.
Features
Dynamic rendering of blog posts from an API.
Contact form with email integration.
Clean and simple design.
Project Structure
plaintext
Copy code
flask-blog-website/
│
├── templates/
│   ├── index.html        # Home page template
│   ├── about.html        # About page template
│   ├── contact.html      # Contact page template
│   └── post.html         # Blog post detail page template
│
├── main.py               # Main Flask application
├── requirements.txt      # List of Python dependencies
├── .env                  # Environment variables file
└── README.md             # Project README file
Environment Variables
MY_EMAIL: Your Gmail address, used to send emails from the contact form.
PASSWORD: Your Gmail account password or App Password.
API_ENDPOINT: The API endpoint URL from which the blog posts are fetched.
Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
