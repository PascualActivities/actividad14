import os
import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Portfolio | Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Modern CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero section */
    .hero-container {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(168, 85, 247, 0.08) 50%, rgba(59, 130, 246, 0.05) 100%);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 20px;
        padding: 30px 35px;
        margin-bottom: 25px;
        position: relative;
        overflow: hidden;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        padding: 5px 14px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.25);
    }

    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 10px;
        background: linear-gradient(90deg, #1e293b, #475569);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    @media (prefers-color-scheme: dark) {
        .hero-title {
            background: linear-gradient(90deg, #f8fafc, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    }

    .hero-desc {
        font-size: 1.05rem;
        color: #64748b;
        max-width: 850px;
        line-height: 1.6;
        margin-bottom: 15px;
    }

    /* Metrics Bar */
    .metric-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(0, 0, 0, 0.06);
        padding: 6px 14px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        backdrop-filter: blur(10px);
    }

    @media (prefers-color-scheme: dark) {
        .metric-pill {
            background: rgba(30, 41, 59, 0.7);
            border-color: rgba(255, 255, 255, 0.08);
            color: #e2e8f0;
        }
    }

    /* Card styling */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        background: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(0, 0, 0, 0.08) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03) !important;
    }

    @media (prefers-color-scheme: dark) {
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(30, 32, 45, 0.7) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.25) !important;
        }
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 14px 28px rgba(99, 102, 241, 0.16) !important;
        border-color: rgba(99, 102, 241, 0.4) !important;
    }

    /* Fixed image standard inside cards */
    div[data-testid="stImage"] img {
        height: 185px !important;
        object-fit: cover !important;
        border-radius: 12px !important;
        width: 100% !important;
    }

    /* Tags and Chips */
    .badge-category {
        display: inline-block;
        padding: 3px 10px;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 8px;
        background: rgba(99, 102, 241, 0.12);
        color: #4f46e5;
        margin-bottom: 8px;
    }

    @media (prefers-color-scheme: dark) {
        .badge-category {
            background: rgba(99, 102, 241, 0.25);
            color: #a5b4fc;
        }
    }

    .tech-pill {
        display: inline-block;
        padding: 2px 8px;
        font-size: 0.72rem;
        font-weight: 600;
        border-radius: 6px;
        background: rgba(148, 163, 184, 0.15);
        color: #475569;
        margin-right: 4px;
        margin-bottom: 4px;
    }

    @media (prefers-color-scheme: dark) {
        .tech-pill {
            background: rgba(148, 163, 184, 0.2);
            color: #cbd5e1;
        }
    }

    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-top: 8px;
        margin-bottom: 6px;
        color: inherit;
        line-height: 1.3;
    }

    .card-desc {
        font-size: 0.88rem;
        color: #64748b;
        line-height: 1.5;
        min-height: 48px;
        margin-bottom: 12px;
    }

    @media (prefers-color-scheme: dark) {
        .card-desc {
            color: #94a3b8;
        }
    }

    /* Profile / Sidebar styling */
    .sidebar-profile {
        padding: 15px 0;
        text-align: center;
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        margin-bottom: 18px;
    }

    @media (prefers-color-scheme: dark) {
        .sidebar-profile {
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
    }

    /* Footer */
    .portfolio-footer {
        text-align: center;
        padding: 35px 15px 20px 15px;
        color: #94a3b8;
        font-size: 0.85rem;
        border-top: 1px solid rgba(0, 0, 0, 0.06);
        margin-top: 40px;
    }

    @media (prefers-color-scheme: dark) {
        .portfolio-footer {
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Project Data Store
# ---------------------------------------------------------
PROJECTS = [
    {
        "id": "tts",
        "title": "Conversión de Texto a Voz",
        "category": "Audio & Voz",
        "category_icon": "🎙️",
        "image": "txt_to_audio2.png",
        "desc": "Síntesis vocal hiperrealista a partir de texto (TTS) con modulación de entonación y arquitectura multimodal.",
        "tags": ["TTS", "Audio AI", "Streamlit", "Multimodal"],
        "url": "https://imultimod.streamlit.app/",
        "featured": True
    },
    {
        "id": "yolo",
        "title": "Reconocimiento y Detección de Objetos",
        "category": "Visión por Computador",
        "category_icon": "👁️",
        "image": "txt_to_audio.png",
        "desc": "Detección, conteo y clasificación de objetos en imágenes en tiempo real mediante la arquitectura YOLOv5.",
        "tags": ["YOLOv5", "Computer Vision", "PyTorch", "Realtime"],
        "url": "https://yolov5cmc.streamlit.app/",
        "featured": True
    },
    {
        "id": "training",
        "title": "Entrenamiento de Modelos Personalizados",
        "category": "Modelos & ML",
        "category_icon": "⚙️",
        "image": "OIG5.jpg",
        "desc": "Laboratorio para entrenar, transferir aprendizaje y probar modelos customizados de deep learning.",
        "tags": ["Model Training", "Deep Learning", "Inferencia", "Transfer Learning"],
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "featured": False
    },
    {
        "id": "stt",
        "title": "Conversión de Voz a Texto",
        "category": "Audio & Voz",
        "category_icon": "🎙️",
        "image": "OIG8.jpg",
        "desc": "Reconocimiento automático del habla (STT) y traducción inteligente en vivo con alta precisión.",
        "tags": ["Speech-to-Text", "Audio AI", "Traducción", "NLP"],
        "url": "https://traductorw.streamlit.app/",
        "featured": False
    },
    {
        "id": "data_agents",
        "title": "Análisis de Datos con Agentes IA",
        "category": "Agentes & Datos",
        "category_icon": "📊",
        "image": "data_analisis.png",
        "desc": "Automatización del análisis exploratorio, insights estadísticos y visualizaciones mediante agentes inteligentes.",
        "tags": ["AI Agents", "Pandas", "Analytics", "Data Science"],
        "url": "https://dataagente.streamlit.app/",
        "featured": True
    },
    {
        "id": "whisper",
        "title": "Transcriptor Inteligente Audio / Video",
        "category": "Audio & Voz",
        "category_icon": "🎙️",
        "image": "OIG3.jpg",
        "desc": "Transcripción multimedia profunda con soporte multilenguaje y marcas de tiempo utilizando OpenAI Whisper.",
        "tags": ["Whisper", "Multimedia", "Transcripción", "OpenAI"],
        "url": "https://transcript-whisper.streamlit.app/",
        "featured": False
    },
    {
        "id": "rag_pdf",
        "title": "Generación en Contexto (RAG con PDF)",
        "category": "LLMs & RAG",
        "category_icon": "📄",
        "image": "Chat_pdf.png",
        "desc": "Asistente conversacional con recuperación aumentada (RAG) para consultar y extraer información de documentos PDF.",
        "tags": ["RAG", "LangChain", "Vector DB", "PDF Chat"],
        "url": "https://chatpdf-cc.streamlit.app/",
        "featured": True
    },
    {
        "id": "vision_gpt4o",
        "title": "Análisis Multimodal de Imágenes",
        "category": "Visión por Computador",
        "category_icon": "👁️",
        "image": "OIG4.jpg",
        "desc": "Interpretación visual avanzada, resolución de problemas y razonamiento multimodal potenciado por GPT-4o.",
        "tags": ["GPT-4o", "Multimodal", "Vision AI", "Image QA"],
        "url": "https://vision2-gpt4o.streamlit.app/",
        "featured": False
    },
    {
        "id": "cyberphysical",
        "title": "Sistemas Ciberfísicos & Percepción",
        "category": "Sistemas Ciberfísicos",
        "category_icon": "🤖",
        "image": "OIG6.jpg",
        "desc": "Interacción entre algoritmos de visión por computador y el mundo físico para sensórica y automatización.",
        "tags": ["Ciberfísica", "IoT", "Sensórica", "Automatización"],
        "url": "https://vision2-gpt4o.streamlit.app/",
        "featured": False
    }
]

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    # Profile avatar
    if os.path.exists("audio_to_txt.png"):
        avatar_img = Image.open("audio_to_txt.png")
        st.image(avatar_img, use_container_width=True)
    
    st.markdown("""
        <div style="text-align: center; margin-top: -10px; margin-bottom: 15px;">
            <h2 style="margin: 0; font-size: 1.35rem; font-weight: 800;">Carlos M. Correa</h2>
            <p style="color: #6366f1; font-weight: 600; font-size: 0.85rem; margin-top: 4px; margin-bottom: 10px;">
                Desarrollador & Especialista en IA
            </p>
            <p style="font-size: 0.82rem; color: #64748b; line-height: 1.45; text-align: justify;">
                Desarrollo de soluciones avanzadas en Inteligencia Artificial aplicada: visión por computador, modelos de lenguaje (LLMs), síntesis y reconocimiento de voz, y agentes autónomos.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.subheader("📚 Recursos & Prácticas")
    st.markdown(
        "Accede al portal oficial con guías didácticas, ejercicios prácticos y material formativo paso a paso:"
    )
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.link_button("🌐 Abrir Portal de Ejercicios", url_ia, use_container_width=True)

    st.markdown("---")
    st.subheader("🛠️ Stack Tecnológico")
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 4px;">
        <span class="tech-pill">Python</span>
        <span class="tech-pill">Streamlit</span>
        <span class="tech-pill">PyTorch</span>
        <span class="tech-pill">YOLOv5</span>
        <span class="tech-pill">OpenAI Whisper</span>
        <span class="tech-pill">GPT-4o Vision</span>
        <span class="tech-pill">LangChain</span>
        <span class="tech-pill">RAG / Vector DB</span>
        <span class="tech-pill">Pandas</span>
        <span class="tech-pill">AI Agents</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("© 2026 Carlos M. Correa • cmcorrea_apps")

# ---------------------------------------------------------
# Main Header / Hero Section
# ---------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">⚡ Portafolio de Innovación Tecnológica</div>
    <div class="hero-title">Aplicaciones de Inteligencia Artificial</div>
    <div class="hero-desc">
        Explora una suite interactiva de proyectos y soluciones desplegadas en producción. 
        Herramientas prácticas que integran Deep Learning, Visión Computacional, Modelos de Voz, Agentes y Arquitecturas RAG.
    </div>
    <div style="margin-top: 10px;">
        <span class="metric-pill">🚀 <b>9</b> Aplicaciones en vivo</span>
        <span class="metric-pill">🧩 <b>5</b> Áreas de especialización</span>
        <span class="metric-pill">☁️ Despliegues 100% Cloud</span>
        <span class="metric-pill">⚡ Modelos SOTA (YOLO, Whisper, GPT-4o)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Filter & Search Controls
# ---------------------------------------------------------
categories = [
    "🌟 Todas las Aplicaciones",
    "👁️ Visión por Computador",
    "🎙️ Audio & Voz",
    "📄 LLMs & RAG",
    "📊 Agentes & Datos",
    "🤖 Sistemas Ciberfísicos",
    "⚙️ Modelos & ML"
]

col_search, col_filter = st.columns([1.2, 1.8])

with col_search:
    search_query = st.text_input(
        "🔍 Buscar por tecnología o nombre:",
        placeholder="Ej: YOLO, Whisper, RAG, GPT-4o, Audio...",
        label_visibility="collapsed"
    )

with col_filter:
    selected_cat = st.selectbox(
        "Filtrar por categoría:",
        categories,
        label_visibility="collapsed"
    )

# Filter logic
filtered_projects = []
for p in PROJECTS:
    # Category match
    cat_match = True
    if selected_cat != "🌟 Todas las Aplicaciones":
        # Extract clean category name
        cat_clean = selected_cat.split(" ", 1)[1]
        cat_match = (p["category"] == cat_clean)
    
    # Search query match
    search_match = True
    if search_query.strip():
        q = search_query.lower()
        search_match = (
            q in p["title"].lower() or 
            q in p["desc"].lower() or 
            q in p["category"].lower() or
            any(q in t.lower() for t in p["tags"])
        )
    
    if cat_match and search_match:
        filtered_projects.append(p)

# Result status counter
st.markdown(
    f"<p style='color: #64748b; font-size: 0.9rem; margin-top: 5px; margin-bottom: 18px;'>"
    f"Mostrando <b>{len(filtered_projects)}</b> de <b>{len(PROJECTS)}</b> aplicaciones disponibles"
    f"</p>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Projects Grid
# ---------------------------------------------------------
if not filtered_projects:
    st.info("No se encontraron aplicaciones con los criterios seleccionados. Intenta con otra búsqueda o categoría.")
else:
    cols = st.columns(3)
    for i, proj in enumerate(filtered_projects):
        col = cols[i % 3]
        with col:
            with st.container(border=True):
                # Header category badge
                st.markdown(
                    f"<div class='badge-category'>{proj['category_icon']} {proj['category']}</div>",
                    unsafe_allow_html=True
                )
                
                # Image
                if os.path.exists(proj["image"]):
                    img = Image.open(proj["image"])
                    st.image(img, use_container_width=True)
                else:
                    st.write("📷 *Imagen no disponible*")
                
                # Title & Description
                st.markdown(f"<div class='card-title'>{proj['title']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='card-desc'>{proj['desc']}</div>", unsafe_allow_html=True)
                
                # Tech tags
                tags_html = "".join([f"<span class='tech-pill'>{t}</span>" for t in proj["tags"]])
                st.markdown(f"<div style='margin-bottom: 14px;'>{tags_html}</div>", unsafe_allow_html=True)
                
                # CTA Button
                st.link_button(
                    "🚀 Probar Aplicación",
                    proj["url"],
                    use_container_width=True
                )

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("""
<div class="portfolio-footer">
    <p><b>Portafolio de Soluciones de Inteligencia Artificial</b> • Desarrollado con Streamlit & Python</p>
    <p style="font-size: 0.8rem; margin-top: 4px;">
        Descubre más proyectos, tutoriales y documentación en el 
        <a href="https://sites.google.com/view/aplicacionesdeia/inicio" target="_blank" style="color: #6366f1; text-decoration: none; font-weight: 600;">Portal de Aplicaciones de IA</a>
    </p>
</div>
""", unsafe_allow_html=True)
