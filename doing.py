import streamlit as st
import streamlit.components.v1 as components
import base64
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import os
from openai.types.chat import ChatCompletionMessageParam
from openai import OpenAI



# ===================== APP CONFIG =====================
st.set_page_config(page_title="Global Income Inequality Analysis", layout="wide")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# ===================== LOTTIE LOADER =====================
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        print(f"Error loading lottie: {e}")
        return None


# ===================== BACKGROUND IMAGE =====================
def set_background(image_url):
    response = requests.get(image_url)
    encoded_string = base64.b64encode(response.content).decode()
    css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ===================== PAGES =====================
import plotly.express as px

def home():
    st.title("🌍 Welcome to Global Income Inequality Analysis")
    st.write("Navigate using the sidebar to explore the dashboard, view your profile, read the project content, and send feedback.")

    # Animation
    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, speed=1, loop=True, height=400, key="income_inequality_anim")

    # Section 1
    st.markdown("### Why Global Income Inequality Matters?")
    st.write("""
        Income inequality reflects how unevenly wealth is distributed across the world.  
        By analyzing this, we can uncover:
        - 📊 Differences in wealth across countries
        - 🌍 Trends in inequality over time
        - ⚖️ Gaps between rich and poor populations
    """)

    # Section 2 - Key Global Stats
    st.markdown("### 🌐 The Global Picture")
    st.info("""
    - 💰 **The richest 10% of the world** earn more than **50% of total global income**.  
    - 👥 Meanwhile, **the poorest 50% share less than 10%** of total global income.  
    - 📉 In many regions, inequality has widened significantly in the last 20 years.  
    """)

    # Section 3 - Why This Analysis is Important
    st.markdown("### 🚀 Why This Analysis Is Important")
    st.write("""
        Understanding inequality helps:
        - Governments design **better policies** for fair wealth distribution.  
        - Organizations focus on **sustainable development goals (SDGs)**.  
        - Citizens become aware of **social and economic imbalances**.  
    """)

    # Section 4 - World Map Visualization
    st.markdown("### 🗺️ Global Inequality Map (Gini Index by Country)")
    # Sample data (replace with dataset.xlsx later)
    data = {
        "Country": ["United States", "India", "Brazil", "South Africa", "Germany", "Norway", "China"],
        "Gini": [41.4, 35.7, 53.4, 63.0, 31.7, 27.0, 38.5]
    }
    df_map = pd.DataFrame(data)

    fig = px.choropleth(
        df_map,
        locations="Country",
        locationmode="country names",
        color="Gini",
        color_continuous_scale="RdYlBu_r",
        title="Global Income Inequality (Gini Index)"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Section 5 - Call to Action
    st.success("""
    🔎 Use this platform to **explore dashboards**, **analyze data trends**, and **gain insights** into how income inequality affects our world.  
    Together, we can work towards a **fairer and more inclusive future**. 🌍✨
    """)



def dashboard():
    st.title("📊 Global Income Inequality Dashboard")

    dashboard_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiODA2YTQzYTItNGNkYS00NTg4LTg3YmItZjVjNGY1NmJkOGExIiwidCI6IjU1NGQ0NGVjLTkwMmYtNDM1OS1iZWNlLTg2Zjg5MzU4NDJhOSJ9"
    components.iframe(src=dashboard_url, height=600, scrolling=True)

    # Extra context for effectiveness
    st.markdown("### 📈 What You Can Explore in the Dashboard")
    st.write("""
        This interactive dashboard provides a **comprehensive view of global income inequality trends**.  
        By exploring the visuals, you can understand:
        - 🌍 **Country-level Gini coefficients** to see which nations are more equal or unequal.  
        - ⏳ **Trends over time** (2000–2020) that reveal whether inequality is improving or worsening.  
        - 🏦 **Comparison by income groups** (low, middle, high-income countries).  
        - 📊 **Regional differences** showing how inequality patterns vary across continents.  
    """)

    st.markdown("### 🔎 Why This Dashboard Matters")
    st.info("""
        - It helps policymakers **identify regions that need urgent attention**.  
        - Researchers can track **long-term inequality trends**.  
        - Citizens and students gain a **clearer understanding of wealth distribution** worldwide.  
        - It supports progress monitoring for the **United Nations Sustainable Development Goal (SDG 10: Reduced Inequalities)**.  
    """)

    st.markdown("### 🚀 How to Use It Effectively")
    st.write("""
        1. **Hover over data points** to see exact values for each country and year.  
        2. **Filter by region or income group** to narrow down your analysis.  
        3. **Compare countries** side by side to spot differences.  
        4. Use insights from the visuals to form your own conclusions about **global inequality trends**.  
    """)


import streamlit as st
import os
from PIL import Image
import pandas as pd

def profile():
    st.title("👤 User Profile")

    user_email = st.session_state.get('current_user', None)
    if user_email is None:
        st.error("No user logged in.")
        return

    if not os.path.exists("users.xlsx"):
        st.error("User data not found.")
        return

    # Load user data
    users_df = pd.read_excel("users.xlsx")
    users_df.columns = users_df.columns.str.strip().str.lower()

    # Ensure 'email' column exists
    if 'email' not in users_df.columns:
        st.error("Column 'email' not found in users.xlsx")
        return

    # Find current user
    user_data = users_df[users_df['email'] == user_email]
    if user_data.empty:
        st.error("User not found.")
        return

    # Two-column layout
    col1, col2 = st.columns([1, 2])

    with col1:
        # Default profile picture
        profile_pic_path = f"profile_pics/{user_email}.jpg"
        if not os.path.exists("profile_pics"):
            os.makedirs("profile_pics")

        if os.path.exists(profile_pic_path):
            img = Image.open(profile_pic_path)
        else:
            img = Image.open("profile.png")  # Default profile picture

        st.image(img, use_container_width=True, caption="Profile Picture")

        # Upload new profile picture
        uploaded_file = st.file_uploader("Change Profile Picture", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            img.save(profile_pic_path)
            st.success("Profile picture updated!")
            st.image(img, use_container_width=True, caption="Profile Picture")

    with col2:
        # Display all fields except email
        for col in user_data.columns:
            if col != 'email':
                value = user_data[col].values[0]
                # Convert phone to integer if possible
                if col == "phone":
                    try:
                        value = int(float(value))
                    except:
                        pass
                st.write(f"**{col.capitalize()}:** {value}")

        # Editable fields
        with st.expander("Edit Profile"):
            editable_fields = {}
            for col in user_data.columns:
                if col != 'email':
                    value = user_data[col].values[0]

                    if col == "phone":
                        # Ensure phone is a valid integer, otherwise fallback to text input
                        try:
                            value = int(float(value))
                            editable_fields[col] = st.number_input(
                                col.capitalize(),
                                value=int(value),
                                step=1
                            )
                        except:
                            editable_fields[col] = st.text_input(
                                col.capitalize(),
                                value=str(value) if value is not None else ""
                            )
                    else:
                        editable_fields[col] = st.text_input(
                            col.capitalize(),
                            value=str(value) if value is not None else ""
                        )

            if st.button("Save Changes"):
                for col, value in editable_fields.items():
                    users_df.loc[users_df['email'] == user_email, col] = value
                users_df.to_excel("users.xlsx", index=False)
                st.success("Profile updated successfully!")



import streamlit as st

def project_content():
    st.title("📚 Global Income Inequality Analysis")

    # Project Objective
    st.markdown("### 🎯 Project Objective")
    st.write(
        "Analyze and visualize global income inequality using data spanning from 1970 to 2023. "
        "The aim is to understand patterns, trends, and disparities across different countries and regions."
    )

    # Data Source
    st.markdown("### 🗂️ Data Source")
    st.write(
        "- Gini coefficients by country\n"
        "- Income group classifications from World Bank and UN databases\n"
        "- Public datasets on GDP, population, and socio-economic indicators"
    )

    # Key Insights
    st.markdown("### 💡 Key Insights")
    st.write("""
    - 📈 **Rising inequality** in certain developing regions  
    - 🌍 **Lower inequality** observed in most developed countries  
    - 📊 **Mixed trends** in emerging economies, with some improving and some worsening  
    - 💹 **Correlation** observed between economic growth and inequality levels in some countries
    """)

    # Methodology
    st.markdown("### 🛠️ Methodology")
    st.write("""
    1. Data collection and cleaning from reliable sources  
    2. Exploratory Data Analysis (EDA) to identify patterns  
    3. Visualization using charts and graphs to highlight trends  
    4. Comparative analysis across income groups and regions  
    5. Interpretation of results and deriving actionable insights
    """)

    # Tools Used
    st.markdown("### ⚙️ Tools & Technologies")
    st.write("""
    - Power BI: Interactive dashboards and charts") 
    - Streamlit: Web app deployment for visualization") 
    - Python (Pandas, Matplotlib, Seaborn): Data processing and analysis""")

    # Visualizations (Placeholder for later)
    st.markdown("### 📊 Visualizations")
    st.write("Interactive graphs showing Gini coefficient trends, regional comparisons, and income disparity over time will be displayed here.")

    # Implications
    st.markdown("### 🌐 Implications & Recommendations")
    st.write("""
    - Highlight countries and regions requiring policy interventions  
    - Assist governments and NGOs in focusing on socio-economic inequality reduction  
    - Provide insights for further research on the causes of income inequality
    """)

    # Conclusion
    st.markdown("### ✅ Conclusion")
    st.write("The analysis provides a comprehensive understanding of global income inequality trends and highlights the need for targeted economic policies.")




def feedback():
    st.title("✍️ Feedback Form")
    with st.form(key='feedback_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        feedback_text = st.text_area("Your Feedback")
        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            feedback_data = {"Name": name, "Email": email, "Feedback": feedback_text}
            feedback_file = "feedback.xlsx"

            if os.path.exists(feedback_file):
                df = pd.read_excel(feedback_file)
                df = pd.concat([df, pd.DataFrame([feedback_data])], ignore_index=True)
            else:
                df = pd.DataFrame([feedback_data])

            df.to_excel(feedback_file, index=False)
            st.success("Thank you for your feedback!")


def signup():
    st.title("📝 Sign Up")

    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_yr6zz3wv.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=300, key="signup_anim")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        user_data_path = "users.xlsx"
        new_user = {"Name": name, "Email": email, "Password": password}

        if os.path.exists(user_data_path):
            df = pd.read_excel(user_data_path)
            if email in df["Email"].values:
                st.error("An account with this email already exists.")
                return
            df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        else:
            df = pd.DataFrame([new_user])

        df.to_excel(user_data_path, index=False)
        st.success("Sign up successful! Please sign in now.")
        st.session_state['active_page'] = 'Sign In'


def signin():
    st.title(" 🌍 Global Income Inequality Analysis")
    st.title("🔐 Sign In")

    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=300, key="signin_anim")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        user_data_path = "users.xlsx"
        if not os.path.exists(user_data_path):
            st.error("No users found. Please sign up first.")
            return

        df = pd.read_excel(user_data_path)
        match = df[(df["Email"] == email) & (df["Password"] == password)]

        if not match.empty:
            st.session_state['logged_in'] = True
            st.session_state['current_user'] = email
            st.session_state['active_page'] = "Home"
            st.success("Login successful! Redirecting to Home...")
        else:
            st.error("Invalid email or password.")


def admin_panel():
    st.title("🛠️ Admin Panel")
    user_email = st.session_state.get("current_user", None)

    if user_email != "chvineetha2005@gmail.com":
        st.error("⛔ Access Denied. You are not authorized to view this page.")
        return

    st.success("✅ Welcome, Admin!")

    # Users
    if os.path.exists("users.xlsx"):
        st.markdown("### 👥 Registered Users")
        df_users = pd.read_excel("users.xlsx")
        st.dataframe(df_users)
    else:
        st.warning("⚠️ No users file found.")

    # Feedback
    if os.path.exists("feedback.xlsx"):
        st.markdown("### 💬 User Feedback")
        df_feedback = pd.read_excel("feedback.xlsx")
        st.dataframe(df_feedback)
    else:
        st.warning("⚠️ No feedback file found.")


# ===================== AI CHATBOT =====================
# ===================== AI CHATBOT =====================
import streamlit as st
import pandas as pd
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

client = OpenAI()

# -----------------------------
# Generate Dashboard Summary
# -----------------------------
def generate_dashboard_summary(df: pd.DataFrame) -> str:
    summary_parts = []

    if "country" in df.columns:
        country_count = df["country"].nunique()
        summary_parts.append(f"- Number of countries: {country_count}")

    if "year" in df.columns:
        year_range = f"{df['year'].min()} - {df['year'].max()}"
        summary_parts.append(f"- Year range: {year_range}")

    if "gini" in df.columns:
        avg_gini = round(df["gini"].mean(), 2)
        summary_parts.append(f"- Average Gini index: {avg_gini}")

        top5 = df.groupby("country")["gini"].mean().nlargest(5)
        summary_parts.append(f"- Top 5 countries by inequality: {', '.join(top5.index)}")

        bottom5 = df.groupby("country")["gini"].mean().nsmallest(5)
        summary_parts.append(f"- Lowest inequality countries: {', '.join(bottom5.index)}")

    return "Dashboard Insights:\n" + "\n".join(summary_parts)

# -----------------------------
# AI Chatbot Function
# -----------------------------
def ai_chatbot(dataset_summary: str = "", dashboard_summary: str = "", key_suffix: str = "chatbot"):
    st.title("🌍 Global Income Inequality Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    system_prompt = f"""
You are a helpful assistant trained ONLY to answer questions about:
1. Global income inequality analysis
2. The dashboard provided in this Streamlit web app.

Rules:
- ALWAYS use the provided dashboard summary for numbers, years, or metrics.
- NEVER invent values or guess — if something is not in the summary, say: 
  "This detail is not available in the dashboard."
- If a user asks unrelated questions, reply:
  "I can only answer questions about global income inequality or the dashboard insights."

Dashboard summary:
{dashboard_summary}
"""

    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": system_prompt}
    ]

    # Display previous chat history
    for chat in st.session_state.chat_history:
        st.chat_message(chat["role"]).markdown(chat["content"])
        messages.append(chat)

    # Chat input with unique key
    input_key = f"chat_input_{key_suffix}"
    if user_input := st.chat_input("Ask about income inequality or the dashboard...", key=input_key):
        st.chat_message("user").markdown(user_input)
        messages.append({"role": "user", "content": user_input})

        # Call OpenAI APIs
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # fallback: gpt-3.5-turbo
            messages=messages
        )
        bot_reply = response.choices[0].message.content
        st.chat_message("assistant").markdown(bot_reply)

        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

# ===================== MAIN =====================
def main():
    # Custom background (optional)
    def set_background(url):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url({url});
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    background_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwz-1wgSfRwvSzWB3CsOnUwOeLMPxvqvKAxg&s"
    set_background(background_image_url)

    # Custom sidebar styling
    custom_css = """
    <style>
        section[data-testid="stSidebar"] button {
            border-radius: 15px !important;
            padding: 0.6em 1em !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            margin: 5px 0 !important;
            background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%) !important;
            color: #000000 !important;
            border: none !important;
            transition: all 0.3s ease-in-out !important;
        }
        section[data-testid="stSidebar"] button:hover {
            background: linear-gradient(135deg, #a6c1ee 0%, #fbc2eb 100%) !important;
            transform: scale(1.05);
            box-shadow: 0px 6px 12px rgba(0,0,0,0.2);
            color: #000000 !important;
        }
        section[data-testid="stSidebar"] button:active {
            transform: scale(0.97);
            box-shadow: 0px 3px 6px rgba(0,0,0,0.3);
            color: #000000 !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Session state defaults
    if 'users' not in st.session_state:
        st.session_state['users'] = {}
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'active_page' not in st.session_state:
        st.session_state['active_page'] = 'Sign In'

    # Sidebar navigation
    st.sidebar.title("📌 Navigation")
    if not st.session_state['logged_in']:
        pages = ["Sign In", "Sign Up"]
        for page in pages:
            if st.sidebar.button(page, key=page, use_container_width=True):
                st.session_state['active_page'] = page

        if st.session_state['active_page'] == "Sign In":
            signin()  # your signin function
        elif st.session_state['active_page'] == "Sign Up":
            signup()  # your signup function
        else:
            home()    # fallback
    else:
        pages = ["Home", "Dashboard", "Profile", "Project Content", "Feedback", "AI Chatbot", "Logout"]
        if st.session_state['current_user'] == "chvineetha2005@gmail.com":
            pages.insert(-1, "Admin Panel")

        for page in pages:
            if st.sidebar.button(page, key=page, use_container_width=True):
                st.session_state['active_page'] = page

        # Page rendering
        if st.session_state['active_page'] == "Home":
            home()
        elif st.session_state['active_page'] == "Dashboard":
            dashboard()
        elif st.session_state['active_page'] == "Profile":
            profile()
        elif st.session_state['active_page'] == "Project Content":
            project_content()
        elif st.session_state['active_page'] == "Feedback":
            feedback()
        elif st.session_state['active_page'] == "AI Chatbot":
            st.sidebar.title("Upload Dashboard Dataset")
            uploaded_file = st.sidebar.file_uploader("Upload dataset (CSV/Excel)", type=["csv", "xlsx"], key="chatbot_file")
            if uploaded_file:
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)

                st.write("### Dashboard Dataset Preview")
                st.dataframe(df.head())

                dashboard_summary = generate_dashboard_summary(df)
                dataset_summary = ""
                ai_chatbot(dataset_summary, dashboard_summary, key_suffix="dashboard")
            else:
                st.info("Please upload a dataset to start the chatbot.")
        elif st.session_state['active_page'] == "Admin Panel":
            admin_panel()
        elif st.session_state['active_page'] == "Logout":
            st.session_state['logged_in'] = False
            st.session_state['active_page'] = "Sign In"
            st.success("Logged out successfully!")

if __name__ == "__main__":
    main()
