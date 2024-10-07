# Asset Vision

**Asset Vision** is a web-based asset management system designed to help enterprises keep track of their IT assets efficiently. This project leverages **Django** as the backend framework and integrates **React** for a modern, dynamic user interface.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [CSS Styling](#css-styling)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)


## Features
- **Dashboard:** Visual representation of assets and their status.
- **Asset Tracking:** Add, update, and manage assets across locations.
- **Predictive AI:** Insights into asset performance and lifecycle for proactive management.
- **User Management:** Role-based access control for admins and employees.

## Technology Stack
- **Backend:** Django, Python
- **Frontend:** React, JavaScript
- **Database:** MongoDB (`mongodb://localhost:27017/asset-vision`)
- **Other Tools:** Docker, Git

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js
- MongoDB (running locally)
- Git

### Backend Setup (Django)
1. Clone the repository:
    ```bash
    git clone https://github.com/sandeepnadesan/asset-vision.git
    cd asset-vision
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Set up MongoDB:
    Ensure MongoDB is running on `mongodb://localhost:27017/asset-vision`.

4. Run Django migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup (React)
1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install the frontend dependencies:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```


