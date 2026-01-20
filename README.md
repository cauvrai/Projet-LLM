# Portfolio Interactif - Projet Universitaire


Bienvenue sur le code source de mon **Portfolio Chatbot**. 
Ce projet est une application web interactive développée en **Python** avec **Streamlit**. Elle permet aux recruteurs et visiteurs de dialoguer avec une Intelligence Artificielle entraînée pour répondre à des questions sur mon parcours de **Data Analyst** et de **Sportif de Haut Niveau**.

---

## 🚀 Fonctionnalités

- **💬 Interface Chatbot Interactive :** Discussion fluide avec un agent IA personnalisé.
- **⚡ Suggestions Dynamiques :** Boutons rapides pour les questions fréquentes (Formation, Expériences, Passions).
- **🎨 UI/UX Soignée :** Interface personnalisée (couleurs natives Streamlit, avatars, mise en page responsive) sans CSS complexe.
- **⏳ Gestion de Session :**
  - Historique de conversation persistant.
  - Système de **crédits** (limité à 5 questions par session pour la démonstration).
- **🔒 Écran de Fin :** Affichage d'un écran de contact ("Call to Action") une fois la limite de questions atteinte.
- **⚙️ Asynchrone :** Utilisation de `asyncio` pour gérer les réponses de l'IA sans bloquer l'interface.

## 🛠️ Stack Technique

* **Langage :** Python
* **Framework Web :** [Streamlit](https://streamlit.io/)
* **IA / LLM :** Agent personnalisé (fichiers `agent.py` et `agents.py`)
* **Gestion Async :** `asyncio`

## 📂 Structure du Projet

```bash
├── app.py              # 🏠 Point d'entrée principal de l'application (Interface & Logique)
├── agent.py            # 🧠 Configuration de l'agent IA (Prompt & Modèle)
├── agents.py           # ⚙️ Moteur d'exécution de l'agent (Runner)
├── assets/             # 🖼️ Images (Avatar IA, Photo de profil)
│   ├── avatar_ia.png
│   └── photo_profil.jpg
├── requirements.txt    # 📦 Liste des dépendances Python
└── README.md           # 📄 Ce fichier
