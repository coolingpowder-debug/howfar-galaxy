import streamlit as st
import pandas as pd
import random

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
    .game-container {
        background-color: rgba(255, 255, 255, 0.95);
        border: 2px solid #4a0e4e;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 25px;
        color: #240046;
    }
    .shadow-box {
        background-color: #1a1a2e;
        border: 3px dashed #00d2ff;
        text-align: center;
        padding: 30px;
        border-radius: 12px;
        font-size: 5rem;
        color: #ffffff;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ข้อมูลดาวเคราะห์พร้อมไอคอนเงา ตัวอักษรภาษาอังกฤษตัวแรก และคำใบ้
planets = {
    "ดาวพุธ (Mercury)": {
        "icon": "☿️",
        "type": "ดาวเคราะห์หิน",
        "distance": "ประมาณ 77 ล้านกิโลเมตร (0.52 AU)",
        "size": "4,879 กม. (0.38 เท่าของโลก)",
        "gravity": 0.38,
        "desc": "ดาวเคราะห์ที่อยู่ใกล้ดวงอาทิตย์ที่สุดและมีขนาดเล็กที่สุดในระบบสุริยะ",
        "fun_fact": "พื้นผิวมีหลุมอุกกาบาตคล้ายดวงจันทร์ และมีอุณหภูมิร้อนจัดสลับหนาวจัด",
        "image": "https://images-assets.nasa.gov/image/PIA16847/PIA16847~orig.jpg",
        "bar": "🌍---🪐 (ใกล้กว่าโลก)",
        "clue": "ฉันอยู่ใกล้ดวงอาทิตย์ที่สุด มีขนาดเล็กจิ๋ว และพื้นผิวเต็มไปด้วยหลุมอุกกาบาตคล้ายดวงจันทร์!",
        "first_letter": "M"
    },
    "ดาวศุกร์ (Venus)": {
        "icon": "♀️",
        "type": "ดาวเคราะห์หิน",
        "distance": "ประมาณ 41 ล้านกิโลเมตร (0.28 AU)",
        "size": "12,104 กม. (0.95 เท่าของโลก)",
        "gravity": 0.91,
        "desc": "ดาวเคราะห์ที่มีขนาดใกล้เคียงกับโลกมากที่สุด แต่ร้อนที่สุดในระบบสุริยะ",
        "fun_fact": "หมุนรอบตัวเองกลับทิศทางกับดาวเคราะห์ส่วนใหญ่ และมีชั้นบรรยากาศหนาทึบ",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg",
        "bar": "🌍---🪐 (ใกล้กว่ามาก)",
        "clue": "ฉันมีขนาดใกล้เคียงกับโลกมากที่สุด แต่กลับร้อนระอุที่สุดในระบบสุริยะแถมยังหมุนกลับทิศทาง!",
        "first_letter": "V"
    },
    "ดาวอังคาร (Mars)": {
        "icon": "♂️",
        "type": "ดาวเคราะห์หิน",
        "distance": "ประมาณ 78 ล้านกิโลเมตร (0.52 AU)",
        "size": "6,779 กม. (0.53 เท่าของโลก)",
        "gravity": 0.38,
        "desc": "ดาวเคราะห์แดงที่เป็นเป้าหมายสำคัญในการสำรวจสิ่งมีชีวิตนอกโลก",
        "fun_fact": "มีภูเขาไฟที่สูงที่สุดในระบบสุริยะชื่อ โอลิมปัส มอนส์",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",
        "bar": "🌍-----🪐",
        "clue": "ฉันคือดาวเคราะห์สีแดง มีภูเขาไฟที่สูงที่สุดในระบบสุริยะ และนักวิทยาศาสตร์กำลังสนใจไปตั้งถิ่นฐาน!",
        "first_letter": "M"
    },
    "ดาวพฤหัสบดี (Jupiter)": {
        "icon": "♃",
        "type": "ดาวเคราะห์แก๊สยักษ์",
        "distance": "ประมาณ 628 ล้านกิโลเมตร (4.20 AU)",
        "size": "139,820 กม. (11 เท่าของโลก)",
        "gravity": 2.34,
        "desc": "ดาวเคราะห์ที่ใหญ่ที่สุดในระบบสุริยะของเรา",
        "fun_fact": "มีจุดแดงใหญ่ (Great Red Spot) ซึ่งเป็นพายุหมุนยักษ์ที่มีขนาดใหญ่กว่าโลก",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg",
        "bar": "🌍------------🪐",
        "clue": "ฉันคือพี่ใหญ่แห่งระบบสุริยะ เป็นดาวเคราะห์แก๊สยักษ์ที่มีพายุจุดแดงใหญ่หมุนวนอยู่!",
        "first_letter": "J"
    },
    "ดาวเสาร์ (Saturn)": {
        "icon": "♄",
        "type": "ดาวเคราะห์แก๊สยักษ์",
        "distance": "ประมาณ 1,277 ล้านกิโลเมตร (8.53 AU)",
        "size": "116,460 กม. (9 เท่าของโลก)",
        "gravity": 1.06,
        "desc": "โดดเด่นด้วยวงแหวนน้ำแข็งขนาดใหญ่ที่สวยงามและสังเกตเห็นได้ชัดเจน",
        "fun_fact": "มีความหนาแน่นน้อยกว่าน้ำ ถ้ามีอ่างน้ำขนาดใหญ่พอก็จะลอยน้ำได้",
        "image": "https://images-assets.nasa.gov/image/PIA01384/PIA01384~orig.jpg",
        "bar": "🌍-----------------🪐",
        "clue": "ฉันโดดเด่นไม่เหมือนใครเพราะมีวงแหวนน้ำแข็งล้อมรอบสวยงาม และมีความหนาแน่นน้อยจนลอยน้ำได้!",
        "first_letter": "S"
    },
    "ดาวยูเรนัส (Uranus)": {
        "icon": "♅",
        "type": "ดาวเคราะห์น้ำแข็งยักษ์",
        "distance": "ประมาณ 2,720 ล้านกิโลเมตร (18.18 AU)",
        "size": "50,724 กม. (4 เท่าของโลก)",
        "gravity": 0.92,
        "desc": "ดาวเคราะห์สีฟ้าอมเขียวที่มีแกนเอียงราบเกือบขนานกับวงโคจร",
        "fun_fact": "หมุนรอบตัวเองในลักษณะ 'นอนกลิ้ง' ไปบนวงโคจร",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",
        "bar": "🌍------------------------------🪐",
        "clue": "ฉันเป็นดาวเคราะห์สีฟ้าอมเขียวที่แปลกประหลาด เพราะหมุนรอบตัวเองในลักษณะ 'นอนกลิ้ง'!",
        "first_letter": "U"
    },
    "ดาวเนปจูน (Neptune)": {
        "icon": "♆",
        "type": "ดาวเคราะห์น้ำแข็งยักษ์",
        "distance": "ประมาณ 4,351 ล้านกิโลเมตร (29.07 AU)",
        "size": "49,244 กม. (3.8 เท่าของโลก)",
        "gravity": 1.19,
        "desc": "ดาวเคราะห์สีน้ำเงินเข้มที่อยู่ไกลจากดวงอาทิตย์ที่สุดในระบบสุริยะ",
        "fun_fact": "มีกระแสลมที่รุนแรงและเร็วที่สุดในระบบสุริยะ",
        "image": "https://images-assets.nasa.gov/image/PIA01492/PIA01492~orig.jpg",
        "bar": "🌍----------------------------------------🪐",
        "clue": "ฉันเป็นดาวเคราะห์สีน้ำเงินเข้มที่อยู่ไกลสุดขอบระบบสุริยะ และมีกระแสลมที่รุนแรงที่สุด!",
        "first_letter": "N"
    }
}

# Sidebar สำหรับเครื่องมือคำนวณ
st.sidebar.header("🛠️ เครื่องมือจำลองอวกาศ")

st.sidebar.subheader("⚖️ คำนวณน้ำหนักนอกโลก")
user_weight = st.sidebar.number_input("น้ำหนักของคุณบนโลก (กก.):", min_value=1.0, max_value=300.0, value=60.0)
for planet_name, info in planets.items():
    calc_weight = user_weight * info["gravity"]
    st.sidebar.text(f"{planet_name.split(' ')[0]}: {calc_weight:.1f} กก.")

st.sidebar.divider()

st.sidebar.subheader("🦘 วัดความสูงการกระโดด")
jump_earth = st.sidebar.number_input("ปกติคุณกระโดดบนโลกสูง (ซม.):", min_value=5.0, max_value=200.0, value=40.0)

# ส่วนหัวของเว็บไซต์
st.title("🌌 สำรวจระบบสุริยะของเรา")
st.write("เรียนรู้ระยะห่าง ขนาดเปรียบเทียบ และชมภาพถ่ายของดาวเคราะห์แต่ละดวงกับ **โลก** กันเถอะ!")
st.divider()

# --- ส่วนมินิเกมทายเงาดาวเคราะห์ ---
st.subheader("🎮 มินิเกม: ทายเงาดาวเคราะห์ปริศนา")

if "game_planet" not in st.session_state:
    st.session_state["game_planet"] = random.choice(list(planets.keys()))

target_planet = st.session_state["game_planet"]
target_data = planets[target_planet]

st.markdown(f"""
    <div class="game-container">
        <h3 style="margin-top: 0; color: #240046;">🌑 ปริศนาเงาดาวเคราะห์</h3>
        <hr style="border-color: rgba(36,0,70,0.2);">
    </div>
""", unsafe_allow_html=True)

col_shadow, col_clue = st.columns([1, 2])

with col_shadow:
    # ใช้กล่องเงาไอคอนแสดงแทนเพื่อความเสถียร 100%
    st.markdown(f'<div class="shadow-box">🪐</div>', unsafe_allow_html=True)

with col_clue:
    st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; border: 1px solid #ddd; height: 100%;">
            <p style="color: #240046; font-size: 1.1rem; margin-top: 0;"><b>🔍 คำใบ้:</b> {target_data['clue']}</p>
            <p style="color: #d90429; font-size: 1.05rem; margin-bottom: 0;"><b>🔤 ตัวอักษรภาษาอังกฤษตัวแรก:</b> {target_data['first_letter']}</p>
        </div>
    """, unsafe_allow_html=True)

col_game1, col_game2, col_game3 = st.columns([2, 1, 1])

with col_game1:
    user_guess = st.selectbox("เลือกคำตอบของคุณ:", ["--- กรุณาเลือกดาวเคราะห์ ---"] + list(planets.keys()), key="guess_box")

with col_game2:
    st.write("") 
    st.write("")
    if st.button("🎯 ตรวจคำตอบ"):
        if user_guess == "--- กรุณาเลือกดาวเคราะห์ ---":
            st.warning("⚠️ โปรดเลือกคำตอบก่อนกดตรวจครับ!")
        elif user_guess == target_planet:
            st.success(f"🎉 ถูกต้องนะคร้าบ! นี่คือ {target_planet} เก่งมาก!")
        else:
            st.error(f"❌ ยังไม่ถูก ลองใหม่อีกครั้ง!")

with col_game3:
    st.write("")
    st.write("")
    if st.button("🔄 เปลี่ยนคำถาม"):
        st.session_state["game_planet"] = random.choice(list(planets.keys()))
        st.rerun()

st.divider()

# แถบคลิกเลือกดาวเคราะห์หลักเพื่อศึกษาข้อมูล
selected_planet = st.selectbox("🪐 เลือกดาวเคราะห์ที่คุณต้องการสำรวจ:", list(planets.keys()))

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

# ส่วนกราฟิกเปรียบเทียบความสูงการกระโดด
st.subheader("📊 กราฟิกเปรียบเทียบความสูงในการกระโดดแต่ละดาวเคราะห์")
st.write(f"อ้างอิงจากความสูงที่คุณกระโดดบนโลกได้ **{jump_earth} ซม.**")

jump_data = []
for planet_name, info in planets.items():
    h_val = round(jump_earth / info["gravity"], 1)
    short_name = planet_name.split(" ")[0]
    jump_data.append({"ดาวเคราะห์": short_name, "ความสูง (ซม.)": h_val})

df_jump = pd.DataFrame(jump_data).set_index("ดาวเคราะห์")
st.bar_chart(df_jump)

# ส่วนเปรียบเทียบภาพรวมทั้งหมดในรูปตาราง
st.subheader("📊 ตารางเปรียบเทียบสรุปขนาดและระยะทางกับโลก")
df_table = pd.DataFrame([
    {
        "ดาวเคราะห์": k, 
        "ประเภท": v["type"], 
        "ขนาดเทียบกับโลก": v["size"].split("(")[1].replace(")", ""), 
        "ระยะห่างจากโลก": v["distance"].split("(")[0],
        "แผนภาพระยะทางเทียบกับโลก": v["bar"]
    }
    for k, v in planets.items()
])
st.table(df_table)
