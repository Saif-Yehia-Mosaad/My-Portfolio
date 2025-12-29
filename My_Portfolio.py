import streamlit as st
import base64
import os

# =========================================================
# 1. إعدادات الصفحة
# =========================================================
st.set_page_config(
    page_title="Saif Aboseada | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 2. القيم الافتراضية
# =========================================================
PROFILE_IMAGE_PATH = "profile.jpg"

# الألوان
default_primary = "#2DD4BF"  # تيل/سماوي
default_gradient_1 = "#4C1D95"  # بنفسجي
default_gradient_2 = "#134E4A"  # تيل
default_bg_base = "#0F172A"  # كحلي غامق

if 'design_mode' not in st.session_state:
    st.session_state['design_mode'] = "Creative Gradient"

# =========================================================
# 3. لوحة الأدمن
# =========================================================
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    with st.expander("🔒 Admin Access"):
        admin_pass = st.text_input("Enter Admin Password", type="password")
        if admin_pass == "12345":
            st.success("Unlocked! 🔓")
            uploaded_file = st.file_uploader("Upload Photo", type=['jpg', 'png', 'jpeg'])
            if uploaded_file:
                with open(PROFILE_IMAGE_PATH, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.rerun()

            st.markdown("---")
            design_mode = st.radio("Style Mode", ["Creative Gradient", "Solid Dark"])

            if design_mode == "Creative Gradient":
                c1, c2 = st.columns(2)
                with c1:
                    gradient_1 = st.color_picker("Glow 1", default_gradient_1)
                with c2:
                    gradient_2 = st.color_picker("Glow 2", default_gradient_2)
            else:
                gradient_1 = default_gradient_1
                gradient_2 = default_gradient_2

            bg_base = st.color_picker("Base BG", default_bg_base)
            primary_color = st.color_picker("Accent Color", default_primary)
        else:
            design_mode = "Creative Gradient"
            gradient_1 = default_gradient_1
            gradient_2 = default_gradient_2
            bg_base = default_bg_base
            primary_color = default_primary

# =========================================================
# 4. تنسيق CSS (الحل النهائي للصورة)
# =========================================================

if design_mode == "Creative Gradient":
    background_css = f"""
        background-color: {bg_base};
        background-image: 
            radial-gradient(at 0% 0%, {gradient_2}80 0px, transparent 50%),
            radial-gradient(at 100% 0%, {gradient_1}80 0px, transparent 50%);
        background-attachment: fixed;
    """
    card_css = f"""
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    """
else:
    background_css = f"background-color: {bg_base};"
    card_css = "background-color: #1E293B; border: 1px solid #334155;"

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
            unsafe_allow_html=True)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    :root {{ --primary: {primary_color}; }}

    .stApp {{
        {background_css}
        font-family: 'Inter', sans-serif;
        color: #F8FAFC;
    }}

    /* Navbar Styling */
    div[data-testid="stRadio"] > div {{
        display: flex; justify-content: center; gap: 10px;
        background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(10px);
        padding: 10px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);
        margin-top: 10px; flex-wrap: wrap;
    }}
    div[role="radiogroup"] label {{
        background: transparent; padding: 8px 16px; border-radius: 12px; transition: 0.3s; 
        border: 1px solid transparent; color: #94A3B8; font-weight: 500; margin: 0 !important;
    }}
    div[role="radiogroup"] label > div:first-child {{ display: None; }}
    div[role="radiogroup"] label:hover {{ color: var(--primary); background: rgba(255,255,255,0.05); }}
    div[role="radiogroup"] label[data-checked="true"] {{
        background: var(--primary) !important; color: #0F172A !important; font-weight: bold;
        box-shadow: 0 0 15px {primary_color}60;
    }}

    /* Mobile Media Query */
    @media (max-width: 600px) {{
        div[data-testid="stRadio"] > div {{
            display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; width: 100%;
        }}
        div[role="radiogroup"] label {{ width: 100%; padding: 6px 4px; font-size: 0.8rem; text-align: center; }}
        h1 {{ font-size: 2.5rem !important; }}
    }}

    /* Cards & Typography */
    .custom-card {{
        {card_css}
        border-radius: 16px; padding: 24px; margin-bottom: 20px; 
        transition: transform 0.3s ease; height: 100%;
    }}
    .custom-card:hover {{ transform: translateY(-5px); border-color: var(--primary); }}

    h1 {{ 
        font-size: 3.5rem !important; 
        background: linear-gradient(to right, #FFFFFF, #94A3B8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .section-header {{ 
        display: inline-block; border-bottom: 2px solid var(--primary); 
        padding-bottom: 5px; margin-bottom: 30px; margin-top: 30px; 
        color: #F1F5F9; font-size: 1.8rem; font-weight: 700;
    }}

    /* ========================================================
       THE PERFECT CIRCLE FIX (الحل النهائي للصورة)
       ======================================================== */
    .nav-logo {{ 
        width: 45px !important; 
        height: 45px !important; 
        border-radius: 50% !important; 
        border: 2px solid var(--primary); 
        object-fit: cover !important; 
        object-position: center top !important;
    }}

    .sidebar-img {{ 
        width: 100px !important; 
        height: 100px !important; 
        border-radius: 50% !important; 
        border: 2px solid var(--primary); 
        object-fit: cover !important; 
        object-position: center top !important;
        display: block; margin: 0 auto; 
    }}

    .profile-hero-img {{
        width: 220px !important;        /* عرض ثابت */
        height: 220px !important;       /* نفس الطول بالظبط */
        border-radius: 50% !important;  /* دائرة كاملة */
        border: 4px solid var(--primary); 
        object-fit: cover !important;   /* يقص الزيادات ويملا الفراغات */
        object-position: center top !important; /* يركز على الوش */
        display: block; 
        margin: 0 auto;
        box-shadow: 0 0 50px {primary_color}40;
    }}
    /* ======================================================== */

    .skill-badge {{
        background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.1); 
        color: #E2E8F0; padding: 6px 14px; border-radius: 30px; 
        font-size: 0.85em; display: inline-block; margin: 4px; backdrop-filter: blur(5px);
    }}
    </style>
