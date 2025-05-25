# Youth Unemployment Tracker (YUT)

## Project Overview

The Youth Unemployment Tracker (YUT) is a web application designed to collect, analyze, and visualize data related to youth unemployment. It allows users to submit survey data regarding their employment status, education, and demographic information. The platform aims to provide insights into employment trends among young people, offering valuable data for researchers, policymakers, and individuals.

## Tech Stack

### Backend
*   **Programming Language:** Python
*   **Framework:** Django, Django REST Framework (DRF)
*   **Database:** MySQL
*   **Authentication:** JSON Web Tokens (JWT) via `djangorestframework-simplejwt`
*   **CORS Handling:** `django-cors-headers`

### Frontend (Example Stack - Please update if different)
*   **Framework/Library:** React.js (or Vue.js, Angular)
*   **Languages:** JavaScript, HTML, CSS
*   **State Management:** Redux, Context API (or equivalent)
*   **API Communication:** Axios, Fetch API

### General
*   **Version Control:** Git & GitHub
*   **Virtual Environment:** `venv` (Python)

## Key Features

*   **User Authentication:** Secure user registration and login using JWT.
*   **Survey Submission:** Enables users to submit detailed surveys about their employment situation.
*   **Data Collection:** Gathers information on demographics, education, employment status, job search duration, and income.
*   **Admin Interface:** Django Admin panel for managing users and survey data.
*   **API Endpoints:** RESTful APIs for frontend interaction, data submission, and retrieval.
*   **Data Aggregation:** Backend logic to process and provide summary statistics (e.g., employment rates by state or education level).
*   **(Potential for) Data Visualization:** The collected data can be used to generate charts and graphs on a frontend dashboard.

## Project Setup & Installation (Backend)

Follow these steps to set up the backend of the project locally:

1.  **Clone the Repository:**
    ```bash
    git clone <your-github-repository-url>
    cd YUT-Project
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    ```
    On Windows:
    ```bash
    venv\Scripts\activate
    ```
    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Make sure you have a `requirements.txt` file in the project root.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up MySQL Database:**
    *   Ensure your MySQL server is running.
    *   Create a new database for the project (e.g., `youth_survey_db`).
    *   Update the database configuration in `c:\Users\ROX17\OneDrive\Desktop\YUT Project\yut_backend\settings.py`:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your_database_name',  # e.g., youth_survey_db
                'USER': 'your_mysql_username', # e.g., root
                'PASSWORD': 'your_mysql_password',
                'HOST': 'localhost',           # Or your MySQL host
                'PORT': '3307',                # Or your MySQL port (default is 3306)
            }
        }
        ```

5.  **Configure Settings:**
    In `c:\Users\ROX17\OneDrive\Desktop\YUT Project\yut_backend\settings.py`:
    *   Set a unique `SECRET_KEY`.
    *   Configure `EMAIL_BACKEND`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` if you plan to use email features (e.g., for contact forms or password resets).
    *   Adjust `ALLOWED_HOSTS` for your development/production environments.
    *   Configure `CORS_ALLOWED_ORIGINS` to include your frontend application's URL (e.g., `http://localhost:3000`).

6.  **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations users
    python manage.py migrate
    ```

7.  **Create a Superuser (for Admin Panel Access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up an admin account.

8.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The backend API should now be accessible, typically at `http://12_7.0.0.1:8000/`.

## API Endpoints (Examples)

*   **Admin Panel:** `/admin/`
*   **User Registration:** `POST /api/users/register/`
*   **Obtain JWT Token (Login):** `POST /api/token/`
*   **Refresh JWT Token:** `POST /api/token/refresh/`
*   **Verify JWT Token (Optional):** `POST /api/token/verify/`
*   **Submit Survey:** `POST /api/users/submit-survey/`
*   **Get Survey Statistics:** `GET /api/users/survey-stats/`
*   *(Other endpoints as defined in `users/urls.py`)*

## How This Project is Beneficial

*   **Data-Driven Insights:** Provides a platform to collect specific and current data on youth unemployment, potentially offering more granular insights than broader national statistics.
*   **Trend Analysis:** Over time, the accumulated data can help identify emerging trends in youth employment, desired job sectors, the impact of education levels, and regional variations.
*   **Support for Policymaking:** The findings can serve as a valuable resource for government agencies, educational institutions, and NGOs working on initiatives to address youth unemployment.
*   **Resource for Stakeholders:** Can help career counselors, educators, and youth themselves understand the current employment landscape.
*   **Community Contribution:** Allows individuals to contribute data, fostering a collective understanding of the challenges and opportunities facing young people in the job market.

## Frontend Setup (Placeholder)

*(This section should be updated with the specific instructions for your frontend application, if applicable.)*

1.  Navigate to your frontend project directory.
2.  Install dependencies (e.g., `npm install` or `yarn install`).
3.  Start the frontend development server (e.g., `npm start` or `yarn dev`).
4.  Ensure the frontend is configured to make API calls to the Django backend (e.g., `http://127.0.0.1:8000/api/`).

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them with clear messages (`git commit -m 'Add some amazing feature'`).
4.  Push your changes to your forked repository (`git push origin feature/your-feature-name`).
5.  Open a Pull Request to the main project repository.

Please ensure your code follows the project's coding style and includes tests where appropriate.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details. (You'll need to create a `LICENSE` file with the MIT License text if you choose this license).