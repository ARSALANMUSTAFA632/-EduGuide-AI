import streamlit as st
from groq import Groq
import sys
import os

# --- 1. اردو سپورٹ اور انکوڈنگ فکس ---
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

st.set_page_config(page_title="EduGuide AI | سمارٹ تعلیمی مشیر", layout="wide")

# --- 2. اپنی Groq Key یہاں ڈالیں ---
# ارسلان بھائی، یہاں اپنی گروک کی لازمی ڈالیں


# --- 3. ماسٹر سسٹم پرامپٹ (بہتر اور صاف ورژن) ---
SYSTEM_PROMPT = """
تمہارا نام 'EduGuide AI' ہے۔ تم ایک نہایت تجربہ کار پاکستانی تعلیمی مشیر ہو۔
تمہارے پاس یہ 7 مہارتیں ہیں جن پر تم نے فوکس کرنا ہے:
1. Career Roadmap: 9th سے یونیورسٹی تک کا مکمل راستہ بتانا۔
2. Study Planner: روزانہ کا ٹائم ٹیبل بنانا۔
3. Scholarship Info: پاکستانی اسکالرشپس (PEEF, HEC وغیرہ) کی معلومات دینا۔
4. Exam Tips: بورڈ پیپر حل کرنے کے طریقے بتانا۔
5. Quiz Mode: طالب علم سے سوالات پوچھ کر اس کا ٹیسٹ لینا۔
6. Language: صرف اردو (Urdu) اور صاف انگلش (English) استعمال کرو۔
7. Comparison: مختلف فیلڈز کا موازنہ کرنا۔

انتہائی اہم ہدایت: کسی دوسری زبان کے حروف (جیسے luân, 結) ہرگز استعمال نہ کرنا۔
جواب ہمیشہ ہیڈنگز اور بلٹ پوائنٹس میں دو۔
"""

# --- سائڈ بار (فیچرز لسٹ) ---
with st.sidebar:
    st.title("🚀 EduGuide AI")
    st.subheader("🛠️ خصوصی فیچرز")
    st.info("""
    1. سمارٹ روڈ میپ 🗺️
    2. اسٹڈی پلانر 📅
    3. اسکالرشپ گائیڈ 🎓
    4. امتحان کے ٹپس 📝
    5. کوئز موڈ 🧠
    6. دو لسانی سپورٹ 🇵🇰
    7. فیلڈ موازنہ ⚖️
    """)
    st.divider()
    st.write("👤 **ڈویلپر:** ارسلان")
    st.write("🎓 سافٹ ویئر انجینئرنگ (ڈپلوما)")

# --- مین انٹرفیس ---
st.title("🚀 EduGuide AI: آپ کا سمارٹ تعلیمی مشیر")
st.write("پاکستان کے میٹرک اور انٹر کے طلباء کے لیے ایک مکمل گائیڈ")

# سیشن اسٹیٹ تاکہ بٹن کلک پر ٹیکسٹ باکس اپ ڈیٹ ہو
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

def set_query(query):
    st.session_state.user_input = query

# --- 4. فوری بٹنز (Quick Action Buttons) ---
st.subheader("💡 فوری مدد حاصل کریں:")
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    if st.button("🎓 میٹرک کے بعد ٹاپ 5 فیلڈز"):
        set_query("میٹرک کے بعد ٹاپ 5 فیلڈز اور ان کا مستقبل بتائیں۔")

with col_btn2:
    if st.button("📅 میرا اسٹڈی ٹائم ٹیبل بنائیں"):
        set_query("میں روزانہ 5 گھنٹے پڑھ سکتا ہوں، میرے لیے ایک بہترین اسٹڈی پلانر بنائیں۔")

with col_btn3:
    if st.button("📝 بورڈ پیپر کے لیے ٹپس"):
        set_query("بورڈ کے امتحانات میں اچھے نمبر لینے اور پیپر حل کرنے کے بہترین ٹپس کیا ہیں؟")

# ان پٹ باکس
user_query = st.text_input("اپنا سوال لکھیں یا اوپر سے بٹن منتخب کریں:", value=st.session_state.user_input)

# --- پراسیسنگ ---
if st.button("مشورہ حاصل کریں 🔍"):
    if not user_query:
        st.warning("ارسلان بھائی، پہلے کوئی سوال تو لکھیں یا بٹن دبائیں!")
    else:
        try:
            with st.spinner('EduGuide AI آپ کے لیے بہترین مشورہ تیار کر رہا ہے...'):
                client = Groq(api_key=MY_GROQ_KEY)
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_query}
                    ]
                )
                answer = res.choices[0].message.content
                
                st.divider()
                st.subheader("📋 EduGuide AI کا مشورہ:")
                st.markdown(answer)
                
                st.info("💡 **ٹپ:** آپ مزید تفصیل کے لیے اسکالرشپ یا روڈ میپ کے بارے میں بھی پوچھ سکتے ہیں۔")
                        
        except Exception as e:
            st.error("نیٹ ورک یا API Key کا مسئلہ ہے۔ براہ کرم چیک کریں۔")

# --- فوٹر ---
st.divider()
st.caption("AI Seekho 2026 Competition Project | Prepared for Google Online Competition")