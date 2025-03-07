import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# KONFIGURASI HALAMAN HARUS DI PALING AWAL
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Membaca dataset
archive = pd.read_csv('all_data.csv')

# Judul Dashboard (Dibuat Rata Tengah)
st.markdown(
    "<h1 style='text-align: center;'>Bike Sharing Dashboard 🚴‍♂</h1>", 
    unsafe_allow_html=True
)

# Menampilkan data
st.subheader("Data Day dan Data Hour")
st.write(archive)

# Menampilkan visualisasi barchart "Total Penyewaan Sepeda Berdasarkan Musim"
st.markdown(
    "<h2 style='text-align: center;'>Total Penyewaan Sepeda Berdasarkan Musim</h2>", 
    unsafe_allow_html=True
)
season_counts = archive.groupby('season')['cnt'].sum()
if not season_counts.empty:
    colors = ['#ADD8E6' if value < season_counts.max() else '#6495ED' for value in season_counts.values]
else:
    colors = ['#ADD8E6']  # Warna default jika data kosong
plt.figure(figsize=(8, 5))
sns.barplot(x=season_counts.index, y=season_counts.values, palette=colors)
plt.xlabel('Season (Musim)', fontsize=12)
plt.ylabel('Total Penyewaan', fontsize=12)
plt.xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(plt)

# Menampilkan visualisasi BarChart "Perbandingan Rata-rata Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan"
st.markdown(
    "<h2 style='text-align: center;'>Perbandingan Rata-rata Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan</h2>", 
    unsafe_allow_html=True
)
ratarata_pengguna = archive.groupby('workingday')[['cnt', 'casual', 'registered']].mean().reset_index()
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x='workingday', y='cnt', data=ratarata_pengguna, palette=['skyblue', 'orange'])
plt.xlabel("Kategori Hari", fontsize=12)
plt.ylabel("Rata-rata Jumlah Penyewaan", fontsize=12)
st.pyplot(plt)

# Menampilkan visualisasi BarChart "Perbandingan Rata-rata Penyewaan Sepeda oleh Kasual dan Terdaftar"
st.markdown(
    "<h2 style='text-align: center;'>Perbandingan Rata-rata Penyewaan Sepeda oleh Kasual dan Terdaftar</h2>", 
    unsafe_allow_html=True
)
avg_users_melted = ratarata_pengguna.melt(id_vars='workingday', value_vars=['casual', 'registered'], var_name='User Type', value_name='Average Rentals')
plt.figure(figsize=(8, 5))
sns.barplot(x='workingday', y='Average Rentals', hue='User Type', data=avg_users_melted, palette=['skyblue', 'orange'])
plt.xlabel("Kategori Hari", fontsize=12)
plt.ylabel("Rata-rata Jumlah Penyewa", fontsize=12)
plt.legend(title="Tipe Pengguna")
st.pyplot(plt)

# Footer
st.caption("📊 Dashboard Bike Sharing | Dibuat oleh Salsabila Mahiroh")