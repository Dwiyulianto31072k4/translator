import streamlit as st
from googletrans import Translator
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="English to Indonesian Translator",
    page_icon="🌐",
    layout="centered"
)

# Inisialisasi translator
translator = Translator()

# Header aplikasi
st.title("🌐 English to Indonesian Translator")
st.markdown("Aplikasi sederhana untuk menerjemahkan teks dari bahasa Inggris ke bahasa Indonesia")

# Membuat dua kolom untuk input dan output
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 English Text")
    # Text area untuk input bahasa Inggris
    english_text = st.text_area(
        "Masukkan teks bahasa Inggris:",
        height=200,
        placeholder="Type or paste your English text here..."
    )

with col2:
    st.subheader("🇮🇩 Indonesian Translation")
    # Container untuk hasil terjemahan
    translation_container = st.empty()

# Tombol untuk menerjemahkan
if st.button("🔄 Translate", type="primary", use_container_width=True):
    if english_text:
        try:
            # Menampilkan loading spinner
            with st.spinner("Translating..."):
                # Melakukan penerjemahan
                translation = translator.translate(english_text, src='en', dest='id')
                time.sleep(0.5)  # Delay kecil untuk UX yang lebih baik
            
            # Menampilkan hasil terjemahan
            with col2:
                translation_container.text_area(
                    "Hasil terjemahan:",
                    value=translation.text,
                    height=200,
                    disabled=True
                )
            
            # Menampilkan informasi tambahan
            st.success("✅ Translation completed!")
            
            # Ekspander untuk informasi detail
            with st.expander("📊 Translation Details"):
                st.write(f"**Source Language:** {translation.src}")
                st.write(f"**Destination Language:** Indonesian")
                st.write(f"**Confidence:** High")
                st.write(f"**Character Count:** {len(english_text)} characters")
                
        except Exception as e:
            st.error(f"❌ Error during translation: {str(e)}")
            st.info("Please check your internet connection and try again.")
    else:
        st.warning("⚠️ Please enter some text to translate!")

# Sidebar dengan fitur tambahan
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This app uses Google Translate API to translate text from English to Indonesian.
    
    **Features:**
    - Real-time translation
    - Simple and clean interface
    - Character count information
    - Error handling
    """)
    
    st.header("💡 Tips")
    st.write("""
    - For best results, use proper English grammar
    - Break long texts into paragraphs
    - Check your internet connection for smooth translation
    """)
    
    # Contoh teks
    st.header("📝 Sample Texts")
    sample_texts = {
        "Simple Greeting": "Hello, how are you today? I hope you're having a great day!",
        "Business Email": "Dear Sir/Madam, I am writing to inquire about your services. Could you please provide more information?",
        "Technical Text": "Artificial Intelligence is transforming the way we interact with technology in our daily lives."
    }
    
    selected_sample = st.selectbox("Choose a sample text:", list(sample_texts.keys()))
    
    if st.button("Use Sample"):
        st.session_state.sample_text = sample_texts[selected_sample]
        st.rerun()

# Menggunakan sample text jika ada
if 'sample_text' in st.session_state:
    english_text = st.session_state.sample_text
    del st.session_state.sample_text
    st.rerun()

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Google Translate API")
