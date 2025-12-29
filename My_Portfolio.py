import streamlit as st
import base64
import os

# =========================================================
# 1. إعدادات الصفحة
# =========================================================
st.set_page_config(
    page_title="Saif Aboseada | Backend Developer",
    page_icon="code",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. نظام الأدمن (للتعديل فقط)
# =========================================================
# القيم الافتراضية للتصميم (Dark & Gold Theme)
default_primary = "#D4AF37"  # ذهبي
default_bg = "#0E1117"  # أسود داكن
default_card = "#161B22"  # رمادي غامق جداً للكروت
default_text = "#E6EDF3"  # أبيض مائل للرمادي
default_font = 16
uploaded_img = None

with st.sidebar:
    st.header("Navigation")
    menu = st.radio(
        "Go to",
        ["Profile", "Experience", "Projects", "Skills", "Education"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # منطقة الأدمن (محمية بكلمة سر)
    with st.expander("🔒 Admin Settings"):
        admin_pass = st.text_input("Password", type="password")
        if admin_pass == "12345":
            st.success("Edit Mode: ON")

            st.markdown("### Design Control")
            # رفع الصورة
            uploaded_img = st.file_uploader("Upload Photo", type=['jpg', 'png', 'jpeg'])
            img_width = st.slider("Photo Size", 120, 300, 180)
            img_shape = st.radio("Photo Shape", ["Circle", "Square"], index=0)

            # الألوان
            primary_color = st.color_picker("Accent Color", default_primary)
            bg_color = st.color_picker("Background", default_bg)
            card_bg_color = st.color_picker("Card BG", default_card)
            text_color = st.color_picker("Text Color", default_text)

            border_radius = "50%" if img_shape == "Circle" else "12px"
        else:
            # القيم الثابتة للزوار
            img_width = 180
            border_radius = "50%"
            primary_color = default_primary
            bg_color = default_bg
            card_bg_color = default_card
            text_color = default_text


# =========================================================
# 3. معالجة الصور والملفات
# =========================================================
def get_image_src(uploaded, local_path):
    if uploaded is not None:
        bytes_data = uploaded.getvalue()
        encoded = base64.b64encode(bytes_data).decode()
        return f"data:image/png;base64,{encoded}"
    elif os.path.exists(local_path):
        with open(local_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/jpg;base64,{encoded}"
    else:
        # Placeholder احترافي لو مفيش صورة
        return "https://ui-avatars.com/api/?name=Saif+Aboseada&background=D4AF37&color=000"


default_img_path = "profile.jpg"
img_src = get_image_src(uploaded_img, default_img_path)

# ملف الـ CV
resume_path = "Saif_Eldien_Backend_CV.pdf"  # تأكد من تغيير الاسم لو مختلف
resume_data = None
if os.path.exists(resume_path):
    with open(resume_path, "rb") as f:
        resume_data = f.read()

# =========================================================
# 4. التنسيق المتقدم (Advanced CSS)
# =========================================================
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
        --text-sec: #8B949E;
    }}

    .stApp {{ background-color: var(--bg-main); font-family: 'Inter', sans-serif; }}

    /* تنسيق الصورة الشخصية */
    .profile-img {{
        width: {img_width}px; height: {img_width}px; border-radius: {border_radius};
        border: 3px solid var(--primary); object-fit: cover;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2); display: block; margin: 0 auto 20px auto;
    }}

    /* === توحيد أطوال الكروت (Equal Height) === */
    [data-testid="column"] {{
        display: flex;
        flex-direction: column;
    }}

    .custom-card {{
        background-color: var(--bg-card); 
        border: 1px solid #30363D;
        border-radius: 8px; 
        padding: 24px; 
        margin-bottom: 20px;
        flex: 1; /* يجعل الكارت يتمدد ليملأ الطول */
        transition: transform 0.2s, border-color 0.2s;
        display: flex;
        flex-direction: column;
    }}
    .custom-card:hover {{ border-color: var(--primary); transform: translateY(-3px); }}

    /* النصوص داخل الكروت */
    .card-title {{ color: var(--text-main); font-weight: 700; font-size: 1.1em; margin-bottom: 5px; }}
    .card-subtitle {{ color: var(--primary); font-size: 0.9em; font-weight: 600; margin-bottom: 10px; }}
    .card-text {{ color: var(--text-sec); font-size: 0.95em; line-height: 1.6; flex-grow: 1; }}

    /* تنسيق المهارات (بدون إيموجي) */
    .skill-badge {{
        background-color: transparent;
        border: 1px solid #30363D;
        color: var(--text-main);
        padding: 6px 14px;
        border-radius: 4px;
        font-size: 0.85em;
        font-weight: 500;
        display: inline-block;
        margin: 4px;
        transition: all 0.2s;
    }}
    .skill-badge:hover {{ border-color: var(--primary); color: var(--primary); }}

    /* العناوين والأيقونات */
    h1, h2, h3 {{ color: var(--text-main) !important; letter-spacing: -0.5px; }}
    .section-header {{ border-bottom: 2px solid #30363D; padding-bottom: 10px; margin-bottom: 25px; margin-top: 10px; }}
    .icon-box {{ color: var(--primary); margin-right: 10px; width: 20px; text-align: center; }}

    /* الروابط */
    a {{ text-decoration: none; color: inherit; transition: 0.3s; }}
    a:hover {{ color: var(--primary) !important; }}

    /* زرار التحميل */
    .stDownloadButton button {{
        width: 100%;
        background-color: transparent !important;
        border: 1px solid var(--primary) !important;
        color: var(--primary) !important;
        border-radius: 6px;
    }}
    .stDownloadButton button:hover {{ background-color: rgba(212, 175, 55, 0.1) !important; }}
    </style>
""", unsafe_allow_html=True)

# صورة السايد بار
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="{img_src}" style="width: 80px; height: 80px; border-radius: {border_radius}; border: 2px solid {primary_color}; object-fit: cover;">
            <h3 style="margin-top: 10px; font-size: 1.1em; color: {text_color};">Saif Aboseada</h3>
        </div>
    """, unsafe_allow_html=True)

    if resume_data:
        st.download_button(
            label="Download Resume (PDF)",
            data=resume_data,
            file_name="Saif_Aboseada_Backend_CV.pdf",
            mime="application/pdf"
        )

# =========================================================
# 5. المحتوى الرئيسي (Main Content)
# =========================================================

# --- Header / Profile ---
if menu == "Profile":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f'<img class="profile-img" src="{img_src}">', unsafe_allow_html=True)
        # معلومات الاتصال
        st.markdown(f"""
            <div class="custom-card" style="text-align: center; padding: 15px;">
                <div style="margin-bottom: 8px;"><i class="fa-solid fa-location-dot icon-box"></i> Port Said, Egypt</div>
                <div style="margin-bottom: 8px;"><i class="fa-solid fa-phone icon-box"></i> +20 127-851-3846</div>
                <div style="margin-bottom: 8px;"><a href="mailto:saifyehia58@gmail.com"><i class="fa-solid fa-envelope icon-box"></i> saifyehia58@gmail.com</a></div>
                <div style="display: flex; justify-content: center; gap: 15px; margin-top: 10px;">
                    <a href="https://www.linkedin.com/in/saif-yehia/" target="_blank"><i class="fa-brands fa-linkedin fa-lg"></i></a>
                    <a href="https://github.com/Saif-Yehia-Mosaad" target="_blank"><i class="fa-brands fa-github fa-lg"></i></a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <h1 style="font-size: 2.8em; margin-bottom: 5px;">SAIF ABOSEADA</h1>
            <h3 style="color: {primary_color} !important; font-weight: 400; margin-top: 0;">.NET Backend Developer</h3>
            <div style="margin-top: 20px; color: {text_color}; line-height: 1.7;">
                Passionate .NET Backend Developer and Computer Science student with specialized expertise in building 
                scalable Web APIs using <b>ASP.NET Core</b> and <b>SQL Server</b>. Proficient in implementing 
                <b>Clean Architecture</b>, <b>Repository Pattern</b>, and securing RESTful services. 
                Seeking a challenging backend position to apply advanced C# skills in developing high-performance enterprise solutions.
            </div>
        """, unsafe_allow_html=True)


# --- Experience ---
elif menu == "Experience":
    st.markdown("<h2 class='section-header'>Professional Experience</h2>", unsafe_allow_html=True)


    # دالة لعرض الخبرة
    def job_entry(role, company, date, tasks):
        task_list = "".join([f"<li style='margin-bottom:6px;'>{t}</li>" for t in tasks])
        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 10px;">
                <div>
                    <div class="card-title">{role}</div>
                    <div class="card-subtitle"><i class="fa-solid fa-building icon-box" style="margin-left:0; width:auto;"></i> {company}</div>
                </div>
                <div style="font-size: 0.85em; background: rgba(255,255,255,0.05); padding: 4px 10px; border-radius: 4px; white-space: nowrap;">{date}</div>
            </div>
            <ul style="padding-left: 20px; color: {default_text}; opacity: 0.9;">{task_list}</ul>
        </div>
        """


    # البيانات من الـ CV بدقة (مع تعديل التاريخ لـ 2025)
    st.markdown(job_entry(
        "Full Stack .NET Development Trainee",
        "Digital Egypt Pioneers Initiative (DEPI)",
        "Nov 2025 - Present",
        [
            "Specialized in Backend Development using ASP.NET Core and SQL Server.",
            "Collaborated with a team to design database schemas and implement business logic for enterprise-level applications.",
            "Mastered version control workflows using Git and GitHub in an Agile environment."
        ]
    ), unsafe_allow_html=True)


# --- Projects ---
elif menu == "Projects":
    st.markdown("<h2 class='section-header'>Technical Projects</h2>", unsafe_allow_html=True)


    # دالة المشاريع
    def project_card(title, tech_type, desc_list, stack_tags):
        items = "".join([f"<li>{item}</li>" for item in desc_list])
        tags = "".join([f"<span class='skill-badge' style='font-size: 0.75em;'>{t}</span>" for t in stack_tags])

        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div class="card-title">{title}</div>
                <span style="font-size:0.7em; border:1px solid {primary_color}; color:{primary_color}; padding:2px 6px; border-radius:4px;">{tech_type}</span>
            </div>
            <div class="card-text">
                <ul style="padding-left: 15px; margin-top: 10px;">{items}</ul>
            </div>
            <div style="margin-top: 15px; border-top: 1px solid #30363D; padding-top: 10px;">
                {tags}
            </div>
        </div>
        """


    # الصف الأول
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(project_card(
            "E-Commerce RESTful API",
            "Backend",
            [
                "Developed a comprehensive API using ASP.NET Core and SQL Server.",
                "Implemented Repository Pattern and Unit of Work.",
                "Designed complex schemas: products, categories, orders, payments."
            ],
            ["ASP.NET Core", "SQL Server", "Repository Pattern"]
        ), unsafe_allow_html=True)

    with c2:
        st.markdown(project_card(
            "Medical Clinic Booking System",
            "Backend",
            [
                "Engineered booking system allowing patients to schedule appointments.",
                "Handled concurrency & validation to prevent double-booking.",
                "Secured API using JWT Auth & Role-Based Access Control (RBAC)."
            ],
            ["Web API", "JWT", "Concurrency Control"]
        ), unsafe_allow_html=True)

    # الصف الثاني
    c3, c4 = st.columns(2)
    with c3:
        st.markdown(project_card(
            "Daily Quotes Application",
            "Full Stack",
            [
                "Developed RESTful API serving dynamic content to mobile apps.",
                "Designed robust endpoints for CRUD operations.",
                "Integrated with a Flutter mobile application."
            ],
            ["ASP.NET Core", "REST API", "Mobile Integration"]
        ), unsafe_allow_html=True)

    with c4:
        st.markdown(project_card(
            "Auth & Authorization Service",
            "Microservice",
            [
                "Built dedicated identity service using ASP.NET Core Identity & JWT.",
                "Implemented custom middleware for error handling and logging."
            ],
            ["Identity", "Middleware", "Security"]
        ), unsafe_allow_html=True)

    # الصف الثالث
    c5, c6 = st.columns(2)
    with c5:
        st.markdown(project_card(
            "Student Management System",
            "MVC",
            [
                "Built classic management application using ASP.NET Core MVC.",
                "Managed complex Relational Database concepts (One-to-Many, Many-to-Many)."
            ],
            ["MVC", "Relational DB", "EF Core"]
        ), unsafe_allow_html=True)
    with c6:
        # كارت فارغ للحفاظ على التنسيق أو ممكن إضافة مشروع مستقبلي
        pass


# --- Skills ---
elif menu == "Skills":
    st.markdown("<h2 class='section-header'>Technical Skills</h2>", unsafe_allow_html=True)


    def skill_section(title, icon, skills_list):
        badges = "".join([f"<span class='skill-badge'>{s}</span>" for s in skills_list])
        st.markdown(f"""
            <div style="margin-bottom: 25px;">
                <h4 style="color: {text_color}; margin-bottom: 10px;"><i class="{icon} icon-box"></i> {title}</h4>
                <div>{badges}</div>
            </div>
        """, unsafe_allow_html=True)


    skill_section("Core Technologies", "fa-solid fa-code",
                  ["C#", ".NET 6/7/8", "ASP.NET Core Web API", "LINQ", "Entity Framework Core"])

    skill_section("Database Management", "fa-solid fa-database",
                  ["SQL Server", "T-SQL", "Database Design", "Normalization"])

    skill_section("Architecture & Patterns", "fa-solid fa-sitemap",
                  ["MVC", "RESTful APIs", "Repository Pattern", "Unit of Work", "Dependency Injection"])

    skill_section("Tools & DevOps", "fa-solid fa-wrench",
                  ["Git", "GitHub", "Postman", "Swagger UI", "Docker (Basics)"])

    skill_section("Testing", "fa-solid fa-vial",
                  ["xUnit", "NUnit", "Unit Testing Fundamentals"])


# --- Education & Certifications ---
elif menu == "Education":
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("<h3 class='section-header'>Education</h3>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class="custom-card">
                <div class="card-title">Bachelor of Computer Science</div>
                <div class="card-subtitle">Suez Canal University</div>
                <div style="font-size: 0.9em; margin-bottom: 10px; color: {primary_color};">Oct 2022 - Present</div>
                <div class="card-text">
                    Focus on OOP, Data Structures, Algorithms, and Distributed Systems.
                </div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("<h3 class='section-header'>Certifications</h3>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class="custom-card">
                <ul style="padding-left: 20px; color: {default_text}; line-height: 1.8;">
                    <li><b>.NET Web Development:</b> 120-hour intensive course (Adv C#, SQL, ASP.NET Core).</li>
                    <li><b>Frontend Web Development:</b> 162-hour course (HTML, CSS, JS, Sass).</li>
                    <li><b>AI for Beginners:</b> Issued by HP LIFE.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)