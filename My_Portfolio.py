import streamlit as st
import base64
import os

# =========================================================
# 1. إعدادات الصفحة
# =========================================================
st.set_page_config(
    page_title="Saif Aboseada | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. نظام الأدمن (ADMIN SYSTEM)
# =========================================================
# المتغيرات الافتراضية (لو مفيش أدمن فاتح)
default_primary = "#D29922"
default_bg = "#0E1117"
default_card = "#161B22"
default_text = "#E6EDF3"
default_font = 16
uploaded_img = None

with st.sidebar:
    st.header("Navigation")
    menu = st.radio(
        "Go to",
        ["Home", "Experience", "Projects", "Services", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # --- منطقة الأدمن (محمية بكلمة سر) ---
    with st.expander("🔒 Admin Access"):
        # ⚠️ هنا كلمة السر (غيرها براحتك)
        admin_pass = st.text_input("Password", type="password")

        if admin_pass == "12345":  # <--- غير الرقم ده لكلمة سر خاصة بيك
            st.success("Unlocked! You can edit now.")

            st.markdown("### 🎨 Edit Design")

            # رفع الصورة
            st.caption("Profile Photo")
            uploaded_img = st.file_uploader("Change Photo", type=['jpg', 'png', 'jpeg'])
            img_width = st.slider("Size", 120, 300, 200)
            img_shape = st.radio("Shape", ["Circle", "Square"], index=0)

            # الألوان
            st.caption("Colors")
            primary_color = st.color_picker("Accent (Gold)", default_primary)
            bg_color = st.color_picker("Background", default_bg)
            card_bg_color = st.color_picker("Card BG", default_card)
            text_color = st.color_picker("Text Color", default_text)
            base_font_size = st.slider("Font Size", 14, 20, default_font)

            # المتغيرات هتتحدث بناء على اختيارك
            border_radius = "50%" if img_shape == "Circle" else "15px"

        else:
            # لو الزائر عادي أو الباسورد غلط، نستخدم القيم الافتراضية
            img_width = 200
            border_radius = "50%"
            primary_color = default_primary
            bg_color = default_bg
            card_bg_color = default_card
            text_color = default_text
            base_font_size = default_font
            if admin_pass != "":
                st.error("Wrong Password")


# =========================================================
# 3. معالجة الملفات (صور و PDF)
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


# صورة البروفايل
default_img_path = "profile.jpg"
img_src = get_image_src(uploaded_img, default_img_path)

# =========================================================
# 4. التنسيق (CSS)
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

    .stApp {{ background-color: var(--bg-main); font-family: 'Inter', sans-serif; font-size: var(--font-size); }}
    a {{ text-decoration: none; color: inherit; transition: 0.3s; }}
    a:hover {{ color: var(--primary) !important; }}

    /* صورة البروفايل */
    .profile-img {{
        width: {img_width}px; height: {img_width}px; border-radius: {border_radius};
        border: 4px solid var(--primary); object-fit: cover;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3); display: block; margin: 0 auto 20px auto;
    }}

    /* الكروت */
    .custom-card {{
        background-color: var(--bg-card); border: 1px solid #30363D;
        border-radius: 12px; padding: 25px; margin-bottom: 20px;
        transition: transform 0.2s, border-color 0.2s;
    }}
    .custom-card:hover {{ border-color: var(--primary); transform: translateY(-3px); }}

    /* Skill Chips */
    .skill-container {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; }}
    .skill-chip {{
        background-color: rgba(255, 255, 255, 0.05); border: 1px solid #30363D;
        border-left: 3px solid var(--primary); color: var(--text-main);
        padding: 8px 16px; border-radius: 6px; font-weight: 500; font-size: 0.9em;
    }}

    /* Sidebar Image */
    .sidebar-img {{
        width: 100px; height: 100px; border-radius: {border_radius}; 
        border: 2px solid {primary_color}; object-fit: cover; display: block; margin: 0 auto;
    }}

    /* العناوين والأيقونات */
    .icon-link {{ display: flex; align-items: center; gap: 10px; color: var(--text-sec); margin-bottom: 10px; font-size: 1.1em; }}
    .icon-link i {{ color: var(--primary); width: 25px; text-align: center; }}
    h1, h2, h3 {{ color: var(--text-main) !important; }}
    p, li {{ color: var(--text-sec); }}

    /* زرار التحميل */
    .stDownloadButton button {{
        background-color: transparent !important;
        border: 2px solid var(--primary) !important;
        color: var(--primary) !important;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }}
    .stDownloadButton button:hover {{
        background-color: var(--primary) !important;
        color: var(--bg-main) !important;
    }}
    </style>
""", unsafe_allow_html=True)

# صورة في السايد بار
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="{img_src}" class="sidebar-img">
            <h3 style="margin-top: 10px; font-size: 1.2em;">Saif Aboseada</h3>
        </div>
    """, unsafe_allow_html=True)

# =========================================================
# 5. منطق تحميل الـ Resume
# =========================================================
resume_file_path = "resume.pdf"  # اسم الملف اللي هتحطه جنبه الكود
resume_data = None

if os.path.exists(resume_file_path):
    with open(resume_file_path, "rb") as f:
        resume_data = f.read()
else:
    # لو الملف مش موجود منعرضش زرار التحميل
    resume_data = None

# =========================================================
# 6. المحتوى الرئيسي
# =========================================================

