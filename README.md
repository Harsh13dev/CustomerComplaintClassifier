# Customer Email Analyser and Response Generator

This project uses LangChain Runnables to classify customer emails and generate appropriate responses based on their type (complaint, refund, or feedback).

## Features

* **Email Classification**: Classifies incoming customer emails into three categories: 'complaint', 'refund', or 'feedback'.

* **Automated Response Generation**: Generates a tailored, short, and appropriate response based on the classified email type.

* **Streamlit UI**: Provides a simple web interface for entering emails and viewing the generated responses.

## Technologies Used

* LangChain

* Groq API (for `llama-3.1-8b-instant` model)

* Streamlit

* Python-dotenv

## Setup and Installation

1.  **Clone the repository**:

    ```
    git clone https://github.com/Harsh13dev/CustomerComplaintClassifier.git
    cd CustomerComplaintClassifier
    
    ```

2.  **Create a virtual environment** (recommended):

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    ```

3.  **Install dependencies**:

    ```
    pip install -r requirements.txt

    ```

    *(Note: You'll need to create a `requirements.txt` file based on the `app.py` imports. It should include `langchain`, `python-dotenv`, `streamlit`, `langchain-core`, `pydantic`, `langchain-groq`.)*

4.  **Set up API Keys**:
    Create a `.env` file in the root directory of your project and add your Groq API key:

    ```
    GROQ_API_KEY="your_groq_api_key_here"

    ```

## Usage

1.  **Run the Streamlit application**:

    ```
    streamlit run app.py

    ```

2.  Open your web browser and go to the address provided by Streamlit (usually `http://localhost:8501`).

3.  Enter a customer email into the text area and click "Submit" to see the classified email type and the generated response.

## Project Structure

* `app.py`: The main application script containing the LangChain logic and Streamlit UI.

* `.env`: (Not committed) Stores API keys.

## Example Screenshots (Optional)

You could add screenshots of the Streamlit interface here to make the README more visually appealing.