""", unsafe_allow_html=True)


# =========================================================
# 5. الهيكل
# =========================================================
def get_image_src(local_path):
    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/jpg;base64,{encoded}"
    return "https://ui-avatars.com/api/?name=Saif+Aboseada&background=0D9488&color=fff&size=256"


img_src = get_image_src(PROFILE_IMAGE_PATH)

col_logo, col_nav = st.columns([1, 10])
with col_logo:
    st.markdown(f'<img src="{img_src}" class="nav-logo">', unsafe_allow_html=True)

with col_nav:
    selected_page = st.radio(
        "Menu",
        ["Profile", "Experience", "Projects", "Skills", "Education", "Contact"],
        horizontal=True,
        label_visibility="collapsed"
    )

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{img_src}" class="sidebar-img">
            <h3 style="margin-top:10px; color:#F1F5F9;">Saif Aboseada</h3>
        </div>
    """, unsafe_allow_html=True)

# =========================================================
# 6. المحتوى الكامل (Full Data)
# =========================================================

if selected_page == "Profile":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown(f'<img src="{img_src}" class="profile-hero-img">', unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div style="padding-top: 10px;">
                <h1>SAIF ABOSEADA</h1>
                <div style="font-size: 1.5rem; color: {primary_color}; font-weight: 600; margin-top: 5px;">.NET Backend Developer</div>
                <p style="color: #94A3B8; font-size: 1.1em; margin-top: 15px; line-height: 1.6;">
                    Port Said, Egypt | +20 127-851-3846
                </p>
                <div style="margin-top: 30px; display: flex; gap: 15px; flex-wrap: wrap;">
                    <a href="https://linkedin.com/in/saif-yehia" target="_blank" style="background:{primary_color}; color:#0F172A; padding:10px 20px; border-radius:30px; font-weight:bold; text-decoration:none;">LinkedIn</a>
                    <a href="https://github.com/Saif-Yehia-Mosaad" target="_blank" style="background: rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); color:#F1F5F9; padding:10px 20px; border-radius:30px; font-weight:bold; text-decoration:none;">GitHub</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>Professional Summary</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="color: #CBD5E1; line-height: 1.8; font-size: 1.05em;">
    Passionate <b>.NET Backend Developer</b> and Computer Science student with specialized expertise in building scalable Web
    APIs using <b>ASP.NET Core</b> and <b>SQL Server</b>. Proficient in implementing <b>Clean Architecture</b>, Repository Pattern, and
    securing RESTful services. Seeking a challenging backend or full-stack position to apply advanced C# skills in
    developing high-performance enterprise solutions.
    </div>
    """, unsafe_allow_html=True)

elif selected_page == "Experience":
    st.markdown("<div class='section-header'>Professional Experience</div>", unsafe_allow_html=True)


    def job_card(role, company, date, tasks):
        task_html = "".join([f"<li style='margin-bottom:8px; line-height: 1.6;'>{t}</li>" for t in tasks])
        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items: center; margin-bottom: 15px; flex-wrap: wrap; gap: 10px;">
                <div><div style="font-weight:700; font-size:1.2em; color:#fff;">{role}</div><div style="color:{primary_color}; font-weight:600;">{company}</div></div>
                <div style="background:rgba(255,255,255,0.1); padding:6px 12px; border-radius:20px; font-size:0.85em;">{date}</div>
            </div>
            <ul style="padding-left:20px; color:#94A3B8;">{task_html}</ul>
        </div>
        """


    st.markdown(job_card(
        "Full Stack .NET Development Trainee",
        "Digital Egypt Pioneers Initiative (DEPI)",
        "Nov 2025 - Present",
        [
            "Specialized in Backend Development using ASP.NET Core and SQL Server.",
            "Collaborated with a team to design database schemas and implement business logic for enterprise-level applications.",
            "Mastered version control workflows using Git and GitHub in an Agile environment."
        ]
    ), unsafe_allow_html=True)

elif selected_page == "Projects":
    st.markdown("<div class='section-header'>Technical Projects</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)


    def proj(title, type_tag, items, stack):
        items_html = "".join([f"<li style='margin-bottom:5px; line-height: 1.5;'>{i}</li>" for i in items])
        tags = "".join([f"<span class='skill-badge'>{s}</span>" for s in stack])
        return f"""
        <div class="custom-card" style="height:100%;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                <div style="font-weight:700; font-size:1.15em; color:#fff;">{title}</div>
                <span style="border:1px solid {primary_color}; color:{primary_color}; font-size:0.7em; padding:2px 6px; border-radius:4px;">{type_tag}</span>
            </div>
            <ul style="padding-left:15px; font-size:0.95em; color:#94A3B8; margin-bottom:20px;">{items_html}</ul>
            <div style="margin-top:auto; border-top:1px solid rgba(255,255,255,0.1); padding-top:15px;">{tags}</div>
        </div>
        """


    with c1:
        st.markdown(proj(
            "E-Commerce RESTful API", "Backend",
            [
                "Developed a comprehensive API for an online store using ASP.NET Core Web API and SQL Server.",
                "Implemented the Repository Pattern and Unit of Work to decouple business logic from data access.",
                "Designed complex database schemas including products, categories, orders, and payment transactions."
            ],
            ["ASP.NET Core", "SQL Server", "Repo Pattern", "Unit of Work"]
        ), unsafe_allow_html=True)
        st.markdown(proj(
            "Daily Quotes Application", "Full Stack",
            [
                "Developed a RESTful API using ASP.NET Core to serve dynamic content to a mobile frontend.",
                "Designed robust endpoints for CRUD operations and integrated with a Flutter mobile application."
            ],
            ["ASP.NET Core", "REST API", "Flutter Integration"]
        ), unsafe_allow_html=True)
        st.markdown(proj(
            "Student Management System", "MVC",
            [
                "Built a classic management application using ASP.NET Core MVC.",
                "Demonstrated strong grasp of Relational Database concepts (One-to-Many, Many-to-Many relationships)."
            ],
            ["ASP.NET Core MVC", "Relational DB", "EF Core"]
        ), unsafe_allow_html=True)

    with c2:
        st.markdown(proj(
            "Medical Clinic Booking System", "Backend",
            [
                "Engineered a booking management system allowing patients to schedule appointments with doctors.",
                "Handled concurrency issues and implemented validation logic to prevent double-booking.",
                "Secured the API using JWT Authentication and Role-Based Access Control (RBAC)."
            ],
            ["Web API", "JWT Auth", "Concurrency Control", "RBAC"]
        ), unsafe_allow_html=True)
        st.markdown(proj(
            "Authentication & Authorization Service", "Microservice",
            [
                "Built a dedicated identity service using ASP.NET Core Identity and JWT tokens.",
                "Implemented custom middleware for error handling and request logging."
            ],
            ["ASP.NET Core Identity", "JWT", "Middleware", "Logging"]
        ), unsafe_allow_html=True)

elif selected_page == "Skills":
    st.markdown("<div class='section-header'>Technical Skills</div>", unsafe_allow_html=True)


    def skill(title, icon, s_list):
        badges = "".join([f"<span class='skill-badge'>{s}</span>" for s in s_list])
        st.markdown(
            f"""<div style="margin-bottom:25px;"><h4 style="color:#E2E8F0;"><i class="{icon}" style="color:{primary_color}; margin-right:10px;"></i> {title}</h4><div style="margin-top:10px;">{badges}</div></div>""",
            unsafe_allow_html=True)


    skill("Core Technologies", "fa-solid fa-code",
          ["C#", ".NET 6/7/8", "ASP.NET Core Web API", "LINQ", "Entity Framework Core (EF Core)"])
    skill("Database Management", "fa-solid fa-database",
          ["Microsoft SQL Server", "T-SQL", "Database Design", "Normalization", "Relationships"])
    skill("Architecture & Patterns", "fa-solid fa-sitemap",
          ["MVC", "RESTful APIs", "Repository Pattern", "Unit of Work", "Dependency Injection (DI)"])
    skill("Tools & DevOps", "fa-solid fa-wrench", ["Git", "GitHub", "Postman", "Swagger UI", "Docker (Basics)"])
    skill("Testing", "fa-solid fa-vial", ["xUnit", "NUnit", "Unit Testing fundamentals"])

elif selected_page == "Education":
    st.markdown("<div class='section-header'>Education & Certifications</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="custom-card">
            <div><i class="fa-solid fa-graduation-cap" style="color:{primary_color}; font-size:1.2em;"></i> <span style="font-weight:700; font-size:1.1em; color:#fff;">Bachelor of Computer Science (CS)</span></div>
            <div style="margin-top:10px; color:{primary_color}; font-weight:600;">Faculty of Computers and Informatics, Suez Canal University</div>
            <div style="font-size:0.9em; margin-top:5px; margin-bottom:15px; color:#94A3B8;">Oct 2022 - Present</div>
            <div style="color:#CBD5E1; line-height:1.6;">Focus: Object-Oriented Programming (OOP), Data Structures, Algorithms, and Distributed Systems.</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="custom-card">
            <div style="margin-bottom:15px;"><i class="fa-solid fa-certificate" style="color:{primary_color}; font-size:1.2em;"></i> <span style="font-weight:700; font-size:1.1em; color:#fff;">Certifications</span></div>
            <ul style="color:#94A3B8; padding-left:20px; line-height:1.7;">
                <li><b>.NET Web Development:</b> 120-hour intensive course covering Advanced C#, SQL Server, and ASP.NET Core.</li>
                <li><b>Frontend Web Development:</b> 162-hour course covering HTML5, CSS3, JavaScript, and Sass.</li>
                <li><b>AI for Beginners:</b> Issued by HP LIFE.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif selected_page == "Contact":
    st.markdown("<div class='section-header'>Get In Touch</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.5, 1])
    with c1:
        with st.form("contact_form"):
            st.text_input("Your Name")
            st.text_input("Your Email")
            st.text_area("Message")

            # هنا التعديل: استخدام Toast بدل Success
            if st.form_submit_button("Send Message"):
                st.toast("Message Sent Successfully! 🚀", icon="🎉")

    with c2:
        st.markdown(f"""
        <div class="custom-card">
            <div style="margin-bottom:15px;"><i class="fa-solid fa-envelope" style="color:{primary_color}; margin-right:10px;"></i> <a href="mailto:saifyehia58@gmail.com" style="color:#fff; text-decoration:none;">saifyehia58@gmail.com</a></div>
            <div style="margin-bottom:15px;"><i class="fa-solid fa-phone" style="color:{primary_color}; margin-right:10px;"></i> +20 127-851-3846</div>
            <div><i class="fa-solid fa-location-dot" style="color:{primary_color}; margin-right:10px;"></i> Port Said, Egypt</div>
        </div>
        """, unsafe_allow_html=True)