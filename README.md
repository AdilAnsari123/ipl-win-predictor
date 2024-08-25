# Cricket Match Win Probability Predictor

This project aims to predict the probability of a cricket team winning a match based on various factors such as the batting team, bowling team, match location, target score, current score, overs completed, and wickets lost. The model is trained using historical match data and implemented using Python with a web interface built in Streamlit.

## Project Overview

### 1. Data Cleaning
The dataset was cleaned using Pandas to ensure accuracy in predictions. Key columns in the cleaned data include:

- `batting_team`: The team currently batting.
- `bowling_team`: The team currently bowling.
- `city`: The city where the match is being played.
- `run_left`: Runs remaining to achieve the target.
- `ball_left`: Balls remaining to achieve the target.
- `wickets`: Number of wickets fallen.
- `total_runs_x`: Total runs scored so far.
- `crr`: Current run rate.
- `rrr`: Required run rate.
- `result`: The outcome of the match (win/lose).

### 2. Model Training
- **Train-Test Split**: The data was split into training and testing sets.
- **Feature Encoding**: Categorical features such as `batting_team`, `bowling_team`, and `city` were encoded using `OneHotEncoder` from scikit-learn.
- **Model Pipeline**: A pipeline was created using scikit-learn's `Pipeline` to streamline the process of feature transformation and model fitting. The pipeline includes:
  1. **Column Transformation**: One-hot encoding of categorical features.
  2. **Logistic Regression Model**: A logistic regression model with `liblinear` solver was used to predict the win probability.
- **Model Evaluation**: The model was evaluated using accuracy score on the test data, and class probabilities were predicted using `predict_proba`.

### 3. Model Deployment
- The trained model was saved using Python's `pickle` module for future use.
- A web application was built using Streamlit to provide a user-friendly interface for predicting match outcomes. Users can input the following details:
  - Batting Team
  - Bowling Team
  - Match City
  - Target Score
  - Current Score
  - Overs Completed
  - Wickets Fallen
- The application then predicts the probability of the batting team winning the match.

## Conclusion

This project demonstrates the power of data science in predicting the outcome of cricket matches using historical data and machine learning techniques. By cleaning the data and applying a Logistic Regression model, we were able to accurately estimate the probability of a team winning based on real-time match conditions.

The integration of this model with a Streamlit web application makes it easy for users to input match details and receive instant predictions. This tool can be particularly useful for cricket enthusiasts, analysts, and anyone interested in understanding the dynamics of the game.

As with any model, the predictions are based on historical data, and while they provide a strong indication of potential outcomes, they should be interpreted with caution. Future improvements could include incorporating more advanced machine learning models, expanding the dataset, and adding more features to enhance prediction accuracy.

This project showcases the end-to-end process of data-driven decision-making, from data cleaning and model training to deployment and user interaction.

