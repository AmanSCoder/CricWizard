# CricWizard

Welcome to CricWizard! CricWizard is a web application that fetches data from the ESPN website for T20 cricket matches and allows users to filter and find players based on specific criteria. 

## Website Link

[CricWizard](https://cricwizard.onrender.com/)

## Features

- **Player Categories**: Filter players by categories including Batsman, Bowler, Wicketkeeper, and All-Rounder.
- **Detailed Statistics**: Access detailed statistics of players from T20 matches.
- **Responsive Design**: User-friendly interface that works on both desktop and mobile devices.

## Tech Stack

- **Frontend**: React
- **Backend**: Flask
- **Data Source**: ESPN website for T20 cricket data

## Installation

To run CricWizard locally, follow these steps:

### Prerequisites

- Node.js
- Python 3.x
- Flask
- React

### Backend Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/AmanSCoder/CricWizard.git
    cd CricWizard/app
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask server:

    ```bash
    flask run
    ```

### Frontend Setup

1. Navigate to the frontend directory:

    ```bash
    cd ../app
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Start the React application:

    ```bash
    npm start
    ```

The React app should now be running on `http://localhost:3000` and the Flask server on `http://localhost:5000`.

## Usage

1. Visit the website: [CricWizard](https://cricwizard.onrender.com/)
2. Use the filter options to select a player category: Batsman, Bowler, Wicketkeeper, or All-Rounder.
3. View the list of players that match the selected criteria.

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.


## Contact

For any inquiries or feedback, please contact us at amansrivastava7969@gmail.com.

---

Thank you for using CricWizard! We hope you enjoy exploring cricket statistics with our app.
