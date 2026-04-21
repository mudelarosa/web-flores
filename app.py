import streamlit as st

st.set_page_config(page_title="JEILAFLOR", page_icon="💐", layout="wide")

# CSS (mejorado pero estable)
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
    background: rgba(0,0,0,0.4);
    z-index: -1;
}

/* Contenedor */
.block-container {
    background-color: rgba(255,255,255,0.95);
    padding: 1.5rem;
    border-radius: 12px;
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

/* Texto */
h1, h2, h3, p, label {
    color: black !important;
}

/* Móvil */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# HEADER (simple y limpio)
st.markdown("<h2 style='text-align:center; color:#e75480;'>🌸 JEILAFLOR 🌸</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ramos y flor cortada para floristerías</p>", unsafe_allow_html=True)

st.divider()

# DESCRIPCIÓN
st.markdown("""
### 🚚 Servicio profesional de reparto

- 💐 Ramos de flores frescas  
- 🪴 Cubos de flor cortada  
- ⚡ Entregas rápidas y seguras  
""")

st.divider()

# FORMULARIO (igual que el tuyo, solo mejor organizado)
st.markdown("## 📝 Haz tu pedido")

nombre = st.text_input("Nombre")
telefono = st.text_input("Teléfono")
direccion = st.text_input("Dirección de entrega")

producto = st.selectbox(
    "Producto",
    ["Ramo de flores", "Cubo flor cortada"]
)

cantidad = st.number_input("Cantidad", min_value=1)

mensaje = st.text_area("Detalles del pedido")

if st.button("🌸 Enviar pedido"):
    texto = f"Pedido:%0A"
    texto += f"Nombre: {nombre}%0A"
    texto += f"Teléfono: {telefono}%0A"
    texto += f"Dirección: {direccion}%0A"
    texto += f"Producto: {producto}%0A"
    texto += f"Cantidad: {cantidad}%0A"
    texto += f"Detalles: {mensaje}"

    telefono_negocio = "34653379953"
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
    📲 Confirmar por WhatsApp
    </a>
    """, unsafe_allow_html=True)

st.divider()

# PRODUCTOS (como antes pero mejorados)
st.markdown("## 🌼 Nuestros productos")

col1, col2 = st.columns(2)

with col1:
    st.image("images/ramo.jpg", use_container_width=True)
    st.markdown("**💐 Ramos de flores**")

with col2:
    st.image("images/cubo.jpg", use_container_width=True)
    st.markdown("**🪴 Flor cortada**")

st.divider()

# FOOTER
st.markdown("<p style='text-align:center;'>🌸 Flores frescas | Servicio rápido | Atención personalizada</p>", unsafe_allow_html=True)