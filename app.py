import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="ท่องระบบสุริยะ",
    page_icon="🪐",
    layout="wide"
)

# ตกแต่ง CSS เพิ่มความสวยงามสไตล์อวกาศ
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to bottom, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .planet-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .metric-title {
        font-size: 1.1rem;
        color: #00d2ff;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ข้อมูลดาวเคราะห์ (เปลี่ยนมาใช้ลิงก์ตรงและปลอดภัยสำหรับแสดงผลเว็บ)
planets = {
    "ดาวพุธ (Mercury)": {
        "icon": "☿️",
        "type": "ดาวเคราะห์หิน",
        "distance": "ประมาณ 77 ล้านกิโลเมตร (0.52 AU)",
        "size": "4,879 กม. (0.38 เท่าของโลก)",
        "gravity": 0.38,
        "desc": "ดาวเคราะห์ที่อยู่ใกล้ดวงอาทิตย์ที่สุดและมีขนาดเล็กที่สุดในระบบสุริยะ",
        "fun_fact": "พื้นผิวมีหลุมอุกกาบาตคล้ายดวงจันทร์ และมีอุณหภูมิร้อนจัดสลับหนาวจัด",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Mercury_in_color_-_Prockter07_centered.jpg/600px-Mercury_in_color_-_Prockter07_centered.jpg"
    },
    "ดาวศุกร์ (Venus)": {
        "icon": "♀️",
        "type": "ดาวเคราะห์หิน",
        "distance": "ประมาณ 41 ล้านกิโลเมตร (0.28 AU)",
        "size": "12,104 กม. (0.95 เท่าของโลก)",
        "gravity": 0.91,
        "desc": "ดาวเคราะห์ที่มีขนาดใกล้เคียงกับโลกมากที่สุด แต่ร้อนที่สุดในระบบสุริยะ",
        "fun_fact": "หมุนรอบตัวเองกลับทิศทางกับดาวเคราะห์ส่วนใหญ่ และมีชั้นบรรยากาศหนาทึบ",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Venus-real_color.jpg/600px-Venus-real_color.jpg"
    },
    "ดาวอังคาร (Mars)": {
        "icon": "♂️",
        "type": "ดาวเคราะห์หิน",
        "distance": "ประมาณ 78 ล้านกิโลเมตร (0.52 AU)",
        "size": "6,779 กม. (0.53 เท่าของโลก)",
        "gravity": 0.38,
        "desc": "ดาวเคราะห์แดงที่เป็นเป้าหมายสำคัญในการสำรวจสิ่งมีชีวิตนอกโลก",
        "fun_fact": "มีภูเขาไฟที่สูงที่สุดในระบบสุริยะชื่อ โอลิมปัส มอนส์",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/600px-OSIRIS_Mars_true_color.jpg"
    },
    "ดาวพฤหัสบดี (Jupiter)": {
        "icon": "♃",
        "type": "ดาวเคราะห์แก๊สยักษ์",
        "distance": "ประมาณ 628 ล้านกิโลเมตร (4.20 AU)",
        "size": "139,820 กม. (11 เท่าของโลก)",
        "gravity": 2.34,
        "desc": "ดาวเคราะห์ที่ใหญ่ที่สุดในระบบสุริยะของเรา",
        "fun_fact": "มีจุดแดงใหญ่ (Great Red Spot) ซึ่งเป็นพายุหมุนยักษ์ที่มีขนาดใหญ่กว่าโลก",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg/600px-Jupiter_and_its_shrunken_Great_Red_Spot.jpg"
    },
    "ดาวเสาร์ (Saturn)": {
        "icon": "♄",
        "type": "ดาวเคราะห์แก๊สยักษ์",
        "distance": "ประมาณ 1,277 ล้านกิโลเมตร (8.53 AU)",
        "size": "116,460 กม. (9 เท่าของโลก)",
        "gravity": 1.06,
        "desc": "โดดเด่นด้วยวงแหวนน้ำแข็งขนาดใหญ่ที่สวยงามและสังเกตเห็นได้ชัดเจน",
        "fun_fact": "มีความหนาแน่นน้อยกว่าน้ำ ถ้ามีอ่างน้ำขนาดใหญ่พอก็จะลอยน้ำได้",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox_-_Flickr_-_NASA_Goddard_Photo_and_Video.jpg/600px-Saturn_during_Equinox_-_Flickr_-_NASA_Goddard_Photo_and_Video.jpg"
    },
    "ดาวยูเรนัส (Uranus)": {
        "icon": "♅",
        "type": "ดาวเคราะห์น้ำแข็งยักษ์",
        "distance": "ประมาณ 2,720 ล้านกิโลเมตร (18.18 AU)",
        "size": "50,724 กม. (4 เท่าของโลก)",
        "gravity": 0.92,
        "desc": "ดาวเคราะห์สีฟ้าอมเขียวที่มีแกนเอียงราบเกือบขนานกับวงโคจร",
        "fun_fact": "หมุนรอบตัวเองในลักษณะ 'นอนกลิ้ง' ไปบนวงโคจร",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Uranus2.jpg/600px-Uranus2.jpg"
    },
    "ดาวเนปจูน (Neptune)": {
        "icon": "♆",
        "type": "ดาวเคราะห์น้ำแข็งยักษ์",
        "distance": "ประมาณ 4,351 ล้านกิโลเมตร (29.07 AU)",
        "size": "49,244 กม. (3.8 เท่าของโลก)",
        "gravity": 1.19,
        "desc": "ดาวเคราะห์สีน้ำเงินเข้มที่อยู่ไกลจากดวงอาทิตย์ที่สุดในระบบสุริยะ",
        "fun_fact": "มีกระแสลมที่รุนแรงและเร็วที่สุดในระบบสุริยะ",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Neptune_Full_-_Voyager_2_%2829347980848%29_%28cropped%29.jpg/600px-Neptune_Full_-_Voyager_2_%2829347980848%29_%28cropped%29.jpg"
    }
}

# Sidebar สำหรับฟีเจอร์คำนวณน้ำหนัก
st.sidebar.header("⚖️ เครื่องคำนวณน้ำหนักนอกโลก")
user_weight = st.sidebar.number_input("ใส่น้ำหนักของคุณบนโลก (กิโลกรัม):", min_value=1.0, max_value=300.0, value=60.0)
st.sidebar.write("น้ำหนักของคุณบนดาวดวงอื่น ๆ:")
for planet_name, info in planets.items():
    calculated_weight = user_weight * info["gravity"]
    st.sidebar.text(f"{planet_name.split(' ')[0]}: {calculated_weight:.1f} กก.")

# ส่วนหัวของเว็บไซต์
st.title("🌌 สำรวจระบบสุริยะของเรา")
st.write("เรียนรู้ระยะห่าง ขนาดเปรียบเทียบ และชมภาพถ่ายของดาวเคราะห์แต่ละดวงกับ **โลก** กันเถอะ!")
st.divider()

# แถบคลิกเลือกดาวเคราะห์หลัก
selected_planet = st.selectbox("🪐 เลือกดาวเคราะห์ที่คุณต้องการสำรวจ:", list(planets.keys()))

# จัดหน้าจอแสดงผลข้อมูลคู่กับรูปภาพ
p_data = planets[selected_planet]
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown(f"""
        <div class="planet-card">
            <h2>{p_data['icon']} {selected_planet}</h2>
            <p><i>{p_data['desc']}</i></p>
            <hr style="border-color: rgba(255,255,255,0.2);">
            <p class="metric-title">📏 ระยะห่างจากโลก (โดยเฉลี่ย):</p>
            <p>{p_data['distance']}</p>
            <p class="metric-title">📐 ขนาดเส้นผ่านศูนย์กลาง:</p>
            <p>{p_data['size']}</p>
            <p class="metric-title">✨ เกร็ดความรู้:</p>
            <p>{p_data['fun_fact']}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(p_data["image"], caption=f"ภาพถ่าย {selected_planet}", use_container_width=True)

# ส่วนเปรียบเทียบภาพรวมทั้งหมดในรูปตาราง
st.subheader("📊 ตารางเปรียบเทียบสรุปขนาดและระยะทางกับโลก")
df = pd.DataFrame([
    {
        "ดาวเคราะห์": k, 
        "ประเภท": v["type"], 
        "ขนาดเทียบกับโลก": v["size"].split("(")[1].replace(")", ""), 
        "ระยะห่างจากโลก": v["distance"].split("(")[0]
    }
    for k, v in planets.items()
])
st.table(df)
