import streamlit as st
import requests
import pandas as pd

# Personal Details
GITHUB_USERNAME = "aaditya0810"
PORTFOLIO_NAME = "Aaditya C Punekar"
LINKEDIN_URL = "https://www.linkedin.com/in/aaditya-punekar/"
RESUME_LINK = "https://github.com/aaditya0810/Resume/blob/main/Aaditya%20C%20Punekar.pdf"

# Fetch Repositories from GitHub API
GITHUB_API_URL = f"https://api.github.com/users/aaditya0810/repos"
response = requests.get(GITHUB_API_URL)
repos = response.json()

# Convert to DataFrame and Sort by Latest Date
df_repos = pd.DataFrame(repos)[["name", "html_url", "description", "created_at"]]
df_repos["created_at"] = pd.to_datetime(df_repos["created_at"])
df_repos = df_repos.sort_values(by="created_at", ascending=False)  # Sort newest first

# Streamlit Page Configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# ---- HEADER ----
st.title(f"🚀 {PORTFOLIO_NAME} - Data Analytics Portfolio")
st.write(f"📌 **GitHub:** [{GITHUB_USERNAME}](https://github.com/{GITHUB_USERNAME}) | 📇 **[LinkedIn]({LINKEDIN_URL})** | 📄 **[Resume]({RESUME_LINK})**")

# ---- PROJECTS SECTION ----
st.subheader("📂 My Latest GitHub Projects")

for index, row in df_repos.iterrows():
    st.write(f"### [{row['name']}]({row['html_url']})")
    st.write(f"📝 {row['description'] if row['description'] else 'No description available.'}")
    st.write(f"📅 Created on: {row['created_at'].date()}")
    st.write("---")

st.write("🔄 This portfolio updates **automatically** whenever I upload a new project to GitHub!")
