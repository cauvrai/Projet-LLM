import os
from dotenv import load_dotenv
from upstash_vector import Index

# 1. On charge tes nouvelles clés du .env
load_dotenv()
index = Index(url=os.getenv("UPSTASH_VECTOR_REST_URL"), token=os.getenv("UPSTASH_VECTOR_REST_TOKEN"))

def remplir_upstash():
    data_path = "data"
    
    if not os.path.exists(data_path):
        print(f"Erreur : Le dossier '{data_path}' n'existe pas !")
        return

    print("Connexion au Upstash...")
    
    # On scanne le dossier data
    fichiers = [f for f in os.listdir(data_path) if f.endswith(".md")]
    
    if not fichiers:
        print("⚠️ Aucun fichier .md trouvé dans le dossier data.")
        return

    for filename in fichiers:
        file_path = os.path.join(data_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            texte = f.read().strip()
            
            if texte:
                # On envoie le texte vers Upstash
                index.upsert(vectors=[(filename, texte)])
                print(f"✅ Envoyé avec succès : {filename} ({len(texte)} caractères)")
            else:
                print(f"⚠️ Fichier vide ignoré : {filename}")

if __name__ == "__main__":
    remplir_upstash()
    print("\nUpstash rempli ! Tu peux tester l'agent.")