import streamlit as st
from gtts import gTTS
import os
import tempfile
from io import BytesIO
import base64

def text_to_speech(text, language='en'):
    """Convert text to speech and return audio data"""
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        st.error(f"Error generating speech: {str(e)}")
        return None

def get_audio_download_link(audio_bytes, filename="voiceover.mp3"):
    """Generate a download link for the audio file"""
    # Create a copy of the audio data to avoid reading the same BytesIO twice
    audio_copy = BytesIO(audio_bytes.getvalue())
    b64 = base64.b64encode(audio_copy.read()).decode()
    href = f'<a href="data:audio/mp3;base64,{b64}" download="{filename}">Download Audio File</a>'
    return href

def main():
    st.set_page_config(
        page_title="Text to Speech Voiceover Generator",
        page_icon="🎤",
        layout="wide"
    )
    
    st.title("🎤 Text to Speech Voiceover Generator")
    st.markdown("Convert your text into professional voiceover audio files")
    
    # Sidebar for settings
    st.sidebar.header("Settings")
    
    # Language selection
    languages = {
        'English': 'en',
        'Spanish': 'es',
        'French': 'fr',
        'German': 'de',
        'Italian': 'it',
        'Portuguese': 'pt',
        'Russian': 'ru',
        'Japanese': 'ja',
        'Korean': 'ko',
        'Chinese (Simplified)': 'zh-cn',
        'Arabic': 'ar',
        'Hindi': 'hi'
    }
    
    selected_language = st.sidebar.selectbox(
        "Select Language",
        list(languages.keys()),
        index=0
    )
    
    # Text input area
    st.header("Enter Your Text")
    
    # Text input with character counter
    text_input = st.text_area(
        "Type or paste your text here:",
        height=200,
        placeholder="Enter the text you want to convert to speech..."
    )
    
    # Character counter
    if text_input:
        char_count = len(text_input)
        word_count = len(text_input.split())
        st.info(f"📊 Text Statistics: {char_count} characters, {word_count} words")
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button(
            "🎵 Generate Voiceover",
            type="primary",
            use_container_width=True
        )
    
    # Process the text
    if generate_button and text_input.strip():
        with st.spinner("Generating voiceover..."):
            try:
                # Generate audio
                audio_data = text_to_speech(text_input, languages[selected_language])
                
                if audio_data:
                    st.success("✅ Voiceover generated successfully!")
                    
                    # Display audio player
                    st.header("🎧 Preview Your Voiceover")
                    st.audio(audio_data, format='audio/mp3')
                    
                    # Download section
                    st.header("📥 Download Options")
                    
                    # Create a clean filename
                    clean_text = "".join(c for c in text_input[:30] if c.isalnum() or c in (' ', '-', '_')).rstrip()
                    filename = f"voiceover_{clean_text}.mp3"
                    
                    # Download button
                    st.markdown(
                        get_audio_download_link(audio_data, filename),
                        unsafe_allow_html=True
                    )
                    
                    # Additional info
                    st.info("💡 Tip: Right-click the download link and select 'Save link as...' to save the file")
                else:
                    st.error("❌ Failed to generate voiceover. Please try again.")
                    
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("💡 Try using shorter text or check your internet connection.")
                
    elif generate_button and not text_input.strip():
        st.warning("⚠️ Please enter some text to generate a voiceover.")
    
    # Features section
    st.header("✨ Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🌍 Multiple Languages**
        - Support for 12+ languages
        - High-quality voice synthesis
        """)
    
    with col2:
        st.markdown("""
        **🎵 Instant Preview**
        - Listen before downloading
        - Real-time generation
        """)
    
    with col3:
        st.markdown("""
        **📱 Easy Download**
        - MP3 format
        - Custom filenames
        - No registration required
        """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "Made with ❤️ using Streamlit and gTTS | "
        "Powered by Google Text-to-Speech"
    )

if __name__ == "__main__":
    main() 