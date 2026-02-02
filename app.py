import streamlit as st
import asyncio
from agent import agent 
from agents import Runner
import os

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Portfolio - Charles Auvrai",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PETIT CSS OBLIGATOIRE POUR LA COULEUR DE L'INPUT ---
st.markdown("""
<style>
    /* Je veux modifier la couleur de l'input pour la mettre en bleu */
    .stChatInput textarea::placeholder {
        color: #2E86C1 !important; 
        opacity: 1; 
        font-weight: bold;
    }
    
    .stChatInput textarea {
        color: #2E86C1 !important;
        caret-color: #1a252f !important; 
    }
    
    /* Style pour les phrases mises en avant */
    .highlight-phrase {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        border-left: 5px solid #1976D2;
        padding: 20px 15px;
        border-radius: 8px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .highlight-phrase p {
        color: #0D47A1;
        font-size: 16 px;
        font-weight: 600;
        margin: 0;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. ÉTAT (SESSION STATE) ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Bonjour ! Je suis l'IA de Charles. Pose-moi une question sur mon parcours ou mes compétences !"}
    ]

if "request_count" not in st.session_state:
    st.session_state.request_count = 0


if "view_history" not in st.session_state:
    st.session_state.view_history = False

MAX_REQUESTS = 5

# 4. BARRE LATÉRALE
with st.sidebar:
    if os.path.exists("assets/photo_profil.jpg"):
        col_g, col_img, col_d = st.columns([1, 2, 1])
        with col_img:
            st.image("assets/photo_profil.jpg", width=150)
    
    st.markdown("## :blue[Charles Auvrai]")
    st.caption("Data Analyst & Sportif SHN")
    
    st.divider() 
    st.text("📍 Niort/Tours/Vendôme, France")
    st.text("🎓 BUT Science des Données")
    st.text("💻 Data & IA")
    
    st.divider()
    
    with st.container(border=True):
        st.subheader("🔗 Me contacter")
        st.link_button("LinkedIn", "https://www.linkedin.com/in/charles-auvrai-0b6b42292/", use_container_width=True)
        st.link_button("Email", "mailto:charlesauvrai@gmail.com", use_container_width=True)

# 5. LOGIQUE D'AFFICHAGE 

ai_avatar = "assets/avatar_ia.png" if os.path.exists("assets/avatar_ia.png") else "🤖"
user_avatar = "👤"

# SI ON A ENCORE DES CRÉDITS ( < 5 )
if st.session_state.request_count < MAX_REQUESTS:
    
    st.title("Bienvenue sur mon chatbot!")
    
    # A. Affichage de l'historique
    for message in st.session_state.messages:
        avatar_to_show = ai_avatar if message["role"] == "assistant" else user_avatar
        with st.chat_message(message["role"], avatar=avatar_to_show):
            st.write(message["content"])

    # B. Suggestions de questions
    st.divider()
    st.caption(":blue[ Suggestions rapides :]")
    
    col1, col2, col3, col4 = st.columns(4)
    prompt = None

    if col1.button("Ma Formation", use_container_width=True):
        prompt = "Peux-tu me détailler ta formation actuelle ?"
    
    if col2.button("Expériences professionnelles", use_container_width=True):
        prompt = "Quelles sont tes expériences professionnelles ?"
    
    if col3.button("Qui suis-je ?", use_container_width=True):
        prompt = "Qui es-tu ? Raconte-moi ton parcours."
        
    if col4.button("Passions ?", use_container_width=True):
        prompt = "Que fais-tu en dehors des cours (Passions, Sport) ?"

    # C. Zone de saisie
    chat_input_value = st.chat_input("Votre question ici...")
    
    if chat_input_value:
        prompt = chat_input_value

    # D. Traitement
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        if not chat_input_value:
             with st.chat_message("user", avatar=user_avatar):
                st.write(prompt)

        with st.chat_message("assistant", avatar=ai_avatar):
            with st.spinner("Analyse en cours..."):
                st.session_state.request_count += 1
                
                async def get_res():
                    res = await Runner.run(agent, prompt)
                    return res.final_output
                
                # Petit fix asyncio pour éviter les erreurs de boucle
                try:
                    loop = asyncio.get_event_loop()
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)

                response_text = loop.run_until_complete(get_res())
                
                if "volley" in response_text.lower():
                    response_text += " 🏐"

                st.write(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
                st.rerun()

# SI QUESTION ( >= 5 ) -> ÉCRAN DE FIN MODIFIÉ
else:
    # Si on n'est PAS en mode "lecture historique", on affiche la carte de contact
    if not st.session_state.view_history:
        placeholder = st.empty()
        
        with placeholder.container():
            st.divider()
            
            c1, c2, c3 = st.columns([1, 2, 1])
            
            with c2:
                
               
                st.markdown("""
                <div class="highlight-phrase">
                    <p>Vous en savez plus sur moi maintenant.</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class="highlight-phrase">
                    <p>Pour discuter plus concrètement de mon profil, retrouvez-moi ici :</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("") 
                
                if os.path.exists("assets/photo_profil.jpg"):
                    st.image("assets/photo_profil.jpg", width=500)
                
                st.write("") 
                
                with st.container(border=True):
                    st.link_button("👔 Me contacter sur LinkedIn", "https://www.linkedin.com/in/charles-auvrai-0b6b42292/", use_container_width=True)
                    st.link_button("📧 M'envoyer un Email", "mailto:charlesauvrai@gmail.com", use_container_width=True)
                
                st.divider()
                
                
                if st.button("Revoir l'historique", use_container_width=True):
                    st.session_state.view_history = True
                    st.rerun()

    # Si on EST en mode lecture historique, on affiche un bouton retour en haut
    else:
        if st.button("🔙 Retour à l'écran de fin", use_container_width=True):
            st.session_state.view_history = False
            st.rerun()

    # L'historique s'affiche toujours en dessous 
    st.subheader("Historique de la conversation")
    for message in st.session_state.messages:
        role_icon = "🤖" if message["role"] == "assistant" else "👤"
        with st.chat_message(message["role"], avatar=role_icon):

            st.write(message["content"])
