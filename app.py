import streamlit as st

# -------------------
# Basic Config
# -------------------
st.set_page_config(page_title="Srivarshini P - Portfolio", page_icon="💻", layout="wide")

# -------------------
# Header Section
# -------------------
st.title("👩‍💻 Srivarshini P")
st.subheader("Student at St. Joseph's College of Engineering | Full-Stack Developer | AI/ML Enthusiast")

st.write("📍 Chennai | ✉️ psrivarshini80@gmail.com | 📱 7538848395")
st.write("[🔗 LinkedIn](https://www.linkedin.com/in/srivarshini-p-589a74291)")

st.markdown("---")

# -------------------
# Profile
# -------------------
st.header("About Me")
st.write("""
Motivated Computer Science student passionate about full-stack development and problem-solving.  
Proficient in **Python, Java, MySQL**, with a growing interest in **AI/ML technologies**.  
Solved **140+ LeetCode problems** with a 100-day streak, demonstrating strong logic and consistency.  
Experienced in user-focused design, software development, and effective team collaboration.  
Seeking opportunities to apply technical and analytical skills to real-world challenges.
""")

# -------------------
# Skills
# -------------------
st.header("Skills")
cols = st.columns(3)
with cols[0]:
    st.subheader("Programming")
    st.write("Python, Java")
with cols[1]:
    st.subheader("Databases")
    st.write("MySQL")
with cols[2]:
    st.subheader("Frontend & Design")
    st.write("HTML, CSS, JavaScript, Figma, Canva")

# -------------------
# Education
# -------------------
st.header("Education")
st.write("""
- 🎓 **B.E. Computer Science** – St. Joseph's College Of Engineering (2023–2027), CGPA: 9.17  
- 📘 Higher Secondary – Babaji Vidhyashram (2022–2023), 92.2%  
- 📘 High School – Velammal Vidhyashram (2020–2021), 90.4%  
""")

# -------------------
# Projects
# -------------------
st.header("Projects")
st.write("""
- 📦 **Stock Management System** – Python, MySQL  
- 🌱 **AI Driven Cauliflower Disease Detection** – Python, ML, Google Colab  
- 📚 **Smart Notes & Study Material Hub** – Streamlit, FastAPI, SQLite  
""")

# -------------------
# Internships
# -------------------
st.header("Internship Experience")
st.write("""
- 💻 **Mphasis Ltd. (Full Stack Developer Intern, 2025)** – Built an Innovation Portal prototype & document segregation system.  
- 🎨 **RETECH Solutions Pvt Ltd (UI/UX Designer, 2024)** – 15-day internship, received positive feedback for creativity.  
- 📈 **Younity.in (Business Development Specialist, 2023)** – Generated ₹4,250 revenue, Certificate of Excellence.  
""")

# -------------------
# Certifications
# -------------------
st.header("Certifications")
st.write("""
- Python Programming (Younity)  
- Introduction to Machine Learning (NPTEL)  
- Python for Data Science (NPTEL)  
- Introduction to Data Science (Cisco)  
- Introduction to MongoDB (MongoDB University)  
""")

# -------------------
# Achievements
# -------------------
st.header("Key Achievements")
st.write("""
- 🏆 1st Place – Technical Quiz @ SIMATS Wissennaire’3  
- 🥇 1st Place – Technical Quiz @ Crescent Arcane’24  
- 🥈 Top 10 – CFTRI Food Hackathon  
- 🥉 4th Place – INNOVATHON’25 Ideathon  
- 🥈 Elite Silver Certification in Python for Data Science  
""")

# -------------------
# Contact
# -------------------
st.header("Contact Me")
st.write("📧 Email: psrivarshini80@gmail.com")
st.write("📱 Phone: 7538848395")
st.write("🔗 LinkedIn: [Click Here](https://www.linkedin.com/in/srivarshini-p-589a74291)")
