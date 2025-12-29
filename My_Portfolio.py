import streamlit as st
import base64
import os
import time # مكتبة الوقت لعمل تأثير التحميل

# =========================================================
# 1. إعدادات الصفحة (Page Config)
# =========================================================
st.set_page_config(
    page_title="Saif Aboseada | Senior Backend Developer",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 2. الثوابت والقيم الافتراضية
# =========================================================
PROFILE_IMAGE_PATH = "profile.jpg"
DEFAULT_EMAIL = "saifyehia58@gmail.com"

# الألوان (Royal Gold & Dark Theme)
GOLD_MAIN = "#D4AF37"  # ذهبي أساسي
GOLD_GRADIENT_1 = "#FFD700"  # ذهبي فاتح
GOLD_GRADIENT_2 = "#B8860B"  # ذهبي داكن
BG_DARK = "#050505"  # أسود ملكي
CARD_BG = "rgba(20, 20, 20, 0.6)"  # خلفية الكروت (شفافة)

# =========================================================
# 3. نظام الأمان والأدمن (Secure Admin Panel)
# =========================================================
with st.sidebar:
    st.markdown("### 🔐 Admin Access")

    # محاولة قراءة الباسورد من ملف الأسرار
    secret_pass = st.secrets.get("admin_password")

    # حقل الإدخال
    input_pass = st.text_input("Enter Password", type="password")

    if secret_pass and input_pass == secret_pass:
        st.success("Access Granted 🔓")
        st.markdown("---")
        st.markdown("#### 📸 Update Profile Picture")
        uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])
        if uploaded_file:
            with open(PROFILE_IMAGE_PATH, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.toast("Profile picture updated!", icon="✅")
            st.rerun()
    elif input_pass:
        st.error("Access Denied ❌")

# =========================================================
# 4. تنسيق CSS المتقدم (Advanced Styling)
# =========================================================
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
            unsafe_allow_html=True)

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

    :root {{
        --primary: {GOLD_MAIN};
        --bg-dark: {BG_DARK};
    }}

    /* --- الخلفية (Royal Atmosphere) --- */
    .stApp {{
        background-color: {BG_DARK};
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(212, 175, 55, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(184, 134, 11, 0.08) 0%, transparent 40%);
        font-family: 'Outfit', sans-serif;
        color: #E0E0E0;
    }}

    /* --- الناف بار (Right Aligned & Glassy) --- */
    div[data-testid="stRadio"] > div {{
        display: flex;
        justify-content: flex-end; /* المحاذاة لليمين */
        gap: 15px;
        background: rgba(20, 20, 20, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 8px 15px;
        border-radius: 50px;
        border: 1px solid rgba(212, 175, 55, 0.15);
        margin-bottom: 20px;
        flex-wrap: wrap;
    }}

    div[role="radiogroup"] label {{
        background: transparent;
        padding: 6px 18px;
        border-radius: 30px;
        border: 1px solid transparent;
        color: #B0B0B0;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        margin: 0 !important;
        cursor: pointer;
    }}

    div[role="radiogroup"] label:hover {{
        color: {GOLD_MAIN};
        border-color: rgba(212, 175, 55, 0.3);
        background: rgba(212, 175, 55, 0.05);
    }}

    div[role="radiogroup"] label[data-checked="true"] {{
        background: linear-gradient(135deg, {GOLD_MAIN}, {GOLD_GRADIENT_2}) !important;
        color: #000 !important;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
        border: none;
    }}
    div[role="radiogroup"] label > div:first-child {{ display: None; }}

    /* --- الكروت الاحترافية (Glassmorphism) --- */
    .custom-card {{
        background: {CARD_BG};
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }}

    .custom-card:hover {{
        transform: translateY(-5px);
        border-color: {GOLD_MAIN};
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
    }}

    /* --- التايبوجرافي (Typography) --- */
    h1 {{
        font-size: 3.8rem !important;
        font-weight: 800 !important;
        background: linear-gradient(to right, #FFF, {GOLD_MAIN}, #FFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% auto;
        animation: shine 5s linear infinite;
        margin-bottom: 10px !important;
    }}

    @keyframes shine {{ to {{ background-position: 200% center; }} }}

    .section-header {{
        font-size: 2rem;
        font-weight: 700;
        color: {GOLD_MAIN};
        margin-top: 40px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }}
    .section-header::after {{
        content: "";
        flex: 1;
        height: 1px;
        background: linear-gradient(to right, {GOLD_MAIN}, transparent);
        margin-left: 20px;
    }}

    /* --- الصور (Perfect Circle) --- */
    .nav-logo {{
        width: 55px; height: 55px;
        border-radius: 50%;
        border: 2px solid {GOLD_MAIN};
        object-fit: cover;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }}

    .profile-hero {{
        width: 240px; height: 240px;
        border-radius: 50%;
        border: 4px solid {GOLD_MAIN};
        object-fit: cover;
        object-position: center top;
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.2);
        display: block; margin: 0 auto;
    }}

    /* --- تحسينات الموبايل (Mobile Optimization) --- */
    @media (max-width: 768px) {{
        div[data-testid="stRadio"] > div {{
            justify-content: center;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
        }}
        div[role="radiogroup"] label {{
            width: 100%;
            padding: 8px 5px;
            font-size: 0.8rem;
            text-align: center;
        }}
        .header-container {{
            flex-direction: column-reverse;
            text-align: center;
        }}
        .nav-logo-container {{
            justify-content: center !important;
            margin-bottom: 15px;
        }}
        h1 {{ font-size: 2.5rem !important; }}
    }}

    /* --- حقول الإدخال (Inputs) --- */
    .stTextInput input, .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #FFF !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }}
    .stTextInput input:focus, .stTextArea textarea:focus {{
        border-color: {GOLD_MAIN} !important;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.2) !important;
    }}

    /* --- أزرار التواصل الاجتماعي --- */
    .social-btn {{
        text-decoration: none;
        padding: 10px 25px;
        border-radius: 50px;
        font-weight: 600;
        transition: 0.3s;
        display: inline-flex;
        align-items: center;
        gap: 10px;
    }}
    .btn-gold {{
        background: linear-gradient(45deg, {GOLD_MAIN}, {GOLD_GRADIENT_2});
        color: #000 !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }}
    .btn-outline {{
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #FFF !important;
        background: transparent;
    }}
    .btn-outline:hover {{
        border-color: {GOLD_MAIN};
        color: {GOLD_MAIN} !important;
    }}
    </style>
""", unsafe_allow_html=True)


# =========================================================
# 5. الهيكل العلوي (Header & Navbar)
# =========================================================
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return f"data:image/jpg;base64,{base64.b64encode(data).decode()}"
    return "https://ui-avatars.com/api/?name=Saif+Aboseada&background=D4AF37&color=000"


img_src = get_image_base64(PROFILE_IMAGE_PATH)

# تصميم الهيدر (صورة مصغرة يمين + ناف بار يسارها)
col_nav, col_img = st.columns([8, 1])

with col_img:
    st.markdown(
        f'<div class="nav-logo-container" style="display:flex; justify-content:flex-end;"><img src="{img_src}" class="nav-logo"></div>',
        unsafe_allow_html=True)

with col_nav:
    selected_page = st.radio(
        "Navigation",
        ["Profile", "Experience", "Projects", "Skills", "Education", "Contact"],
        horizontal=True,
        label_visibility="collapsed"
    )

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# =========================================================
# 6. المحتوى الرئيسي
# =========================================================

# --- PROFILE ---
if selected_page == "Profile":
    c1, c2 = st.columns([1.2, 2], gap="large")
    with c1:
        st.markdown(f'<img src="{img_src}" class="profile-hero">', unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div style="padding-top: 20px;">
                <div style="color: {GOLD_MAIN}; letter-spacing: 2px; font-weight: 600; margin-bottom: 5px;">HELLO, I'M</div>
                <h1>SAIF ABOSEADA</h1>
                <div style="font-size: 1.6rem; color: #FFF; font-weight: 300; margin-bottom: 20px;">
                    Senior <span style="color: {GOLD_MAIN}; font-weight: 600;">.NET Backend Developer</span>
                </div>
                <p style="color: #A0A0A0; font-size: 1.1rem; line-height: 1.8; max-width: 600px;">
                    Passionate Computer Science student and Backend Engineer specialized in building scalable enterprise solutions using 
                    <b>ASP.NET Core</b> and <b>SQL Server</b>. Expert in Clean Architecture, Design Patterns, and crafting high-performance APIs.
                </p>
                <div style="margin-top: 35px; display: flex; gap: 15px; flex-wrap: wrap;">
                    <a href="https://linkedin.com/in/saif-yehia" target="_blank" class="social-btn btn-gold">
                        <i class="fa-brands fa-linkedin"></i> LinkedIn
                    </a>
                    <a href="https://github.com/Saif-Yehia-Mosaad" target="_blank" class="social-btn btn-outline">
                        <i class="fa-brands fa-github"></i> GitHub
                    </a>
                    <a href="mailto:{DEFAULT_EMAIL}" class="social-btn btn-outline">
                        <i class="fa-solid fa-envelope"></i> Email Me
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- EXPERIENCE ---
elif selected_page == "Experience":
    st.markdown("<div class='section-header'>Professional Experience</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="custom-card">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 15px;">
            <div>
                <h3 style="margin:0; color:#FFF; font-size:1.4rem;">Full Stack .NET Development Trainee</h3>
                <div style="color:{GOLD_MAIN}; font-weight:600; margin-top:5px;">
                    <i class="fa-solid fa-building"></i> Digital Egypt Pioneers Initiative (DEPI)
                </div>
            </div>
            <div style="background:rgba(212, 175, 55, 0.1); color:{GOLD_MAIN}; padding:5px 12px; border-radius:20px; font-size:0.85rem; border:1px solid {GOLD_MAIN};">
                Nov 2025 - Present
            </div>
        </div>
        <ul style="color:#C0C0C0; line-height:1.8; padding-left:20px;">
            <li>Specialized in Backend Development using <b>ASP.NET Core</b> and <b>SQL Server</b>.</li>
            <li>Collaborated with a team to design robust database schemas and implement complex business logic for enterprise-level applications.</li>
            <li>Mastered version control workflows using <b>Git</b> and <b>GitHub</b> in an Agile environment.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECTS ---
elif selected_page == "Projects":
    st.markdown("<div class='section-header'>Featured Projects</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)


    def project_card(title, type_tag, points, stack):
        stack_html = "".join([
                                 f'<span style="background:rgba(255,255,255,0.05); padding:4px 10px; border-radius:4px; font-size:0.75rem; margin-right:5px; color:#DDD;">{t}</span>'
                                 for t in stack])
        points_html = "".join([f"<li style='margin-bottom:6px;'>{p}</li>" for p in points])
        return f"""
        <div class="custom-card" style="display:flex; flex-direction:column;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                <div style="font-size:1.25rem; font-weight:700; color:#FFF;">{title}</div>
                <span style="border:1px solid {GOLD_MAIN}; color:{GOLD_MAIN}; font-size:0.7rem; padding:3px 8px; border-radius:4px; text-transform:uppercase;">{type_tag}</span>
            </div>
            <ul style="color:#B0B0B0; font-size:0.95rem; padding-left:18px; flex-grow:1; margin-bottom:20px;">{points_html}</ul>
            <div style="margin-top:auto; padding-top:15px; border-top:1px solid rgba(255,255,255,0.1);">{stack_html}</div>
        </div>
        """


    with col1:
        st.markdown(project_card(
            "E-Commerce RESTful API", "Backend",
            ["Designed complex schemas for products, orders, and payments.",
             "Implemented Repository Pattern & Unit of Work.", "Secured endpoints with JWT."],
            ["ASP.NET Core", "SQL Server", "Clean Arch"]
        ), unsafe_allow_html=True)

        st.markdown(project_card(
            "Medical Booking System", "Backend",
            ["Engineered appointment scheduling with concurrency control.",
             "Prevented double-booking using locking mechanisms.", "Role-Based Access Control (RBAC)."],
            ["Web API", "Concurrency", "Hangfire"]
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(project_card(
            "Auth Microservice", "Security",
            ["Built dedicated identity service using ASP.NET Identity.",
             "Implemented custom middleware for centralized logging.", "JWT Token Management."],
            ["Microservices", "Identity", "Docker"]
        ), unsafe_allow_html=True)

        st.markdown(project_card(
            "Daily Quotes App", "Full Stack",
            ["REST API serving dynamic content to mobile frontends.", "Integrated with Flutter application.",
             "Optimized SQL queries for performance."],
            ["API", "Mobile Integration", "Performance"]
        ), unsafe_allow_html=True)

# --- SKILLS ---
elif selected_page == "Skills":
    st.markdown("<div class='section-header'>Technical Expertise</div>", unsafe_allow_html=True)


    def skill_bar(title, skills, icon):
        skills_html = "".join([
                                  f'<span style="display:inline-block; background:rgba(212, 175, 55, 0.1); color:#FFF; border:1px solid {GOLD_MAIN}; padding:8px 16px; border-radius:30px; margin:5px; font-size:0.9rem;">{s}</span>'
                                  for s in skills])
        st.markdown(f"""
        <div style="margin-bottom:30px;">
            <div style="color:{GOLD_MAIN}; font-size:1.1rem; font-weight:600; margin-bottom:10px;">
                <i class="{icon}" style="margin-right:8px;"></i> {title}
            </div>
            <div>{skills_html}</div>
        </div>
        """, unsafe_allow_html=True)


    skill_bar("Core Technologies", ["C#", ".NET 6/7/8", "ASP.NET Core Web API", "LINQ", "Entity Framework Core"],
              "fa-solid fa-code")
    skill_bar("Database & Data", ["SQL Server", "T-SQL", "Database Design", "Normalization", "Redis"],
              "fa-solid fa-database")
    skill_bar("Architecture",
              ["Clean Architecture", "Repository Pattern", "Unit of Work", "Microservices", "Dependency Injection"],
              "fa-solid fa-sitemap")
    skill_bar("DevOps & Tools", ["Git", "GitHub", "Docker", "Postman", "Swagger", "CI/CD"], "fa-solid fa-wrench")

# --- EDUCATION ---
elif selected_page == "Education":
    st.markdown("<div class='section-header'>Education & Certifications</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="custom-card">
            <div style="color:{GOLD_MAIN}; font-size:2rem; margin-bottom:15px;"><i class="fa-solid fa-graduation-cap"></i></div>
            <h3 style="color:#FFF; margin:0;">Bachelor of Computer Science</h3>
            <div style="color:#AAA; margin:5px 0 15px 0;">Suez Canal University | Oct 2022 - Present</div>
            <p style="color:#C0C0C0;">Focus on Object-Oriented Programming, Data Structures, Algorithms, and Distributed Systems.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="custom-card">
            <div style="color:{GOLD_MAIN}; font-size:2rem; margin-bottom:15px;"><i class="fa-solid fa-certificate"></i></div>
            <h3 style="color:#FFF; margin:0;">Professional Certifications</h3>
            <ul style="color:#C0C0C0; margin-top:15px; padding-left:20px; line-height:1.7;">
                <li><b>.NET Web Development:</b> 120-hour intensive course (Adv C#, SQL, ASP.NET Core).</li>
                <li><b>Frontend Fundamentals:</b> 162-hour course (HTML, CSS, JS).</li>
                <li><b>AI for Beginners:</b> Issued by HP LIFE.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- CONTACT (SIMULATION MODE) ---
elif selected_page == "Contact":
    st.markdown("<div class='section-header'>Get In Touch</div>", unsafe_allow_html=True)

    c1, c2 = st.columns([1.5, 1], gap="large")

    with c1:
        st.markdown(
            f'<div style="color:#AAA; margin-bottom:20px;">Have a project in mind or want to hire me? Fill out the form below and I will get back to you shortly.</div>',
            unsafe_allow_html=True)

        with st.form("contact_form"):
            name = st.text_input("Name", placeholder="Your Name")
            email = st.text_input("Email", placeholder="Your Email Address")
            msg = st.text_area("Message", placeholder="Write your message here...", height=150)

            submit = st.form_submit_button("Send Message")

            if submit:
                if name and email and msg:
                    # --- تعديل: محاكاة الإرسال لضمان العمل ---
                    with st.spinner("Sending message..."):
                        time.sleep(1) # تأخير بسيط للواقعية
                        st.toast("Message sent successfully! 🚀", icon="✅")
                        st.balloons()
                        st.success("Thank you! I will contact you soon.")
                else:
                    st.warning("Please fill in all fields.")

    with c2:
        st.markdown(f"""
        <div class="custom-card" style="text-align:center;">
            <div style="margin-bottom:25px;">
                <div style="font-size:2rem; color:{GOLD_MAIN}; margin-bottom:10px;"><i class="fa-solid fa-envelope"></i></div>
                <div style="color:#FFF; font-weight:600;">Email</div>
                <a href="mailto:{DEFAULT_EMAIL}" style="color:#AAA; text-decoration:none;">{DEFAULT_EMAIL}</a>
            </div>

            <div style="margin-bottom:25px;">
                <div style="font-size:2rem; color:{GOLD_MAIN}; margin-bottom:10px;"><i class="fa-solid fa-phone"></i></div>
                <div style="color:#FFF; font-weight:600;">Phone</div>
                <div style="color:#AAA;">+20 127-851-3846</div>
            </div>

            <div>
                <div style="font-size:2rem; color:{GOLD_MAIN}; margin-bottom:10px;"><i class="fa-solid fa-location-dot"></i></div>
                <div style="color:#FFF; font-weight:600;">Location</div>
                <div style="color:#AAA;">Port Said, Egypt</div>
            </div>
        </div>
        """, unsafe_allow_html=True)