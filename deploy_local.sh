#!/bin/bash
echo "Lancement local de l'application Streamlit"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py