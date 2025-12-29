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
default_primary = "#D4AF37"  # الذهبي
default_bg = "#0E1117"  # الخلفية الداكنة
default_card = "#161B22"  # لون الكروت
default_secondary = "#1F2937"  # لون ثانوي للتدرج
default_text = "#E6EDF3"
PROFILE_IMAGE_PATH = "profile.jpg"

# متغيرات التصميم
primary_color = default_primary
bg_color = default_bg
card_bg_color = default_card
secondary_card_color = default_secondary
text_color = default_text
design_mode = "Solid"  # الافتراضي

# =========================================================
# 3. لوحة الأدمن (ADMIN PANEL)
# =========================================================
with st.sidebar:
    st.markdown("### ⚙️ Settings")

    with st.expander("🔒 Admin Access"):
        admin_pass = st.text_input("Enter Admin Password", type="password")

        if admin_pass == "12345":
            st.success("Unlocked! ✅")
            st.markdown("---")

            # 1. رفع الصورة
            st.markdown("#### 📸 Profile Photo")
            uploaded_file = st.file_uploader("Upload Photo", type=['jpg', 'png', 'jpeg'])

            if uploaded_file is not None:
                with open(PROFILE_IMAGE_PATH, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success("Saved! Reloading...")
                st.rerun()

            st.markdown("---")

            # 2. إعدادات التصميم المتطورة
            st.markdown("#### 🎨 Design Style")

            # اختيار المود (عادي - تدرج - زجاجي)
            design_mode = st.radio("Card Style", ["Solid", "Gradient", "Glassy"])

            st.markdown("###### Colors")
            primary_color = st.color_picker("Accent (Gold)", default_primary)
            bg_color = st.color_picker("Page Background", default_bg)

            if design_mode == "Solid":
                card_bg_color = st.color_picker("Card Color", default_card)

            elif design_mode == "Gradient":
                col_g1, col_g2 = st.columns(2)
                with col_g1:
                    card_bg_color = st.color_picker("Start Color", default_card)
                with col_g2:
                    secondary_card_color = st.color_picker("End Color", default_secondary)

            elif design_mode == "Glassy":
                st.info("Glassy mode uses transparency & blur automatically.")
                # في الوضع الزجاجي نستخدم شفافية ثابتة
                card_bg_color = "rgba(255, 255, 255, 0.05)"

            text_color = st.color_picker("Text Color", default_text)

        elif admin_pass != "":
            st.error("Wrong Password ❌")

# =========================================================
# 4. منطق CSS المتقدم (Dynamic CSS)
# =========================================================

# تحديد كود الخلفية للكروت بناءً على اختيارك
if design_mode == "Solid":
    card_css = f"background-color: {card_bg_color}; border: 1px solid #30363D;"
elif design_mode == "Gradient":
    card_css = f"background: linear-gradient(135deg, {card_bg_color}, {secondary_card_color}); border: 1px solid #30363D;"
elif design_mode == "Glassy":
    card_css = f"""
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    """

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
            unsafe_allow_html=True)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    :root {{
        --primary: {primary_color};
        --bg-main: {bg_color};
        --text-main: {text_color};
    }}

    .stApp {{ background-color: var(--bg-main); font-family: 'Inter', sans-serif; }}

    /* Navbar Styling */
    div[data-testid="stRadio"] > div {{
        display: flex; justify-content: center; gap: 20px;
        {card_css} /* تطبيق نفس ستايل الكروت على الناف بار */
        padding: 10px; border-radius: 15px; 
    }}
    div[role="radiogroup"] label > div:first-child {{ display: None; }}
    div[role="radiogroup"] label {{
        padding: 5px 15px; border-radius: 8px; transition: 0.3s; border: 1px solid transparent;
    }}
    div[role="radiogroup"] label:hover {{ border-color: var(--primary); color: var(--primary); }}
    div[role="radiogroup"] label[data-checked="true"] {{
        background-color: var(--primary) !important; color: #000 !important; font-weight: bold;
        box-shadow: 0 0 10px {primary_color};
    }}

    /* --- Card Styling (The Magic Part) --- */
    .custom-card {{
        {card_css}
        border-radius: 12px; 
        padding: 24px; 
        margin-bottom: 20px; 
        transition: transform 0.3s, box-shadow 0.3s;
    }}
    .custom-card:hover {{ 
        border-color: var(--primary); 
        transform: translateY(-5px); 
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }}

    /* Typography */
    .card-title {{ color: var(--text-main); font-weight: 700; font-size: 1.1em; margin-bottom: 5px; }}
    .card-subtitle {{ color: var(--primary); font-size: 0.9em; font-weight: 600; margin-bottom: 10px; }}
    h1, h2, h3 {{ color: var(--text-main) !important; }}
    .section-header {{ border-bottom: 2px solid #30363D; padding-bottom: 10px; margin-bottom: 25px; margin-top: 10px; color: var(--primary); }}

    /* Badges */
    .skill-badge {{
        background: rgba(255,255,255,0.05); border: 1px solid #30363D; color: var(--text-main);
        padding: 6px 14px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin: 4px;
    }}

    /* --- Image Styling (Perfect Circle Fix) --- */
    .nav-logo {{ 
        width: 50px; height: 50px; border-radius: 50%; 
        border: 2px solid {primary_color}; object-fit: cover; aspect-ratio: 1/1; 
    }}

    .profile-hero-img {{
        width: 220px; 
        height: 220px; 
        border-radius: 50%; 
        border: 4px solid {primary_color}; 
        object-fit: cover;      /* يضمن ملء الصورة للدائرة */
        object-position: center top; /* تركيز الصورة على الوجه */
        aspect-ratio: 1/1;      /* يضمن أن الطول يساوي العرض تماماً */
        display: block; 
        margin: 0 auto;
        box-shadow: 0 0 25px {primary_color}40; /* وهج خفيف */
    }}

    .sidebar-img {{
        width: 120px; height: 120px; border-radius: 50%; 
        border: 3px solid {primary_color}; object-fit: cover; aspect-ratio: 1/1;
        display: block; margin: 0 auto;
    }}

    /* Contact Form */
    div[data-testid="stForm"] {{ {card_css} padding: 20px; border-radius: 12px; }}
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
    return "https://ui-avatars.com/api/?name=Saif+Aboseada&background=D4AF37&color=000&size=256"


img_src = get_image_src(PROFILE_IMAGE_PATH)

# =========================================================
# 6. الهيكل العام (Navbar & Sidebar)
# =========================================================
col_logo, col_nav = st.columns([1, 8])
with col_logo:
    st.markdown(f'<img src="{img_src}" class="nav-logo">', unsafe_allow_html=True)

with col_nav:
    selected_page = st.radio(
        "Menu",
        ["Profile", "Experience", "Projects", "Skills", "Education", "Contact"],
        horizontal=True,
        label_visibility="collapsed"
    )

st.markdown("---")

# السايد بار (صورة واسم فقط - الأدمن مخفي)
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{img_src}" class="sidebar-img">
            <h3 style="margin-top:10px; color:{text_color}; font-size:1.2em;">Saif Aboseada</h3>
        </div>
    """, unsafe_allow_html=True)

# =========================================================
# 7. المحتوى الرئيسي
# =========================================================

if selected_page == "Profile":
    col1, col2 = st.columns([1, 2])
    with col1:
        # هنا الصورة الكبيرة في البروفايل
        st.markdown(f'<img src="{img_src}" class="profile-hero-img">', unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <h1 style="font-size: 3.5em; margin-bottom: 0;">SAIF ABOSEADA</h1>
            <h3 style="color: {primary_color} !important; margin-top: 0;">.NET Backend Developer</h3>
            <p style="color: #8B949E; font-size: 1.1em; margin-top: 15px;">
                <i class="fa-solid fa-location-dot" style="color:{primary_color}"></i> Port Said, Egypt
            </p>
            <div style="margin-top: 25px;">
                <a href="https://linkedin.com/in/saif-yehia" target="_blank" style="background:{primary_color}; color:#000; padding:10px 20px; border-radius:5px; font-weight:bold; margin-right:15px; text-decoration:none;"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
                <a href="https://github.com/Saif-Yehia-Mosaad" target="_blank" style="border:1px solid {primary_color}; color:{primary_color}; padding:10px 20px; border-radius:5px; font-weight:bold; text-decoration:none;"><i class="fa-brands fa-github"></i> GitHub</a>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-header'>Professional Summary</h3>", unsafe_allow_html=True)
    st.markdown(
        """Backend.NET Developer with 2 years of experience building and maintaining web applications. Proficient in C#, .NET Core, MVC, and Web API development. Strong foundation in SQL Server and creating responsive front-end interfaces using HTML5, CSS3, and JavaScript. Experienced with Git/GitHub, unit testing, and Dockerand professional in use Microsoft office(Excel , Word, Power Point ).""")

elif selected_page == "Experience":
    st.markdown("<h2 class='section-header'>Professional Experience</h2>", unsafe_allow_html=True)


    def job_card(role, company, date, tasks):
        task_html = "".join([f"<li>{t}</li>" for t in tasks])
        return f"""<div class="custom-card"><div style="display:flex; justify-content:space-between;"><div><div class="card-title">{role}</div><div class="card-subtitle">{company}</div></div><div style="background:rgba(255,255,255,0.1); padding:5px 10px; border-radius:5px; height:fit-content; font-size:0.85em;">{date}</div></div><ul style="padding-left:20px; color:#C9D1D9;">{task_html}</ul></div>"""


    st.markdown(job_card("Full Stack .NET Development Trainee", "Digital Egypt Pioneers Initiative (DEPI)",
                         "Nov 2025 - Present", ["Specialized in Backend Development using ASP.NET Core and SQL Server.",
                                                "Collaborated with a team to design database schemas.",
                                                "Mastered version control workflows using Git and GitHub."]),
                unsafe_allow_html=True)

elif selected_page == "Projects":
    st.markdown("<h2 class='section-header'>Technical Projects</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)


    def proj(title, type_tag, items, stack):
        items_html = "".join([f"<li>{i}</li>" for i in items])
        tags = "".join([f"<span class='skill-badge'>{s}</span>" for s in stack])
        return f"""<div class="custom-card"><div style="display:flex; justify-content:space-between;"><div class="card-title">{title}</div><span style="border:1px solid {primary_color}; color:{primary_color}; font-size:0.7em; padding:2px 6px; border-radius:4px; height:fit-content;">{type_tag}</span></div><ul style="padding-left:15px; font-size:0.95em; color:#8B949E; margin-top:10px;">{items_html}</ul><div style="margin-top:15px; border-top:1px solid rgba(255,255,255,0.1); padding-top:10px;">{tags}</div></div>"""


    with c1:
        st.markdown(proj("E-Commerce RESTful API", "Backend",
                         ["Developed API using ASP.NET Core & SQL Server.", "Implemented Repository Pattern."],
                         ["ASP.NET Core", "SQL Server", "Clean Arch"]), unsafe_allow_html=True)
        st.markdown(proj("Daily Quotes Application", "Full Stack",
                         ["RESTful API serving dynamic content.", "Integrated with Flutter mobile app."],
                         ["ASP.NET Core", "API", "Mobile"]), unsafe_allow_html=True)
    with c2:
        st.markdown(proj("Medical Clinic Booking System", "Backend",
                         ["Booking system with concurrency control.", "Secured API using JWT & RBAC."],
                         ["Web API", "JWT", "Security"]), unsafe_allow_html=True)
        st.markdown(proj("Auth & Authorization Service", "Microservice",
                         ["Dedicated identity service using ASP.NET Identity.", "Implemented JWT tokens."],
                         ["Identity", "Microservices"]), unsafe_allow_html=True)

elif selected_page == "Skills":
    st.markdown("<h2 class='section-header'>Technical Skills</h2>", unsafe_allow_html=True)


    def skill_group(title, icon, skills):
        badges = "".join([f"<span class='skill-badge'>{s}</span>" for s in skills])
        st.markdown(
            f"""<div style="margin-bottom:20px;"><h4 style="color:{text_color}"><i class="{icon}" style="color:{primary_color}; margin-right:10px;"></i> {title}</h4><div>{badges}</div></div>""",
            unsafe_allow_html=True)


    skill_group("Core Technologies", "fa-solid fa-code",
                ["C#", ".NET 6/7/8", "ASP.NET Core Web API", "LINQ", "EF Core"])
    skill_group("Database", "fa-solid fa-database", ["SQL Server", "T-SQL", "Database Design"])
    skill_group("Architecture", "fa-solid fa-sitemap",
                ["MVC", "RESTful APIs", "Repository Pattern", "Unit of Work", "DI"])
    skill_group("Tools & DevOps", "fa-solid fa-wrench", ["Git", "GitHub", "Postman", "Swagger", "Docker (Basics)"])

elif selected_page == "Education":
    st.markdown("<h2 class='section-header'>Education & Certifications</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"""<div class="custom-card"><div class="card-title"><i class="fa-solid fa-graduation-cap" style="color:{primary_color}"></i> Bachelor of Computer Science</div><div class="card-subtitle">Suez Canal University</div><div style="font-size:0.9em;">Oct 2022 - Present</div></div>""",
            unsafe_allow_html=True)
    with c2:
        st.markdown(
            f"""<div class="custom-card"><div class="card-title"><i class="fa-solid fa-certificate" style="color:{primary_color}"></i> Certifications</div><ul style="padding-left:20px; color:#8B949E;"><li>.NET Web Development</li><li>Frontend Web Development</li><li>AI for Beginners</li></ul></div>""",
            unsafe_allow_html=True)

elif selected_page == "Contact":
    st.markdown("<h2 class='section-header'>Get In Touch</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("### Send me a message")
        with st.form("contact_form"):
            st.text_input("Your Name")
            st.text_input("Your Email")
            st.text_area("Message")
            if st.form_submit_button("Send Message"): st.success("Message Sent!")
    with c2:
        st.markdown("### Contact Info")
        st.markdown(
            f"""<div class="custom-card"><div style="margin-bottom:15px;"><i class="fa-solid fa-envelope" style="color:{primary_color};"></i> <a href="mailto:saifyehia58@gmail.com">saifyehia58@gmail.com</a></div><div style="margin-bottom:15px;"><i class="fa-solid fa-phone" style="color:{primary_color};"></i> +20 127-851-3846</div></div>""",
            unsafe_allow_html=True)