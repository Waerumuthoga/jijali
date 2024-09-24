# Jijali - Mental Health Web Application

---

## Project Overview

*Jijali* is a mental health web application designed to help users manage their mental well-being through journaling, mood tracking, and graphical analysis. The app provides a platform where users can log their daily emotions, reflect on triggers, and monitor their mental health journey.

### Deployed Application

You can access the live application [here](http://34.46.72.53/).

### Final Project Blog Article

Read more about the development process in my blog [here](https://www.linkedin.com/posts/jeremymuthoga_enhancing-mental-well-being-through-reflective-activity-7244420350346752000-9Jhi?utm_source=share&utm_medium=member_ios).

## Features

- **User Authentication**: Register and log in securely using JWT.
- **Journaling**: Create, view, update, and delete journal entries.
- **Mood Tracking**: Track moods with emojis and reflect on triggers.
- **Graphical Analysis**: Visualize mood patterns and trends over time.
- **Responsive Design**: Optimized for both desktop and mobile use.

## Technology Stack

- **Backend**: FastAPI, PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: PostgreSQL
- **Environment Management**: Python dotenv

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/jijali.git
   cd jijali
2. **Set up a virtual environment:**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install the required packages:**
   pip install -r requirements.txt
   
4. **Set up your environment variables: Create a .env file in the root directory and add your database configuration and secret keys.**

5. **Run the application:**
     uvicorn main:app --reload
**Usage**
Once the application is running, navigate to http://127.0.0.1:8000 in your browser. You can register a new account, log in, and start journaling to enhance your mental well-being.

**Contributing**
Contributions are welcome! If you have suggestions for improvements or want to add features, please open an issue or submit a pull request.
1. Fork the repository.
2. Create your feature branch: git checkout -b feature/AmazingFeature
3. Commit your changes: git commit -m 'Add some AmazingFeature'
4. Push to the branch: git push origin feature/AmazingFeature
5. Open a pull request.

**Licensing**
This project is licensed under the MIT License - see the [LICENSE] file for details.

Thank you for checking out Jijali! Your mental well-being matters.

**Contact**
For any inquiries or issues, feel free to reach out:
- *Email*: waerumuthoga@gmail.com
- *GitHub*: https://github.com/Waerumuthoga
- *LinkedIn*: https://www.linkedin.com/in/jeremymuthoga
