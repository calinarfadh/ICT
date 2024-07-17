import streamlit as st
from PIL import Image

def main():
    st.title("PLS 2024 SMA PLUS PGRI CIBINONG")
    
    imgpython = Image.open("logopython2.png")
    imgprodesk = Image.open("logoprodesk.jpg")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(
            imgprodesk,
            caption = "Student Day Programming Desktop",
            width = 300,
            channels="RGB"
        )
        
    with col2:
        st.image(
            imgpython,
            caption = "Bahasa Pemograman Python" ,
            width = 300,
            channels= "RGB"
        )
    
    name = st.text_input("Masukkan nama Anda:")

    if st.button("Submit"):
        if name:
            st.write(f"Selamat datang, {name}!","Selamat Mengikuti PLS 2024")
            st.success("Semoga Sukses!")
            st.balloons()
        else:
            st.write("Silakan masukkan nama Anda.")
            
if __name__ == "__main__":
    main()