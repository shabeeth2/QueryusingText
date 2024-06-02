# QueryusingText-Interactive Database Query Assistant

## Overview

This project introduces an interactive database query assistant designed to facilitate efficient querying and analysis of retail inventory data. Leveraging advanced natural language processing (NLP) techniques and machine learning models, it enables users to ask questions about the inventory in plain English, which are then translated into SQL queries to fetch the required data.

## Features

- **Natural Language Processing**: Users can interact with the system using natural language, making it more intuitive and accessible.
- **SQL Query Generation**: The system translates user queries into SQL queries, allowing for direct interaction with the database.
- **Interactive Interface**: Provides a user-friendly interface for entering queries and viewing results.
- **Few-Shot Learning**: Utilizes few-shot learning techniques to improve the accuracy and efficiency of query translation.

## Getting Started

### Prerequisites

- Python > 3.9
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```
   git clone https://your-repository-url.git
   cd RetailProject
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have a PostgreSQL database set up and accessible. Update the `config.py` file with your database credentials.

4. Start the application:
   ```
   streamlit run main.py
   ```

## Usage

After starting the application, navigate to the provided URL (usually `http://localhost:8501`) in your web browser. You'll be greeted with a simple interface where you can enter your database URI and your question about the inventory.

https://github.com/shabeeth2/QueryusingText/blob/main/sample-Quert-with-HL.mp4

### Database Connection

Enter your database URI in the provided field. This URI should point to your retail inventory database.

### Asking Questions

Type your question in the text box. The system will process your question and return the relevant data from the database.

## Contributing

Contributions are welcome Please feel free to submit a pull request or open an issue if you encounter any problems.

---

This README provides a comprehensive overview of the project, including setup instructions, usage guidelines, and licensing information. It's tailored to help both new users get started quickly and contributors understand how to engage with the project.