if menu == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(f'<img class="profile-img" src="{img_src}">', unsafe_allow_html=True)

        st.markdown(f"""
            <div class="custom-card">
                <a href="#" class="icon-link"><i class="fa-solid fa-location-dot"></i> Port Said, Egypt</a>
                <a href="mailto:saif@example.com" class="icon-link"><i class="fa-solid fa-envelope"></i> saif@example.com</a>
                <a href="https://linkedin.com/in/YOUR_LINKEDIN" target="_blank" class="icon-link"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
                <a href="https://github.com/YOUR_GITHUB" target="_blank" class="icon-link"><i class="fa-brands fa-github"></i> GitHub</a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <h1 style="font-size: 3em; margin-bottom: 0;">Saif Aboseada</h1>
            <h3 style="color: {primary_color} !important; margin-top: 0;">Senior .NET Backend Developer</h3>
            <p style="font-size: 1.2em; margin-top: 20px; max-width: 650px;">
                Computer Science graduate specializing in building robust, scalable <b>RESTful APIs</b> 
                and high-performance backend systems using <b>ASP.NET Core</b>.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # --- قسم المهارات (Tech Stack) ---
        st.subheader("🛠️ Technical Stack")


        def tech_badge_group(title, skills):
            badges_html = "".join([f'<div class="skill-chip">{s}</div>' for s in skills])
            st.markdown(
                f"""<div style="margin-bottom: 15px;"><strong style="color: {primary_color};">{title}</strong><div class="skill-container">{badges_html}</div></div>""",
                unsafe_allow_html=True)


        tech_badge_group("Backend Core", ["C#", ".NET 8", "ASP.NET Core Web API", "MVC", "SignalR", "LINQ"])
        tech_badge_group("Data & Storage", ["SQL Server", "Entity Framework Core", "Redis", "PostgreSQL"])
        tech_badge_group("Architecture", ["Microservices", "Docker", "Clean Architecture", "CI/CD"])

        st.markdown("---")

        # --- أزرار التحميل والتواصل ---
        c1, c2 = st.columns([1, 4])
        with c1:
            if resume_data:
                st.download_button(
                    label="📄 Download CV",
                    data=resume_data,
                    file_name="Saif_Aboseada_Resume.pdf",
                    mime="application/pdf"
                )
            else:
                st.warning("Resume file not found.")

        with c2:
            st.link_button("✉️ Hire Me", "mailto:saif@example.com")


elif menu == "Experience":
    st.markdown("<h2><i class='fa-solid fa-briefcase'></i> Professional History</h2>", unsafe_allow_html=True)


    def job_card(role, company, date, tasks):
        task_items = "".join([f"<li style='margin-bottom:6px;'>{t}</li>" for t in tasks])
        return f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items:start;">
                <h3 style="color:{primary_color} !important; margin:0;">{role}</h3>
                <span style="background:rgba(255,255,255,0.1); padding:4px 10px; border-radius:15px; font-size:0.85em;">{date}</span>
            </div>
            <div style="font-weight:bold; margin-bottom:15px; opacity:0.9;"><i class="fa-solid fa-building"></i> {company}</div>
            <ul style="padding-left:20px; opacity:0.85;">{task_items}</ul>
        </div>
        """


    st.markdown(job_card(
        "Full-Stack .NET Trainer", "Digital Pioneers Initiative (DPI)", "Nov 2023 - Present",
        ["Mentored 50+ students in C# and .NET backend concepts.", "Designed curriculum for API development.",
         "Conducted code reviews."]
    ), unsafe_allow_html=True)

    st.markdown(job_card(
        "Freelance Backend Developer", "Remote / Upwork", "Jan 2023 - Present",
        ["Built scalable E-commerce APIs.", "Optimized legacy SQL queries.",
         "Integrated Payment Gateways (Stripe, PayPal)."]
    ), unsafe_allow_html=True)


elif menu == "Projects":
    st.markdown("<h2><i class='fa-solid fa-code'></i> Featured Projects</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)


    def project_card(title, desc, stack, link):
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
        st.markdown(
            project_card("E-Commerce API", "Full featured API with Basket, Ordering.", [".NET 8", "Redis", "Docker"],
                         "#"), unsafe_allow_html=True)
        st.markdown(
            project_card("Smart Recruitment", "AI-based CV filtering system.", ["Python", "Streamlit", "SQL"], "#"),
            unsafe_allow_html=True)

    with c2:
        st.markdown(project_card("Medical Booking", "Clinic management with concurrency control.",
                                 ["MVC", "SignalR", "Hangfire"], "#"), unsafe_allow_html=True)
        st.markdown(
            project_card("Auth Microservice", "Centralized Identity Server.", ["IdentityServer", "RabbitMQ"], "#"),
            unsafe_allow_html=True)


elif menu == "Services":
    st.markdown("<h2><i class='fa-solid fa-layer-group'></i> Services</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)


    def service_box(icon, title, desc):
        return f"""<div class="custom-card" style="text-align:center; height:100%;"><i class="{icon}" style="font-size:2.5em; margin-bottom:15px; color:{primary_color};"></i><h3 style="font-size:1.3em;">{title}</h3><p style="font-size:0.9em;">{desc}</p></div>"""


    with col1:
        st.markdown(service_box("fa-solid fa-server", "API Development", "Secure RESTful APIs."),
                    unsafe_allow_html=True)
    with col2:
        st.markdown(service_box("fa-solid fa-database", "Database Design", "Schema design & Tuning."),
                    unsafe_allow_html=True)
    with col3:
        st.markdown(service_box("fa-brands fa-docker", "Cloud & DevOps", "Deployment & Docker."),
                    unsafe_allow_html=True)


elif menu == "Contact":
    st.markdown("<h2><i class='fa-solid fa-paper-plane'></i> Get In Touch</h2>", unsafe_allow_html=True)
    with st.form("contact_form"):
        c1, c2 = st.columns(2)
        with c1: st.text_input("Name")
        with c2: st.text_input("Email")
        st.text_area("Message")
        st.form_submit_button("Send Message")