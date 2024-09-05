* * * * *

Chatbot 
===================

Overview
--------

This project consists of a chatbot application with a backend powered by Flask and a frontend built with React. The chatbot uses a machine learning model to generate responses based on user input.

Project Structure
-----------------

-   **Backend**:

    -   **Flask Server**: Handles requests, processes user input, and interacts with the machine learning model.
    -   **Files**: `app.py`, `chatbot_model.h5`, `intents.json`, `words.pkl`, `classes.pkl`
-   **Frontend**:

    -   **React App**: Provides the user interface for interacting with the chatbot.
    -   **Files**: `Chatbot.js`, `index.js`

Setup and Installation
----------------------

### Backend

1.  **Clone the Repository:**

    

    `git clone <repository-url>
    cd <repository-directory>`

2.  **Create and Activate Virtual Environment:**

    

    `python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate``

3.  **Install Dependencies:**

    
    `pip install -r requirements.txt`

4.  **Run the Flask Server:**

    

    `python app.py`

    The server will run on `http://127.0.0.1:5000`.

### Frontend

1.  **Navigate to Frontend Directory:**

    

    `cd frontend`

2.  **Install Dependencies:**

   

    `npm install`

3.  **Run the React App:**

    

    `npm start`

    The React app will run on `http://localhost:3000`.

Usage
-----

1.  **Start the Backend Server:** Make sure the Flask server is running and accessible at `http://127.0.0.1:5000`.

2.  **Start the Frontend App:** Launch the React application, which will interact with the backend server.

3.  **Interact with the Chatbot:** Open `http://localhost:3000` in your browser. Enter a message in the chat input field and hit enter to receive a response from the chatbot.


Contributing
------------

Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue on the GitHub repository.
