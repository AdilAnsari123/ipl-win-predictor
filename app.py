import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import os

# Custom CSS to enhance the appearance
st.markdown("""
<style>
    .main {
        background-color:#2ECC71 ;
        padding: 20px;
    }
        h1 {
        color: #ffffff;  /* White Text for Title */
        font-size: 50px;
        text-align: center;
    }
    .stButton>button {
        color: white;
        background-color: #007bff;
        border: none;
        padding: 10px 20px;
        text-align: center;
        font-size: 16px;
        cursor: pointer;
        margin-top: 20px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stSelectbox, .stNumberInput {
        padding: 10px;
        margin: 10px 0;
        font-size: 16px;
        border: 2px solid #007bff;  /* Blue Border */
        border-radius: 8px;  /* Rounded Corners */
        background-color: #FFFFFF;  /* white Background */
        color: #ffffff;  /* White Text */
    }
    .stHeader {
        color: #007bff;
        font-size: 100px;
        margin-top: 20px;
        text-align: center;
    }
    .prediction-result {
        background-color: #cceeff;
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .prediction-result h2 {
        color: #004d99;
    }
</style>
""", unsafe_allow_html=True)

image_path = 'ipl_image1.jpg'  # Path to the image file

# Check if the file exists
if os.path.exists(image_path):
    image = Image.open(image_path)

    # Resize the image
    base_width = 800  # Adjust width as needed
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    image = image.resize((base_width, h_size), Image.LANCZOS)

    st.image(image, use_column_width=True)
else:
    st.error("Image file not found. Please check the path.")
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
        'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai',
        'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
        'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi',
        'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']


pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
   batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
   bowling_team = st.selectbox('Select the bowling team', sorted(teams))

selected_city = st.selectbox('Select host city', sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
   score = st.number_input('Score')
with col4:
   overs = st.number_input('Overs completed')
with col5:
   wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
   run_left = target - score
   ball_left = 120 - (overs * 6)
   wickets = 10 - wickets
   crr = score / overs
   rrr = (run_left * 6) / ball_left

   input_df = pd.DataFrame({
    'batting_team': [batting_team],
    'bowling_team': [bowling_team],
    'city': [selected_city],
    'run_left': [run_left],
    'ball_left': [ball_left],
    'wickets': [wickets],
    'total_runs_x': [target],
    'crr': [crr],
    'rrr': [rrr]
   })

   result = pipe.predict_proba(input_df)
   loss = result[0][0]
   win = result[0][1]

   st.markdown(f"""
   <div class='prediction-result'>
      <h2>{batting_team} - {round(win * 100)}%</h2>
       <h2>{bowling_team} - {round(loss * 100)}%</h2>
   </div>
    """, unsafe_allow_html=True)
