
# Streamlit Ping-Pong App – Version Intégrée HTML5 + CI/CD

Ce projet propose :
- Une interface Streamlit simple avec **vrai jeu de ping-pong HTML5 intégré**
- Un pipeline CI/CD via GitHub Actions (tests + lint)
- Un script de lancement local
- Et un déploiement facile sur Streamlit Cloud

## Démo en ligne

[https://app-pingpong-app-ejbn8yq8bzkbc9ntgs4kdi.streamlit.app/](https://app-pingpong-app-ejbn8yq8bzkbc9ntgs4kdi.streamlit.app/)

## Lancer localement

```bash
chmod +x deploy_local.sh
./deploy_local.sh
```

## Fichiers clés

- `app.py` → lance l’app Streamlit avec le jeu intégré
- `game.html` → le vrai jeu HTML5 autonome
- `requirements.txt`, `.github/workflows/ci.yml`, etc.

## Déploiement Cloud

1. Poussez ce projet sur GitHub
2. Allez sur https://streamlit.io/cloud
3. Sélectionnez le repo, branche `main`, fichier `app.py`
4. L’app est en ligne !
