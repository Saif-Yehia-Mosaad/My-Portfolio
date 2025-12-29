import streamlit as st
import base64
import os
from PIL import Image

# =========================================================
# 1. إعدادات الصفحة
# =========================================================
st.set_page_config(
    page_title="Saif Aboseada | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. القائمة الجانبية والإعدادات (Sidebar & Settings)
# =========================================================
with st.sidebar:
    st.header("Navigation")
    menu = st.radio(
        "Go to",
        ["Home", "Experience", "Projects", "Services", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # --- ترس الإعدادات (Popover) ---
    with st.popover("⚙️ Settings"):
        st.markdown("### 🎨 Design Studio")

        # إعدادات الصورة
        st.caption("Profile Photo")
        uploaded_file = st.file_uploader("Change Photo", type=['jpg', 'png', 'jpeg'])
        img_width = st.slider("Size", 120, 300, 200)
        img_shape = st.radio("Shape", ["Circle", "Square"], index=0)
        border_radius = "50%" if img_shape == "Circle" else "15px"

        st.markdown("---")

        # إعدادات الألوان
        st.caption("Theme Colors")
        primary_color = st.color_picker("Accent (Gold)", "#D29922")
        bg_color = st.color_picker("Background", "#0E1117")
        card_bg_color = st.color_picker("Card BG", "#161B22")
        text_color = st.color_picker("Text Color", "#E6EDF3")
        base_font_size = st.slider("Font Size", 14, 20, 16)


# =========================================================
# 3. معالجة الصور
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
        return "https://via.placeholder.com/200"


default_img_path = "profile.jpg"
img_src = get_image_src(uploaded_file, default_img_path)

# =========================================================
# 4. التنسيق (CSS) - التصميم الجديد للمهارات
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
        --font-size: {base_font_size}px;
    }}

    .stApp {{
        background-color: var(--bg-main);
        font-family: 'Inter', sans-serif;
        font-size: var(--font-size);
    }}

    a {{ text-decoration: none; color: inherit; transition: 0.3s; }}
    a:hover {{ color: var(--primary) !important; }}

    /* تنسيق الصورة */
    .profile-img {{
        width: {img_width}px;
        height: {img_width}px;
        border-radius: {border_radius};
        border: 4px solid var(--primary);
        object-fit: cover;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        display: block;
        margin: 0 auto 20px auto;
    }}

    /* تنسيق الكروت */
    .custom-card {{
        background-color: var(--bg-card);
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        transition: transform 0.2s, border-color 0.2s;
    }}
    .custom-card:hover {{
        border-color: var(--primary);
        transform: translateY(-3px);
    }}

    /* --- تنسيق المهارات الجديد (Skill Chips) --- */
    .skill-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
    }}

    .skill-chip {{
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid #30363D;
        border-left: 3px solid var(--primary); /* الخط الملون الجانبي */
        color: var(--text-main);
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 500;
        font-size: 0.9em;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .skill-chip:hover {{
        background-color: var(--primary);
        color: var(--bg-main);
        border-left-color: var(--text-main);
    }}

    /* الأيقونات والعناوين */
    .icon-link {{
        display: flex; align-items: center; gap: 10px;
        color: var(--text-sec); margin-bottom: 10px; font-size: 1.1em;
    }}
    .icon-link i {{ color: var(--primary); width: 25px; text-align: center; }}

    h1, h2, h3 {{ color: var(--text-main) !important; }}
    p, li {{ color: var(--text-sec); }}

    /* صورة Sidebar */
    .sidebar-img {{
        width: 100px; height: 100px; border-radius: {border_radius}; 
        border: 2px solid {primary_color}; object-fit: cover; display: block; margin: 0 auto;
    }}
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 5. صورة القائمة الجانبية
# =========================================================
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="{img_src}" class="sidebar-img">
            <h3 style="margin-top: 10px; font-size: 1.2em;">Saif Aboseada</h3>
            <p style="font-size: 0.9em; opacity: 0.8;">.NET Backend Developer</p>
        </div>
    """, unsafe_allow_html=True)

# =========================================================
# 6. المحتوى الرئيسي
# =========================================================

if menu == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(f'<img class="profile-img" src="{img_src}">', unsafe_allow_html=True)

        # كارت المعلومات الشخصية
        st.markdown(f"""
            <div class="custom-card">
                <a href="#" class="icon-link"><i class="fa-solid fa-location-dot"></i> Port Said, Egypt</a>
                <a href="mailto:saif@example.com" class="icon-link"><i class="fa-solid fa-envelope"></i> saif@example.com</a>
                <a href="https://linkedin.com/in/YOUR_LINKEDIN" target="_blank" class="icon-link"><i class="fa-brands fa-linkedin"></i> LinkedIn Profile</a>
                <a href="https://github.com/YOUR_GITHUB" target="_blank" class="icon-link"><i class="fa-brands fa-github"></i> GitHub Profile</a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <h1 style="font-size: 3em; margin-bottom: 0;">Saif Aboseada</h1>
            <h3 style="color: {primary_color} !important; margin-top: 0;">Senior .NET Backend Developer</h3>
            <p style="font-size: 1.2em; margin-top: 20px; max-width: 650px;">
                Computer Science graduate specializing in building robust, scalable <b>RESTful APIs</b> 
                and high-performance backend systems using <b>ASP.NET Core</b>. 
                Passionate about Clean Architecture, System Design, and Cloud Solutions.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # --- قسم المهارات الجديد (بدون نسب) ---
        st.subheader("🛠️ Technical Stack")


        # دالة لإنشاء شارات المهارات
        def tech_badge_group(title, skills):
            badges_html = "".join([f'<div class="skill-chip">{s}</div>' for s in skills])
            st.markdown(f"""
                <div style="margin-bottom: 15px;">
                    <strong style="color: {primary_color}; font-size: 1.1em;">{title}</strong>
                    <div class="skill-container">
                        {badges_html}
                    </div>
                </div>
            """, unsafe_allow_html=True)


        # عرض المهارات في مجموعات
        tech_badge_group("Backend Core",
                         ["C#", ".NET 8", "ASP.NET Core Web API", "MVC", "SignalR", "LINQ"])

        tech_badge_group("Data & Storage",
                         ["SQL Server", "Entity Framework Core", "Redis", "PostgreSQL", "Dapper"])

        tech_badge_group("Architecture & DevOps",
                         ["Microservices", "Docker", "Clean Architecture", "CI/CD", "Unit Testing", "Git"])

        st.markdown("---")

        # أزرار الإجراءات
        c1, c2 = st.columns([1, 4])
        with c1: st.link_button("📄 Resume", "https://drive.google.com/...")
        with c2: st.link_button("✉️ Hire Me", "mailto:saif@example.com")


elif menu == "Experience":
    st.markdown("<h2><i class='fa-solid fa-briefcase'></i> Professional History</h2>", unsafe_allow_html=True)


    def job_card(role, company, date, tasks):
        task_items = "".join([f"<li style='margin-bottom:6px;'>{t}</li>" for t in tasks])
        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items:start; flex-wrap:wrap;">
                <h3 style="color:{primary_color} !important; margin:0;">{role}</h3>
                <span style="background:rgba(255,255,255,0.1); padding:4px 10px; border-radius:15px; font-size:0.85em;">{date}</span>
            </div>
            <div style="font-weight:bold; margin-bottom:15px; opacity:0.9;"><i class="fa-solid fa-building"></i> {company}</div>
            <ul style="padding-left:20px; opacity:0.85;">{task_items}</ul>
        </div>
        """


    st.markdown(job_card(
        "Full-Stack .NET Trainer", "Digital Pioneers Initiative (DPI)", "Nov 2023 - Present",
        ["Mentored 50+ students in C# and .NET backend concepts.",
         "Designed curriculum for API development and Database design.",
         "Conducted code reviews and technical assessments."]
    ), unsafe_allow_html=True)

    st.markdown(job_card(
        "Freelance Backend Developer", "Remote / Upwork", "Jan 2023 - Present",
        ["Built scalable E-commerce APIs supporting 10k+ products.",
         "Optimized legacy SQL queries improving performance by 40%.",
         "Integrated secure Payment Gateways (Stripe, PayPal)."]
    ), unsafe_allow_html=True)


elif menu == "Projects":
    st.markdown("<h2><i class='fa-solid fa-code'></i> Featured Projects</h2>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)


    def project_card(title, desc, stack, link):
        # تصميم التاجات داخل الكارت
        tags = "".join([
                           f"<span style='background:rgba(210, 153, 34, 0.15); color:{primary_color}; padding:3px 10px; border-radius:4px; font-size:0.8em; margin-right:5px; display:inline-block; margin-top:5px;'>{t}</span>"
                           for t in stack])
        return f"""
        <div class="custom-card" style="height:100%">
            <div style="display:flex; justify-content:space-between;">
                <h3 style="margin:0;">{title}</h3>
                <a href="{link}" target="_blank" style="color:{primary_color};"><i class="fa-brands fa-github"></i></a>
            </div>
            <p style="margin-top:10px; font-size:0.95em;">{desc}</p>
            <div style="margin-top:15px;">{tags}</div>
        </div>
        """


    with c1:
        st.markdown(project_card(
            "Enterprise E-Commerce API", "A complete backend solution with Basket management, Orders, and Identity.",
            ["ASP.NET Core 8", "Redis", "Docker", "Clean Arch"], "https://github.com/..."
        ), unsafe_allow_html=True)
        st.markdown(project_card(
            "Smart Recruitment System", "Graduation project using AI to filter CVs and automate hiring.",
            ["Python", "Streamlit", "SQL Server"], "https://github.com/..."
        ), unsafe_allow_html=True)

    with c2:
        st.markdown(project_card(
            "Medical Booking Platform",
            "SaaS platform handling doctor schedules and patient appointments with concurrency control.",
            ["MVC", "SignalR", "Hangfire"], "https://github.com/..."
        ), unsafe_allow_html=True)
        st.markdown(project_card(
            "Auth Microservice", "Centralized Identity Server implementing OAuth2 & OIDC for secure access.",
            ["IdentityServer", "RabbitMQ", "Microservices"], "https://github.com/..."
        ), unsafe_allow_html=True)


elif menu == "Services":
    st.markdown("<h2><i class='fa-solid fa-layer-group'></i> Services</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)


    def service_box(icon, title, desc):
        return f"""
        <div class="custom-card" style="text-align:center; height:100%;">
            <i class="{icon}" style="font-size:2.5em; margin-bottom:15px; color:{primary_color};"></i>
            <h3 style="font-size:1.3em;">{title}</h3>
            <p style="font-size:0.9em;">{desc}</p>
        </div>
        """


    with col1:
        st.markdown(service_box("fa-solid fa-server", "API Development", "Building secure, documented RESTful APIs."),
                    unsafe_allow_html=True)
    with col2:
        st.markdown(service_box("fa-solid fa-database", "Database Architecture", "Schema design & Performance tuning."),
                    unsafe_allow_html=True)
    with col3:
        st.markdown(service_box("fa-brands fa-docker", "Cloud & DevOps", "Deployment pipelines & Dockerization."),
                    unsafe_allow_html=True)


elif menu == "Contact":
    st.markdown("<h2><i class='fa-solid fa-paper-plane'></i> Get In Touch</h2>", unsafe_allow_html=True)
    with st.form("contact_form"):
        c1, c2 = st.columns(2)
        with c1: st.text_input("Name")
        with c2: st.text_input("Email")
        st.text_area("Message")
        st.form_submit_button("Send Message")