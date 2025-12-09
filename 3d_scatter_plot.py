import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

st.title("Visualisasi 3D Scatter Plot")
st.write("Kelompok 13")
st.markdown("""
- ROZA KURNIAWAN NUR WAKID (0110222124)
- PRAMANA RAHMANSAH PUTRA (0110122051)
- IMAD HASAN AQIL (0110221166)
""")

# Data Dummy
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100],
    'Penjualan': [50, 60, 70, 90, 100, 110, 130, 150, 180]
}
df = pd.DataFrame(data)

# Fungsi untuk membuat plot 3D
def plot_3d():
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotting
    scatter = ax.scatter(df['Suhu'], df['Kelembapan'], df['Penjualan'], c='red', s=100)
    
    # Labeling
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Kelembapan (%)')
    ax.set_zlabel('Penjualan')
    ax.set_title('Hubungan Suhu, Kelembapan, dan Penjualan')
    
    return fig

# Menampilkan di Streamlit
st.pyplot(plot_3d())