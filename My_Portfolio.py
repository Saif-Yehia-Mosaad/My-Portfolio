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
default_primary = "#D4AF37"
default_bg = "#0E1117"
default_card = "#161B22"
default_text = "#E6EDF3"

# قراءة المتغيرات
primary_color = default_primary
bg_color = default_bg
card_bg_color = default_card
text_color = default_text

# اسم الملف اللي هنحفظ الصورة فيه
PROFILE_IMAGE_PATH = "profile.jpg"

# =========================================================
# 3. القائمة الجانبية (ADMIN ONLY) - الحفظ الدائم
# =========================================================
with st.sidebar:
    st.markdown("### ⚙️ Settings")

    # القائمة المنسدلة للأدمن
    with st.expander("🔒 Admin Access"):
        admin_pass = st.text_input("Enter Admin Password", type="password")

        if admin_pass == "12345":  # <--- الباسورد
            st.success("Unlocked! ✅")
            st.markdown("---")

            st.markdown("#### 📸 Change Profile Photo")
            # رفع الصورة
            uploaded_file = st.file_uploader("Upload New Photo", type=['jpg', 'png', 'jpeg'])

            # --- التعديل السحري للحفظ ---
            if uploaded_file is not None:
                # 1. حفظ الملف على الهارد ديسك فوراً
                with open(PROFILE_IMAGE_PATH, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                st.success("Image Saved Permanently! 🎉")
                # 2. عمل ريفريش للصفحة عشان الصورة الجديدة تظهر
                st.rerun()

            st.markdown("---")
            st.markdown("#### 🎨 Theme Colors")
            primary_color = st.color_picker("Accent (Gold)", default_primary)
            bg_color = st.color_picker("Background", default_bg)
            card_bg_color = st.color_picker("Card BG", default_card)
            text_color = st.color_picker("Text Color", default_text)

        elif admin_pass != "":
            st.error("Wrong Password ❌")


# =========================================================
# 4. دالة قراءة الصورة (من الملف المحفوظ)
# =========================================================
def get_image_src(local_path):
    # دائماً بنحاول نقرأ من الملف المحفوظ على الجهاز
    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/jpg;base64,{encoded}"

    # لو مفيش ملف محفوظ، نعرض الأفاتار
    return "https://ui-avatars.com/api/?name=Saif+Aboseada&background=D4AF37&color=000&size=256"


# استدعاء الدالة
img_src = get_image_src(PROFILE_IMAGE_PATH)

# =========================================================
# 5. تنسيق CSS
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
    }}

    .stApp {{ background-color: var(--bg-main); font-family: 'Inter', sans-serif; }}

    /* Navbar Styling */
    div[data-testid="stRadio"] > div {{
        display: flex; justify-content: center; gap: 20px;
        background-color: var(--bg-card); padding: 10px; border-radius: 10px; border: 1px solid #30363D;
    }}
    div[role="radiogroup"] label > div:first-child {{ display: None; }}
    div[role="radiogroup"] label {{
        padding: 5px 15px; border-radius: 5px; transition: 0.3s; border: 1px solid transparent;
    }}
    div[role="radiogroup"] label:hover {{ border-color: var(--primary); color: var(--primary); }}
    div[role="radiogroup"] label[data-checked="true"] {{
        background-color: var(--primary) !important; color: #000 !important; font-weight: bold;
    }}

    /* Card Styling */
    .custom-card {{
        background-color: var(--bg-card); border: 1px solid #30363D; border-radius: 8px; padding: 24px; margin-bottom: 20px; transition: transform 0.2s;
    }}
    .custom-card:hover {{ border-color: var(--primary); transform: translateY(-3px); }}
    .card-title {{ color: var(--text-main); font-weight: 700; font-size: 1.1em; margin-bottom: 5px; }}
    .card-subtitle {{ color: var(--primary); font-size: 0.9em; font-weight: 600; margin-bottom: 10px; }}

    /* Badges */
    .skill-badge {{
        background-color: transparent; border: 1px solid #30363D; color: var(--text-main);
        padding: 6px 14px; border-radius: 4px; font-size: 0.85em; display: inline-block; margin: 4px;
    }}

    /* Typography */
    h1, h2, h3 {{ color: var(--text-main) !important; }}
    .section-header {{ border-bottom: 2px solid #30363D; padding-bottom: 10px; margin-bottom: 25px; margin-top: 10px; color: var(--primary); }}

    /* Nav Logo */
    .nav-logo {{ width: 50px; height: 50px; border-radius: 50%; border: 2px solid {primary_color}; object-fit: cover; }}

    /* Contact Form */
    div[data-testid="stForm"] {{ background-color: var(--bg-card); border: 1px solid #30363D; padding: 20px; border-radius: 10px; }}
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 6. الناف بار العلوية
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

# =========================================================
# 7. المحتوى الرئيسي
# =========================================================

if selected_page == "Profile":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
            <img src="{img_src}" style="width:220px; height:220px; border-radius:50%; border:4px solid {primary_color}; display:block; margin:0 auto;">
        """, unsafe_allow_html=True)
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
        """Passionate .NET Backend Developer and Computer Science student with specialized expertise in building scalable Web APIs using **ASP.NET Core** and **SQL Server**. Proficient in implementing **Clean Architecture**, **Repository Pattern**, and securing RESTful services.""")

elif selected_page == "Experience":
    st.markdown("<h2 class='section-header'>Professional Experience</h2>", unsafe_allow_html=True)


    def job_card(role, company, date, tasks):
        task_html = "".join([f"<li>{t}</li>" for t in tasks])
        return f"""<div class="custom-card"><div style="display:flex; justify-content:space-between;"><div><div class="card-title">{role}</div><div class="card-subtitle">{company}</div></div><div style="background:#21262d; padding:5px 10px; border-radius:5px; height:fit-content; font-size:0.85em;">{date}</div></div><ul style="padding-left:20px; color:#C9D1D9;">{task_html}</ul></div>"""


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
        return f"""<div class="custom-card"><div style="display:flex; justify-content:space-between;"><div class="card-title">{title}</div><span style="border:1px solid {primary_color}; color:{primary_color}; font-size:0.7em; padding:2px 6px; border-radius:4px; height:fit-content;">{type_tag}</span></div><ul style="padding-left:15px; font-size:0.95em; color:#8B949E; margin-top:10px;">{items_html}</ul><div style="margin-top:15px; border-top:1px solid #30363D; padding-top:10px;">{tags}</div></div>"""


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