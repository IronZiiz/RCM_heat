import streamlit as st
import math as m

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def mm_to_m(millimeters):
    return millimeters / 1000


    


    return R + Ls
def time_to_target(Ta, Tt, To, rho, cp, ks, R, Ls):
    Ta = celsius_to_kelvin(Ta)
    Tt = celsius_to_kelvin(Tt)
    To = celsius_to_kelvin(To)
    R = (R - 2*Ls)/2
    R = mm_to_m(R)
    t = ((rho * cp * R**2 * m.log((Ls + R) / R) * m.log((Tt - To) / (Tt - Ta))) /(2*ks))
    t = round(t, 4)
    return t

# Configuração da página
st.title("Cálculo do Tempo de Aquecimento do Fio de Cobre")
st.write("Este aplicativo calcula o tempo necessário para que um fio de cobre envolto em silicone atinja uma temperatura alvo.")

# Entradas do usuário
Ta = st.number_input("Temperatura alvo (°C)", value=100.0, step=1.0)
Tt = st.number_input("Temperatura do forno (°C)", value=200.0, step=1.0)
To = st.number_input("Temperatura inicial (°C)", value=30.0, step=1.0)

rho = st.number_input("Densidade do cobre (kg/m³)", value=8960.0, step=10.0)
cp = st.number_input("Calor específico do cobre (J/kgK)", value=385.0, step=1.0)
ks = st.number_input("Condutividade térmica do silicone (W/mK)", value=0.5, step=0.01)


R = st.number_input("Diametro do fio (mm)", value=0.44, step=0.01)
Ls = st.number_input("Espessura da camada de silicone (mm)", value=0.8, step=0.01)

# Botão para calcular o tempo
if st.button("Calcular Tempo"):
    tempo = time_to_target(Ta, Tt, To, rho, cp, ks, R, Ls)
    st.success(f"O tempo para que a interface cobre-silicone atinja {Ta}°C é {tempo} segundos.")
