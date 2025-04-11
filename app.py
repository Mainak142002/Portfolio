import streamlit as st
#from PIL import Image

# --- Profile Section ---
st.set_page_config(page_title="Mainak Dey Portfolio", layout="wide")

# Load your profile image
#image = Image.open("profile.jpg")  # Replace with your profile image file name
#st.sidebar.image(image, width=150)

st.sidebar.title("Mainak Dey")
st.sidebar.markdown("📧 mainak.dey24-26@bibs.co.in")
st.sidebar.markdown("📞 6295768519")
st.sidebar.markdown("📍 West Bengal")

# Socials
st.sidebar.markdown("### 🔗 Connect with Me")
st.sidebar.markdown("[LinkedIn](www.linkedin.com/in/mainak-dey-bbb909171-dataanalyst)")
st.sidebar.markdown("[GitHub](https://github.com/Mainak142002)")


# --- Summary ---
st.title("👋 Hello, I'm Mainak Dey")
st.subheader("Business Analytics and Data Science | BIBS")
st.write(
    """
    A hardworking individual seeking an Analyst role to showcase skills and maximize 
    business efficiency through data insights and visualization.
    """
)

# --- Education ---
st.header("🎓 Education")
st.write("- **MBA in Business Analytics and Data Science**, BIBS Kolkata *(Pursuing)*")
st.write("- **BBA in HR**, Asutosh College, 66% (2020 - 2023)")
st.write("- **Higher Secondary**, Barasat Indira Gandhi High School (CBSE), 81%")

# --- Experience ---
st.header("💼 Work Experience")
st.subheader("HR Intern | Universal Tribes")
st.write("- Recruited and managed a team of 8 persons")
st.write("- Completed 45-day internship and received appreciation certificate")

# --- Skills ---
st.header("🛠️ Skills")
st.write("**Power BI | SQL | Python | MS Excel (Advanced) | PowerPoint**")

# --- Projects ---
st.header("📊 Projects")
st.subheader("1. RFM Analysis")
st.write("Classified customers into categories based on Recency, Frequency, and Monetary value")
st.write("Majority categorized as 'Medium Value' customers")

st.subheader("2. HR Analytics Dashboard")
st.write("Created in Power BI to analyze global attrition trends")
st.write("- Organization: 1,470 employees, Attrition rate: 16.1%")
st.write("- Highest attrition: Life Sciences (38%), Medical fields (27%)")

# --- Certifications ---
st.header("🎓 Certifications")
st.write("- Machine Learning with Python – IIT Kanpur")
st.write("- Data Analysis Using Power BI – WSCUBE TECH")

# --- Achievements & Hobbies ---
st.header("🏆 Achievements & Hobbies")
st.write("- 🏍️ Superbikes Enthusiast")
st.write("- 🎨 Graphic Designing (Logo)")
st.write("- 🐟 Fish Keeping")

# --- Languages ---
st.header("🌐 Languages")
st.write("**English** – Full Professional Proficiency")
st.write("**Bengali** – Native")
st.write("**Hindi** – Full Professional Proficiency")
