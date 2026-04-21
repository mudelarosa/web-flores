import streamlit as st

st.markdown(
    """
    <style>

/* Arreglar selectbox (desplegable) */
div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
}

/* Opciones del desplegable */
ul {
    background-color: white !important;
    color: black !important;
}

/* Inputs (nombre, teléfono, etc.) */
input, textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 8px !important;
}

/* Labels (Nombre, Teléfono…) */
label {
    color: black !important;
}

/* Botón */
.stButton>button {
    background-color: #e75480 !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: bold;
}

/* Hover botón */
.stButton>button:hover {
    background-color: #d9436e !important;
    color: white !important;
}

    .stApp {
        background-image: url("https://images.unsplash.com/photo-1490750967868-88aa4486c946");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Capa oscura encima del fondo */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5); /* más oscuro */
        z-index: -1;
    }

    /* Caja del contenido */
    .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 12px;
    }

    /* Texto oscuro */
    h1, h2, h3, h4, h5, h6, p, label, li {
    color: black !important;
}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Reparto de Flores", page_icon="💐", layout="wide")

# Título principal

st.markdown("<h2 style='text-align: center; color: #e75480;'>🌸 JEILAFLOR 🌸</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Ramos y flor cortada para floristerías</h3>", unsafe_allow_html=True)

st.divider()

# Descripción
st.markdown("""
### 🚚 Servicio profesional de reparto

Ofrecemos:
- 💐 Ramos de flores frescas
- 🪴 Cubos de flor cortada para floristerías
- ⚡ Entregas rápidas y seguras
""")

st.divider()

# Formulario
st.markdown("## 📝 Haz tu pedido")

nombre = st.text_input("Nombre")
telefono = st.text_input("Teléfono")
direccion = st.text_input("Dirección de entrega")

producto = st.selectbox(
    "Producto",
    ["Ramo de flores", "Cubo flor cortada"]
)

cantidad = st.number_input("Cantidad", min_value=1, step=1)

mensaje = st.text_area("Detalles del pedido")

if st.button("🌸 Enviar pedido"):
    texto = f"Pedido de flores:%0A"
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
    text-align:center;
">
📲 Confirmar por WhatsApp
</a>
""", unsafe_allow_html=True)

st.divider()

st.markdown("## 🌼 Nuestros productos")

st.image("images/ramo.jpg", caption="Ramos de flores", use_container_width=True)
st.image("images/cubo.jpg", caption="Flor cortada para floristerías", use_container_width=True)

with col1:
    st.image("images/ramo.jpg", caption="Ramos de flores", use_container_width=True)

with col2:
    st.image("images/cubo.jpg", caption="Flor cortada para floristerías", use_container_width=True)

# Footer
st.markdown("<p style='text-align: center;'>🌸 Flores frescas | Servicio rápido | Atención personalizada</p>", unsafe_allow_html=True)

