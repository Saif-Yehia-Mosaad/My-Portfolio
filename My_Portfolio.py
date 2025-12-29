import streamlit as st
import base64
import os
from PIL import Image

# =========================================================
# 1. إعدادات الصفحة
# =========================================================
st.set_page_config(
    page_title="Saif Aboseada | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 2. القيم الافتراضية
# =========================================================
PROFILE_IMAGE_PATH = "profile.jpg"

# الألوان (Outlier Style)
default_primary = "#2DD4BF"  # تيل/سماوي
default_gradient_1 = "#4C1D95"  # بنفسجي غامق
default_gradient_2 = "#134E4A"  # تيل غامق
default_bg_base = "#0F172A"  # كحلي غامق جداً

if 'design_mode' not in st.session_state:
    st.session_state['design_mode'] = "Creative Gradient"

# =========================================================
# 3. لوحة الأدمن (ADMIN PANEL)
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
            design_mode = st.radio("Style Mode", ["Creative Gradient", "Solid Dark"], index=0)

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
# 4. منطق CSS (Responsive & Perfect Circle)
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

    /* --- Navbar Styling --- */
    div[data-testid="stRadio"] > div {{
        display: flex; justify-content: center; gap: 15px;
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(10px);
        padding: 8px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);
        margin-top: -20px;
        flex-wrap: wrap; /* يسمح للأزرار تنزل سطر جديد لو الشاشة ضيقة */
    }}
    div[role="radiogroup"] label > div:first-child {{ display: None; }}
    div[role="radiogroup"] label {{
        padding: 6px 16px; border-radius: 12px; transition: 0.3s; 
        border: 1px solid transparent; color: #94A3B8; font-weight: 500;
        white-space: nowrap; /* يمنع النص يتقسم */
    }}
    div[role="radiogroup"] label:hover {{ color: var(--primary); background: rgba(255,255,255,0.05); }}
    div[role="radiogroup"] label[data-checked="true"] {{
        background: var(--primary) !important; color: #0F172A !important; font-weight: bold;
        box-shadow: 0 0 15px {primary_color}60;
    }}

    /* --- Cards --- */
    .custom-card {{
        {card_css}
        border-radius: 16px; padding: 24px; margin-bottom: 20px; 
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .custom-card:hover {{ 
        transform: translateY(-5px); border-color: var(--primary);
        box-shadow: 0 10px 40px -10px rgba(0,0,0,0.5); 
    }}

    /* --- Typography --- */
    h1 {{ 
        font-size: 3.5rem !important; font-weight: 800 !important;
        background: linear-gradient(to right, #FFFFFF, #94A3B8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0 !important;
    }}
    .role-text {{
        font-size: 1.5rem; color: var(--primary); font-weight: 600; 
        margin-top: 5px; text-shadow: 0 0 20px {primary_color}40;
    }}
    .section-header {{ 
        display: inline-block; border-bottom: 2px solid var(--primary); 
        padding-bottom: 5px; margin-bottom: 30px; margin-top: 10px; 
        color: #F1F5F9; font-size: 1.8rem; font-weight: 700;
    }}

    /* --- PERFECT CIRCLE IMAGE FIX --- */
    .nav-logo, .sidebar-img {{ 
        border-radius: 50%; border: 2px solid var(--primary); 
        object-fit: cover; aspect-ratio: 1/1; 
    }}
    .nav-logo {{ width: 45px; height: 45px; }}
    .sidebar-img {{ width: 100px; height: 100px; display: block; margin: 0 auto; }}

    .profile-hero-img {{
        width: 220px; 
        height: 220px; 
        border-radius: 50%; 
        border: 4px solid var(--primary); 
        object-fit: cover;      /* يملأ الدائرة بالكامل */
        object-position: center top; /* يركز على الوجه */
        aspect-ratio: 1/1;      /* يضمن إنها دائرة مش بيضاوية */
        display: block; 
        margin: 0 auto;
        box-shadow: 0 0 50px {primary_color}40;
    }}

    /* --- MOBILE RESPONSIVENESS (MEDIA QUERIES) --- */
    @media (max-width: 768px) {{
        /* تعديل القائمة في الموبايل */
        div[data-testid="stRadio"] > div {{
            gap: 5px;
            padding: 5px;
        }}
        div[role="radiogroup"] label {{
            padding: 5px 10px;
            font-size: 0.85rem;
        }}

        /* تصغير النصوص والصور في الموبايل */
        h1 {{ font-size: 2.2rem !important; text-align: center; }}
        .role-text {{ font-size: 1.2rem; text-align: center; }}
        p {{ text-align: center; font-size: 1rem; }}
        .profile-hero-img {{ width: 160px; height: 160px; }}

        /* توسيط الأزرار في الموبايل */
        .social-buttons {{ display: flex; justify-content: center; margin-top: 20px; }}
    }}

    /* Contact Form & Badges */
    div[data-testid="stForm"] {{ {card_css} padding: 25px; border-radius: 16px; }}
    .skill-badge {{
        background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.1); 
        color: #E2E8F0; padding: 6px 14px; border-radius: 30px; 
        font-size: 0.85em; display: inline-block; margin: 4px; backdrop-filter: blur(5px);
    }}
    </style>
""", unsafe_allow_html=True)


# =========================================================
# 5. جلب الصورة
# =========================================================
def get_image_src(local_path):
    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/jpg;base64,{encoded}"
    return "https://ui-avatars.com/api/?name=Saif+Aboseada&background=0D9488&color=fff&size=256"


img_src = get_image_src(PROFILE_IMAGE_PATH)

# =========================================================
# 6. الهيكل العام
# =========================================================
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

st.markdown("<br>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{img_src}" class="sidebar-img">
            <h3 style="margin-top:10px; color:#F1F5F9;">Saif Aboseada</h3>
        </div>
    """, unsafe_allow_html=True)

# =========================================================
# 7. المحتوى الرئيسي
# =========================================================

if selected_page == "Profile":
    # في الموبايل، الـ Columns بتيجي تحت بعض، فده هيظبط الترتيب أوتوماتيك
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown(f'<img src="{img_src}" class="profile-hero-img">', unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div style="padding-top: 10px;">
                <h1>SAIF ABOSEADA</h1>
                <div class="role-text">.NET Backend Developer</div>
                <p style="color: #94A3B8; font-size: 1.1em; margin-top: 15px; line-height: 1.6;">
                    Building scalable, secure, and high-performance APIs. 
                    Specialized in <b>ASP.NET Core</b> architecture and database optimization.
                </p>
                <div class="social-buttons" style="margin-top: 30px;">
                    <a href="https://linkedin.com/in/saif-yehia" target="_blank" style="background:{primary_color}; color:#0F172A; padding:12px 25px; border-radius:30px; font-weight:bold; margin-right:15px; text-decoration:none; box-shadow: 0 4px 15px {primary_color}40;">
                        <i class="fa-brands fa-linkedin"></i> LinkedIn
                    </a>
                    <a href="https://github.com/Saif-Yehia-Mosaad" target="_blank" style="background: rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); color:#F1F5F9; padding:12px 25px; border-radius:30px; font-weight:bold; text-decoration:none;">
                        <i class="fa-brands fa-github"></i> GitHub
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>About Me</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="color: #CBD5E1; font-size: 1.05em; line-height: 1.8;">
    Passionate <b>.NET Backend Developer</b> and Computer Science student. I don't just write code; I design systems. 
    My expertise lies in crafting robust <b>RESTful APIs</b> using <b>ASP.NET Core</b> and orchestrating data with <b>SQL Server</b>. 
    I advocate for <b>Clean Architecture</b> and strictly adhere to SOLID principles to ensure maintainability and scalability.
    </div>
    """, unsafe_allow_html=True)

elif selected_page == "Experience":
    st.markdown("<div class='section-header'>Experience</div>", unsafe_allow_html=True)


    def job_card(role, company, date, tasks):
        task_html = "".join([f"<li style='margin-bottom:8px;'>{t}</li>" for t in tasks])
        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items: center; margin-bottom: 15px; flex-wrap: wrap; gap: 10px;">
                <div>
                    <div style="color:#F8FAFC; font-weight:700; font-size:1.2em;">{role}</div>
                    <div style="color:{primary_color}; font-weight:600;">{company}</div>
                </div>
                <div style="background:rgba(255,255,255,0.1); padding:6px 12px; border-radius:20px; font-size:0.85em; color:#E2E8F0;">{date}</div>
            </div>
            <ul style="padding-left:20px; color:#94A3B8;">{task_html}</ul>
        </div>
        """


    st.markdown(job_card("Full Stack .NET Development Trainee", "Digital Egypt Pioneers Initiative (DEPI)",
                         "Nov 2025 - Present", ["Specialized in Backend Development using ASP.NET Core and SQL Server.",
                                                "Collaborated with a team to design database schemas.",
                                                "Mastered version control workflows using Git and GitHub."]),
                unsafe_allow_html=True)

elif selected_page == "Projects":
    st.markdown("<div class='section-header'>Featured Projects</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)


    def proj(title, type_tag, items, stack):
        items_html = "".join([f"<li>{i}</li>" for i in items])
        tags = "".join([f"<span class='skill-badge'>{s}</span>" for s in stack])
        return f"""
        <div class="custom-card" style="height: 100%;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="color:#F8FAFC; font-weight:700; font-size:1.15em;">{title}</div>
                <span style="border:1px solid {primary_color}; color:{primary_color}; font-size:0.75em; padding:3px 8px; border-radius:6px;">{type_tag}</span>
            </div>
            <ul style="padding-left:15px; font-size:0.95em; color:#94A3B8; margin-top:15px; margin-bottom: 20px;">{items_html}</ul>
            <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:15px;">{tags}</div>
        </div>
        """


    with c1:
        st.markdown(proj("E-Commerce RESTful API", "Backend",
                         ["Developed API using ASP.NET Core & SQL Server.", "Implemented Repository Pattern."],
                         ["ASP.NET Core", "SQL Server", "Redis"]), unsafe_allow_html=True)
        st.markdown(proj("Daily Quotes Application", "Full Stack",
                         ["RESTful API serving dynamic content.", "Integrated with Flutter mobile app."],
                         ["ASP.NET Core", "API", "Flutter"]), unsafe_allow_html=True)
    with c2:
        st.markdown(proj("Medical Clinic Booking System", "Backend",
                         ["Booking system with concurrency control.", "Secured API using JWT & RBAC."],
                         ["Web API", "JWT", "Hangfire"]), unsafe_allow_html=True)
        st.markdown(proj("Auth & Authorization Service", "Microservice",
                         ["Dedicated identity service using ASP.NET Identity.", "Implemented JWT tokens."],
                         ["Identity", "Microservices", "Docker"]), unsafe_allow_html=True)

elif selected_page == "Skills":
    st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)


    def skill_group(title, icon, skills):
        badges = "".join([f"<span class='skill-badge'>{s}</span>" for s in skills])
        st.markdown(
            f"""<div style="margin-bottom:25px;"><h4 style="color:#E2E8F0 !important;"><i class="{icon}" style="color:{primary_color}; margin-right:10px;"></i> {title}</h4><div style="margin-top:10px;">{badges}</div></div>""",
            unsafe_allow_html=True)


    skill_group("Core Technologies", "fa-solid fa-code", ["C#", ".NET 8", "ASP.NET Core", "LINQ", "EF Core"])
    skill_group("Database", "fa-solid fa-database", ["SQL Server", "T-SQL", "Design & Normalization"])
    skill_group("Architecture", "fa-solid fa-sitemap",
                ["Clean Architecture", "RESTful APIs", "Repository Pattern", "CQRS", "Microservices"])
    skill_group("DevOps & Tools", "fa-solid fa-wrench", ["Docker", "Git", "GitHub", "Postman", "CI/CD"])

elif selected_page == "Education":
    st.markdown("<div class='section-header'>Education</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"""<div class="custom-card"><div style="color:#F8FAFC; font-weight:700; font-size:1.1em;"><i class="fa-solid fa-graduation-cap" style="color:{primary_color}"></i> Bachelor of Computer Science</div><div style="color:{primary_color}; font-weight:600; margin-top:5px;">Suez Canal University</div><div style="font-size:0.9em; margin-top:5px; color:#94A3B8;">Oct 2022 - Present</div></div>""",
            unsafe_allow_html=True)
    with c2:
        st.markdown(
            f"""<div class="custom-card"><div style="color:#F8FAFC; font-weight:700; font-size:1.1em;"><i class="fa-solid fa-certificate" style="color:{primary_color}"></i> Certifications</div><ul style="padding-left:20px; color:#94A3B8; margin-top:10px;"><li>.NET Web Development</li><li>Frontend Web Development</li><li>AI for Beginners</li></ul></div>""",
            unsafe_allow_html=True)

elif selected_page == "Contact":
    st.markdown("<div class='section-header'>Get In Touch</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.5, 1])
    with c1:
        with st.form("contact_form"):
            st.text_input("Your Name")
            st.text_input("Your Email")
            st.text_area("Message")
            if st.form_submit_button("Send Message"): st.success("Message Sent!")
    with c2:
        st.markdown(
            f"""<div class="custom-card"><div style="margin-bottom:15px;"><i class="fa-solid fa-envelope" style="color:{primary_color};"></i> <a href="mailto:saifyehia58@gmail.com" style="color:#F1F5F9;">saifyehia58@gmail.com</a></div><div style="margin-bottom:15px;"><i class="fa-solid fa-phone" style="color:{primary_color};"></i> <span style="color:#F1F5F9;">+20 127-851-3846</span></div></div>""",
            unsafe_allow_html=True)