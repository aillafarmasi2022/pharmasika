import streamlit as st
import pandas as pd

# Membaca file Excel
df = pd.read_excel("kamus_farmasi.xlsx")

# Judul aplikasi
st.title("📖 Kamus Istilah Farmasi")

# Input pencarian istilah
search_term = st.text_input("Cari istilah farmasi:", "").strip().lower()

# Filter berdasarkan pencarian
if search_term:
    filtered_df = df[df["Istilah"].str.lower().str.contains(search_term, na=False)]
else:
    filtered_df = df

# Menampilkan hasil pencarian
st.write("### Hasil Pencarian:")
st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.caption("Dibuat dengan ❤️ menggunakan Streamlit")
