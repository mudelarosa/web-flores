import streamlit as st

st.set_page_config(page_title="JEILAFLOR", page_icon="💐", layout="wide")

# CSS PRO
st.markdown("""
<style>

/* Fondo */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1490750967868-88aa4486c946");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Capa oscura */
.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    z-index: -1;
}

/* Contenedor */
.block-container {
    background-color: rgba(255,255,255,0.95);
    padding: 2rem;
    border-radius: 15px;
}

/* Inputs */
input, textarea {
    background-color: white !important;
    color: black !important;
}

/* Botones */
.stButton>button {
    background-color: #e75480 !important;
    color: white !important;
    border-radius: 10px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #d9436e !important;
}

/* Móvil */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<h1 style='text-align:center; color:#e75480;'>🌸 JEILAFLOR 🌸</h1>
<p style='text-align:center; font-size:18px;'>
Reparto profesional de flores frescas para floristerías y eventos
</p>
""", unsafe_allow_html=True)

# BOTÓN WHATSAPP ARRIBA
telefono_negocio = "34653379953"
url_base = f"https://wa.me/{telefono_negocio}"

st.markdown(f"""
<div style="text-align:center;">
<a href="{url_base}" target="_blank" style="
    display:inline-block;
    background-color:#25D366;
    color:white;
    padding:14px 30px;
    border-radius:12px;
    text-decoration:none;
    font-weight:bold;
    font-size:18px;
">
📲 Pedir por WhatsApp
</a>
</div>
""", unsafe_allow_html=True)

st.divider()

# PRODUCTOS
st.markdown("## 🌼 Nuestros productos")

col1, col2 = st.columns(2)

with col1:
    st.image("images/ramo.jpg", use_container_width=True)
    st.markdown("### 💐 Ramos de flores")
    st.write("Perfectos para eventos, regalos y pedidos personalizados.")

with col2:
    st.image("images/cubo.jpg", use_container_width=True)
    st.markdown("### 🪴 Flor cortada")
    st.write("Suministro profesional para floristerías.")

st.divider()

# FORMULARIO
st.markdown("## 📝 Haz tu pedido rápido")

nombre = st.text_input("Nombre")
telefono = st.text_input("Teléfono")
direccion = st.text_input("Dirección")

producto = st.selectbox(
    "Producto",
    ["Ramo de flores", "Cubo flor cortada"]
)

cantidad = st.number_input("Cantidad", min_value=1)

mensaje = st.text_area("Detalles del pedido")

if st.button("🌸 Preparar pedido"):
    texto = f"Pedido:%0A{nombre}%0A{telefono}%0A{direccion}%0A{producto}%0A{cantidad}%0A{mensaje}"
    url = f"https://wa.me/{telefono_negocio}?text={texto}"

    st.success("✅ Pedido listo")
    st.markdown(f"""
    <a href="{url}" target="_blank" style="
        display:inline-block;
        background-color:#25D366;
        color:white;
        padding:12px 25px;
        border-radius:10px;
        text-decoration:none;
        font-weight:bold;
    ">
    📲 Confirmar pedido
    </a>
    """, unsafe_allow_html=True)

st.divider()

# FOOTER
st.markdown("""
<p style='text-align:center; font-size:14px;'>
📍 Servicio local | 🚚 Entrega rápida | 📞 Atención directa por WhatsApp
</p>
""", unsafe_allow_html=True)