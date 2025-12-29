import streamlit as st
import base64
import os

# =========================================================
# 1. إعدادات الصفحة
# =========================================================
st.set_page_config(
    page_title="Saif Aboseada | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. إعدادات التصميم (Themes & CSS)
# =========================================================
# القيم الافتراضية
default_primary = "#D4AF37"  # ذهبي
default_bg = "#0E1117"  # أسود داكن
default_card = "#161B22"  # رمادي غامق جداً
default_text = "#E6EDF3"  # أبيض
img_width = 150  # حجم الصورة في السايد بار

# قراءة المتغيرات (سيتم تحديثها لو الأدمن دخل)
primary_color = default_primary
bg_color = default_bg
card_bg_color = default_card
text_color = default_text
border_radius = "50%"

# --- حقن CSS ---
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
            unsafe_allow_html=True)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    :root {{
        --primary: {primary_color};
        --bg-main: {bg_color};
        --bg-card: {card_bg_color};
        --text-main: {text_color};
    }}

    .stApp {{ background-color: var(--bg-main); font-family: 'Inter', sans-serif; }}

    /* تنسيق العناوين */
    h1, h2, h3 {{ color: var(--text-main) !important; }}
    .section-header {{ border-bottom: 2px solid #30363D; padding-bottom: 10px; margin-bottom: 25px; margin-top: 10px; color: var(--primary); }}

    /* تنسيق الكروت الموحد */
    .custom-card {{
        background-color: var(--bg-card); 
        border: 1px solid #30363D;
        border-radius: 8px; 
        padding: 24px; 
        margin-bottom: 20px;
        transition: transform 0.2s, border-color 0.2s;
    }}
    .custom-card:hover {{ border-color: var(--primary); transform: translateY(-3px); }}

    /* النصوص داخل الكروت */
    .card-title {{ color: var(--text-main); font-weight: 700; font-size: 1.1em; margin-bottom: 5px; }}
    .card-subtitle {{ color: var(--primary); font-size: 0.9em; font-weight: 600; margin-bottom: 10px; }}

    /* Skill Badges */
    .skill-badge {{
        background-color: transparent; border: 1px solid #30363D; color: var(--text-main);
        padding: 6px 14px; border-radius: 4px; font-size: 0.85em; display: inline-block; margin: 4px;
    }}
    .skill-badge:hover {{ border-color: var(--primary); color: var(--primary); }}

    /* Contact Form Styling */
    div[data-testid="stForm"] {{ background-color: var(--bg-card); border: 1px solid #30363D; padding: 20px; border-radius: 10px; }}

    /* Sidebar Styling to match Screenshot */
    section[data-testid="stSidebar"] {{
        background-color: #0E1117;
        border-right: 1px solid #30363D;
    }}
    .sidebar-img {{
        width: 120px; height: 120px; border-radius: 50%; 
        border: 3px solid {primary_color}; object-fit: cover; display: block; margin: 0 auto;
    }}
    .sidebar-name {{
        text-align: center; color: #E6EDF3; font-weight: bold; font-size: 1.2em; margin-top: 10px;
    }}

    /* Custom Radio Buttons */
    .stRadio > div {{ gap: 10px; }}
    </style>
""", unsafe_allow_html=True)


# =========================================================
# 3. معالجة الصور
# =========================================================
def get_image_src(local_path):
    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/jpg;base64,{encoded}"
    return "https://ui-avatars.com/api/?name=Saif+Aboseada&background=D4AF37&color=000"


default_img_path = "profile.jpg"
img_src = get_image_src(default_img_path)

# =========================================================
# 4. القائمة الجانبية (Sidebar) - طبق الأصل للصورة
# =========================================================
with st.sidebar:
    st.markdown("### Navigation")

    # 1. القائمة (Radio Buttons)
    selected_page = st.radio(
        "Go to",
        ["Profile", "Experience", "Projects", "Skills", "Education", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # 2. إعدادات الأدمن (Expander)
    with st.expander("🔒 Admin Settings"):
        admin_pass = st.text_input("Password", type="password")
        if admin_pass == "12345":
            st.success("Admin Mode Unlocked")
            st.info("Edit features are enabled in code.")
        else:
            if admin_pass: st.error("Wrong Password")

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. الصورة والاسم في الأسفل (زي السكرين شوت)
    st.markdown(f"""
        <div>
            <img src="{img_src}" class="sidebar-img">
            <div class="sidebar-name">Saif Aboseada</div>
        </div>
    """, unsafe_allow_html=True)

# =========================================================
# 5. المحتوى الرئيسي
# =========================================================

# --- PROFILE ---
if selected_page == "Profile":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
            <img src="{img_src}" style="width:200px; height:200px; border-radius:50%; border:4px solid {primary_color}; display:block; margin:0 auto;">
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <h1 style="font-size: 3em; margin-bottom: 0;">SAIF ABOSEADA</h1>
            <h3 style="color: {primary_color} !important; margin-top: 0;">.NET Backend Developer</h3>
            <p style="color: #8B949E; font-size: 1.1em; margin-top: 15px;">
                <i class="fa-solid fa-location-dot" style="color:{primary_color}"></i> Port Said, Egypt
            </p>
            <div style="margin-top: 20px;">
                <a href="https://linkedin.com/in/saif-yehia" target="_blank" style="background:{primary_color}; color:#000; padding:8px 15px; border-radius:5px; font-weight:bold; margin-right:10px;"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
                <a href="https://github.com/Saif-Yehia-Mosaad" target="_blank" style="border:1px solid {primary_color}; color:{primary_color}; padding:8px 15px; border-radius:5px; font-weight:bold;"><i class="fa-brands fa-github"></i> GitHub</a>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3 class='section-header'>Professional Summary</h3>", unsafe_allow_html=True)
    st.markdown("""
    Passionate .NET Backend Developer and Computer Science student with specialized expertise in building scalable Web APIs using 
    **ASP.NET Core** and **SQL Server**. Proficient in implementing **Clean Architecture**, **Repository Pattern**, and securing RESTful services. 
    Seeking a challenging backend or full-stack position to apply advanced C# skills in developing high-performance enterprise solutions.
    """)

# --- EXPERIENCE ---
elif selected_page == "Experience":
    st.markdown("<h2 class='section-header'>Professional Experience</h2>", unsafe_allow_html=True)


    def job_card(role, company, date, tasks):
        task_html = "".join([f"<li>{t}</li>" for t in tasks])
        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between;">
                <div>
                    <div class="card-title">{role}</div>
                    <div class="card-subtitle">{company}</div>
                </div>
                <div style="background:#21262d; padding:5px 10px; border-radius:5px; height:fit-content; font-size:0.85em;">{date}</div>
            </div>
            <ul style="padding-left:20px; color:#C9D1D9;">{task_html}</ul>
        </div>
        """


    st.markdown(job_card(
        "Full Stack .NET Development Trainee", "Digital Egypt Pioneers Initiative (DEPI)", "Nov 2025 - Present",
        [
            "Specialized in Backend Development using ASP.NET Core and SQL Server.",
            "Collaborated with a team to design database schemas and implement business logic.",
            "Mastered version control workflows using Git and GitHub in an Agile environment."
        ]
    ), unsafe_allow_html=True)

# --- PROJECTS ---
elif selected_page == "Projects":
    st.markdown("<h2 class='section-header'>Technical Projects</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)


    def project_card(title, type_tag, items, stack):
        item_html = "".join([f"<li>{i}</li>" for i in items])
        tags = "".join([f"<span class='skill-badge'>{s}</span>" for s in stack])
        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between;">
                <div class="card-title">{title}</div>
                <span style="border:1px solid {primary_color}; color:{primary_color}; font-size:0.7em; padding:2px 6px; border-radius:4px; height:fit-content;">{type_tag}</span>
            </div>
            <ul style="padding-left:15px; font-size:0.95em; color:#8B949E; margin-top:10px;">{item_html}</ul>
            <div style="margin-top:15px; border-top:1px solid #30363D; padding-top:10px;">{tags}</div>
        </div>
        """


    with col1:
        st.markdown(project_card(
            "E-Commerce RESTful API", "Backend",
            ["Developed API using ASP.NET Core & SQL Server.", "Implemented Repository Pattern & Unit of Work.",
             "Designed schemas for products, orders, payments."],
            ["ASP.NET Core", "SQL Server", "Clean Arch"]
        ), unsafe_allow_html=True)
        st.markdown(project_card(
            "Daily Quotes Application", "Full Stack",
            ["RESTful API serving dynamic content.", "Designed robust CRUD endpoints.",
             "Integrated with Flutter mobile app."],
            ["ASP.NET Core", "API", "Mobile"]
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(project_card(
            "Medical Clinic Booking System", "Backend",
            ["Booking system with concurrency control.", "Prevented double-booking with validation logic.",
             "Secured API using JWT & RBAC."],
            ["Web API", "JWT", "Security"]
        ), unsafe_allow_html=True)
        st.markdown(project_card(
            "Auth & Authorization Service", "Microservice",
            ["Dedicated identity service using ASP.NET Identity.", "Implemented JWT tokens & Middleware logging."],
            ["Identity", "Microservices", "JWT"]
        ), unsafe_allow_html=True)

# --- SKILLS ---
elif selected_page == "Skills":
    st.markdown("<h2 class='section-header'>Technical Skills</h2>", unsafe_allow_html=True)


    def skill_group(title, icon, skills):
        badges = "".join([f"<span class='skill-badge'>{s}</span>" for s in skills])
        st.markdown(f"""
            <div style="margin-bottom:20px;">
                <h4 style="color:{text_color}"><i class="{icon}" style="color:{primary_color}; margin-right:10px;"></i> {title}</h4>
                <div>{badges}</div>
            </div>
        """, unsafe_allow_html=True)


    skill_group("Core Technologies", "fa-solid fa-code",
                ["C#", ".NET 6/7/8", "ASP.NET Core Web API", "LINQ", "EF Core"])
    skill_group("Database", "fa-solid fa-database", ["SQL Server", "T-SQL", "Normalization", "Database Design"])
    skill_group("Architecture", "fa-solid fa-sitemap",
                ["MVC", "RESTful APIs", "Repository Pattern", "Unit of Work", "DI"])
    skill_group("Tools & DevOps", "fa-solid fa-wrench", ["Git", "GitHub", "Postman", "Swagger", "Docker (Basics)"])
    skill_group("Testing", "fa-solid fa-vial", ["xUnit", "NUnit", "Unit Testing"])

# --- EDUCATION ---
elif selected_page == "Education":
    st.markdown("<h2 class='section-header'>Education & Certifications</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="custom-card">
                <div class="card-title"><i class="fa-solid fa-graduation-cap" style="color:{primary_color}"></i> Bachelor of Computer Science</div>
                <div class="card-subtitle">Suez Canal University</div>
                <div style="font-size:0.9em; margin-bottom:10px;">Oct 2022 - Present</div>
                <p style="color:#8B949E;">Focus: OOP, Data Structures, Algorithms, Distributed Systems.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="custom-card">
                <div class="card-title"><i class="fa-solid fa-certificate" style="color:{primary_color}"></i> Certifications</div>
                <ul style="padding-left:20px; color:#8B949E;">
                    <li><b>.NET Web Development:</b> 120-hour intensive course.</li>
                    <li><b>Frontend Web Development:</b> 162-hour course.</li>
                    <li><b>AI for Beginners:</b> Issued by HP LIFE.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# --- CONTACT (NEW SECTION) ---
elif selected_page == "Contact":
    st.markdown("<h2 class='section-header'>Get In Touch</h2>", unsafe_allow_html=True)

    c1, c2 = st.columns([2, 1])

    with c1:
        st.markdown("### Send me a message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            msg = st.text_area("Message")
            submit = st.form_submit_button("Send Message")

            if submit:
                st.success(f"Thanks {name}! I will get back to you soon.")

    with c2:
        st.markdown("### Contact Info")
        st.markdown(f"""
            <div class="custom-card">
                <div style="margin-bottom:15px;">
                    <i class="fa-solid fa-envelope" style="color:{primary_color}; width:20px;"></i> 
                    <a href="mailto:saifyehia58@gmail.com">saifyehia58@gmail.com</a>
                </div>
                <div style="margin-bottom:15px;">
                    <i class="fa-solid fa-phone" style="color:{primary_color}; width:20px;"></i> 
                    +20 127-851-3846
                </div>
                <div style="margin-bottom:15px;">
                    <i class="fa-brands fa-linkedin" style="color:{primary_color}; width:20px;"></i> 
                    <a href="https://linkedin.com/in/saif-yehia">LinkedIn Profile</a>
                </div>
                <div>
                    <i class="fa-brands fa-github" style="color:{primary_color}; width:20px;"></i> 
                    <a href="https://github.com/Saif-Yehia-Mosaad">GitHub Profile</a>
                </div>
            </div>
        """, unsafe_allow_html=True)