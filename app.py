# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc


# Import our Mini Apps
from eda_app import run_eda_app
from ml_app import run_ml_app

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""

desc_temp = """
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			"""


def main():
	# st.title("Main App")
	stc.html(html_temp)

	menu = ["Home", "EDA", "ML", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Home":
		st.subheader("Home")
		# st.write(desc_temp)
		st.markdown(desc_temp, unsafe_allow_html=True)

	elif choice == "EDA":
		run_eda_app()

	elif choice == "ML":
		run_ml_app()
	else:
		st.subheader("About the Diabetes Prediction App")
		st.write("This app helps you explore diabetes data and use " 
			"machine learning models to predict diabetes status " 
			"based on the information you enter.")

		st.markdown("""
		**Features:**
		- Explore the dataset and descriptive statistics.
		- View interactive charts and distributions.
		- Enter information to generate a model prediction.
		- Compare predictions from the available models.

		**Technologies:** Python, Streamlit, Pandas, NumPy,
		Scikit-learn, Joblib, Matplotlib, Seaborn and Plotly.

		**Developed by:** John Bernard Conteh  
		**JBC@Science_Care_SL**
		        """)







if __name__ == '__main__':
	main()