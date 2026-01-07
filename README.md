# Movie Analytics and Hybrid Recommendation System

## Project Overview
This project implements a comprehensive movie recommendation system that combines Exploratory Data Analysis (EDA) with a Hybrid Filtering Engine. The system leverages both Content-Based Filtering (using TF-IDF and Cosine Similarity) and Collaborative Filtering (using Singular Value Decomposition) to provide personalized movie suggestions.

The application is deployed using Streamlit and features an automated translation capability, converting movie synopses from English to Indonesian to enhance local user accessibility.

## Key Features

### 1. Hybrid Recommendation Engine
The core of this project is a hybrid algorithm that mitigates the "cold start" problem often found in single-method systems:
* **Content-Based Filtering:** Analyzes movie plot summaries using TF-IDF Vectorization to recommend movies with similar textual content.
* **Collaborative Filtering (SVD):** Utilizes matrix factorization to predict user ratings based on historical interaction data, capturing latent user preferences.

### 2. Data Analytics
Includes a detailed analysis of the dataset, covering:
* Distribution of movie runtimes and profitability.
* Correlation between budget, revenue, and popularity.
* Identification of high-performing genres and release trends.

### 3. User Interface
* **Streamlit Dashboard:** A responsive web interface for users to select favorite movies and view recommendations.
* **Real-time Translation:** Integrated with `deep_translator` to automatically translate movie overviews into Indonesian.

## Technical Architecture

* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Surprise (SVD), Scikit-Learn (Feature Extraction)
* **Visualization:** Matplotlib, Seaborn
* **Web Framework:** Streamlit
* **Tunneling:** PyNgrok (for exposing local server)

## Project Structure

* `movies_metadata.csv`: Raw dataset containing movie details.
* `ratings_small.csv`: User ratings dataset for collaborative filtering.
* `app.py`: The main entry point for the Streamlit application.
* `MovieAnalytics.ipynb`: Jupyter Notebook containing the full EDA, model training, and evaluation pipeline.
* `svd_model.pkl`: Serialized SVD model.
* `movie_data.pkl`: Processed dataframe for the application.
* `cosine_sim.pkl`: Pre-computed cosine similarity matrix.
* `indices.pkl`: Mapping of movie titles to dataframe indices.

## Installation and Usage

### Prerequisites
Ensure you have Python installed. It is recommended to use a virtual environment.

### Installation
1.  Clone the repository.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
To launch the Streamlit interface locally:

```bash
streamlit run app.py
