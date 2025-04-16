# Movie Recommendation System

# Overview

This project is a **Movie Recommendation System** built with Python and Streamlit, utilizing the TMDB API to fetch movie posters. It recommends movies based on content similarity (genres, cast, crew, keywords, and overview) using cosine similarity. The system provides an interactive web interface where users can select a movie from a dropdown and view the top 5 recommended movies along with their posters.

# Features

- **Content-Based Recommendations**: Recommends movies similar to the selected movie based on features like genres, cast, crew, keywords, and overview.
- **Interactive Web Interface**: Built using Streamlit, allowing users to select a movie and view recommendations with posters.
- **TMDB API Integration**: Fetches movie posters dynamically using the TMDB API.
- **Precomputed Similarity**: Uses preprocessed movie data and a cosine similarity matrix for efficient recommendations.
- **Responsive Layout**: Displays recommendations in a 5-column grid with movie titles and posters.

# Dataset

The system uses the TMDB 5000 Movie Dataset, consisting of:

- `tmdb_5000_movies.csv`: Contains movie details such as budget, genres, overview, and more.
- `tmdb_5000_credits.csv`: Includes cast and crew information.

The dataset is preprocessed to create `movies.pkl` (processed movie data) and `similarity.pkl` (cosine similarity matrix).

# Prerequisites

- Python 3.8 or higher
- A TMDB API key (obtain one by signing up at TMDB)
- Required Python libraries (listed in `requirements.txt`)

# Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up TMDB API Key**:

   - The `app.py` file contains a hardcoded TMDB API key. Replace it with your own:

     ```python
     url = f"https://api.themoviedb.org/3/movie/{{movie_id}}?api_key=YOUR_API_KEY&language=en-US"
     ```

   - Alternatively, store the API key as an environment variable:

     ```bash
     export TMDB_API_KEY="your-api-key"
     ```

     Update `app.py` to use:

     ```python
     import os
     API_KEY = os.getenv('TMDB_API_KEY')
     ```

4. **Ensure Pickle Files**:

   - Verify that `movies.pkl` and `similarity.pkl` are in the project directory. These files are generated during preprocessing and are required for the app to function.
   - If unavailable, regenerate them using the preprocessing script (see Data Preprocessing).

# Usage

1. **Run the Streamlit App**:

   ```bash
   streamlit run app.py
   ```

   This will launch a local server, typically accessible at `http://localhost:8501`.

2. **Interact with the App**:

   - Open the provided URL in a web browser.
   - Select a movie from the dropdown menu labeled "Type or select a movie from the dropdown".
   - Click the "Show Recommendation" button to view the top 5 recommended movies, each displayed with its title and poster.

# Example

Selecting **"The Hobbit: The Battle of the Five Armies"** might display recommendations like:

- The Hobbit: An Unexpected Journey
- The Hobbit: The Desolation of Smaug
- The Lord of the Rings: The Fellowship of the Ring
- The Lord of the Rings: The Return of the King
- The Lord of the Rings: The Two Towers

Each recommendation includes the movie poster fetched from the TMDB API.

# Project Structure

```
movie-recommendation-system/
│
├── app.py                  # Streamlit application code
├── movies.pkl              # Preprocessed movie data
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

# Data Preprocessing

The preprocessing steps (not included in the repository but summarized here) prepare the dataset for recommendations:

1. **Merging Datasets**: Combines `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` on the `title` column.
2. **Feature Selection**: Selects relevant columns: `movie_id`, `title`, `genres`, `keywords`, `cast`, `crew`, `overview`.
3. **Data Cleaning**:
   - Removes missing values in the `overview` column.
   - Converts JSON strings (e.g., genres, keywords) to lists of names.
   - Extracts the top 3 actors from `cast` and the director from `crew`.
   - Splits `overview` into words.
   - Removes spaces from multi-word tags (e.g., "Science Fiction" becomes "ScienceFiction").
4. **Tag Creation**: Combines `genres`, `keywords`, `cast`, `crew`, and `overview` into a single `tag` column.
5. **Stemming**: Applies NLTK's `PorterStemmer` to reduce words to their root form (e.g., "running" to "run").
6. **Vectorization**: Uses `CountVectorizer` (max 5,000 features, English stop words removed) to convert tags into vectors.
7. **Similarity Calculation**: Computes cosine similarity between all movie vectors.
8. **Serialization**: Saves the processed DataFrame as `movies.pkl` and the similarity matrix as `similarity.pkl`.

To regenerate these files, use the preprocessing code provided in the project context, which requires `pandas`, `numpy`, `scikit-learn`, and `nltk`.

# Dependencies

The required libraries are listed in `requirements.txt`:

```
streamlit
pandas
requests
scikit-learn
nltk
```

Install them with:

```bash
pip install -r requirements.txt
```

Download NLTK data for stemming:

```python
import nltk
nltk.download('punkt')
```

# Deployment

To deploy the app on Streamlit Cloud or another platform:

1. Push the repository to GitHub.

2. Ensure `requirements.txt` is included in the repository.

3. Sign in to Streamlit Cloud and connect your GitHub repository.

4. Add the TMDB API key as a secret in Streamlit Cloud settings:

   ```
   TMDB_API_KEY = "your-api-key"
   ```

5. Deploy the app.

# Limitations

- **TMDB API Rate Limits**: The API may impose rate limits, requiring error handling for 429 responses in production.
- **Content-Based Only**: Recommendations are based on content similarity and do not incorporate user preferences or collaborative filtering.
- **Pickle File Size**: `movies.pkl` and `similarity.pkl` are large files, which may complicate repository storage or require regeneration.
- **Hardcoded API Key**: The current code uses a hardcoded TMDB API key, which should be replaced with an environment variable for security.

# Future Improvements

- **Error Handling**: Add robust handling for API failures, missing posters, or invalid movie selections.
- **Caching**: Cache TMDB API responses to reduce redundant calls.
- **Enhanced UI**: Implement a search bar with autocomplete or display additional movie details (e.g., genres, overview).
- **Advanced Vectorization**: Use TF-IDF instead of `CountVectorizer` for better term weighting.
- **Personalized Recommendations**: Integrate user ratings or collaborative filtering for personalized suggestions.
- **Responsive Design**: Optimize the layout for mobile devices by adjusting the column structure.

# Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments

- TMDB for providing the movie dataset and API.
- Streamlit for the web application framework.
- Kaggle for hosting the TMDB 5000 Movie Dataset.

# Contact

For questions or feedback, please open an issue on GitHub or contact your-email@example.com.




