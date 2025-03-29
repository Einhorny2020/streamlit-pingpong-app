# Streamlit Ping-Pong App – CI/CD + Hébergement Cloud

Ce mini projet montre comment :
- Développer une app interactive Python avec Streamlit
- Ajouter un pipeline CI/CD via GitHub Actions (tests + lint)
- Déployer automatiquement sur **Streamlit Cloud**

---

## Démo hébergée (grâce à Streamlit Cloud)

[Clique ici pour jouer  ton-lien.streamlit.app](https://share.streamlit.io/ton-utilisateur/streamlit-pingpong-app/main/app.py)

---

## Structure

```
streamlit-pingpong-app/
├── app.py                 # Jeu intégré via iframe
├── test_app.py            # Test basique
├── requirements.txt       # Dépendances
├── .flake8                # Style PEP8
├── deploy_local.sh        # Lancement local
└── .github/workflows/ci.yml  # Pipeline CI/CD
```

---

## ▶Lancer localement

```bash
chmod +x deploy_local.sh
./deploy_local.sh
```

---

## Pipeline GitHub

- `flake8` : vérifie la propreté du code
- `pytest` : s’assure que les tests passent
- Déclenché à chaque commit ou PR sur `main`

---

## Déploiement sur Streamlit Cloud

1. Crée un repo GitHub
2. Upload le projet
3. Va sur [https://streamlit.io/cloud](https://streamlit.io/cloud)
4. Connecte ton GitHub et sélectionne le repo
5. Lance : tout est automatique !

---