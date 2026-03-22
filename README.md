🌍 Data Visualization Dashboard for Global Income Inequality Analysis

Infosys Springboard Virtual Internship 6.0 — Batch 02
Completed by Vineetha Chalamala Setti and team


📌 Project Overview
This project analyzes and visualizes global income inequality using international datasets (Gini Index, GDP per capita, median income, income share by deciles). The findings are presented through an interactive Power BI dashboard embedded in a Streamlit web application.

🎯 Project Objectives

Identify and compare income distribution trends across countries and regions
Highlight patterns of inequality (richest vs. poorest income groups)
Provide an interactive platform for exploring global and regional disparities
Document the full workflow: Data Collection → Preprocessing → Visualization → Deployment


🛠️ Tech Stack
ToolPurposePythonCore programming languageStreamlitWeb application frameworkPower BIInteractive dashboardPandasData processing and analysisPlotlyData visualizationOpenAI APIAI Chatbot integrationExcel (openpyxl)User data and feedback storage

📁 Project Structure
global-income-inequality/
│
├── app.py                  # Main Streamlit application
├── profile.png             # Default user profile picture
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── secrets.toml        # API keys (DO NOT COMMIT — see note below)
├── profile_pics/           # Uploaded user profile pictures
└── README.md               # Project documentation

🚀 Features

🔐 User Authentication — Sign In / Sign Up system
📊 Power BI Dashboard — Embedded interactive global inequality dashboard
🗺️ World Map Visualization — Gini Index choropleth map
👤 User Profile — Editable profile with photo upload
💬 AI Chatbot — GPT-powered assistant for income inequality queries
📋 Project Content Page — Full project write-up and insights
📝 Feedback Form — User feedback collection
🛡️ Admin Panel — View all registered users and feedback


⚙️ Setup & Installation
1. Clone the repository
bashgit clone https://github.com/YOUR_USERNAME/global-income-inequality.git
cd global-income-inequality
2. Install dependencies
bashpip install -r requirements.txt
3. Configure API Keys
Create a .streamlit/secrets.toml file:
tomlOPENAI_API_KEY = "your-openai-api-key-here"

⚠️ Never commit your secrets.toml to GitHub! It's already listed in .gitignore.

4. Run the app
bashstreamlit run app.py

📊 Data Sources

World Bank — Gini Index, GDP per capita
OECD — Income share by deciles
IMF — Median income, economic indicators


👥 Team Members
NameVineetha Chalamala SettiMalloju VyshnaviNayana AjayPranathi NethiVidyalakshmi RJatin MukatiSahil GaikwadGokulnathan SaravananAnagha BhurePadmini Swaranam STejaswini NethalaRagavi SSara Mamatha

📅 Internship Timeline
WeekActivityWeek 1Data collection from World Bank, OECD, IMFWeek 2Dataset merging, handling missing valuesWeek 3Data cleaning and preprocessingWeek 4Normalization, aggregation, dashboard layout planningWeek 5Power BI base dashboard creationWeek 6Dashboard interactivity and stylingWeek 7Streamlit integrationWeek 8Testing, refinement, final documentation

🙏 Acknowledgements

Mentor: Bhargava Sai Reddy Vanga
Program Coordinator: Pranathi
Organization: Infosys Springboard Virtual Internship 6.0


📜 License
This project was built as part of an educational internship program. All data is sourced from publicly available international datasets.
