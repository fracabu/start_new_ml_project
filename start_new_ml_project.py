import os

# Struttura del progetto
PROJECT_STRUCTURE = {
    "data": ["raw", "processed", "features"],
    "output": ["ensemble", "evaluation", "metrics", "models", "optimization", "plots", "predictions"],
    "scripts": [
        "01_generate_dataset.py",
        "02_data_analysis.py",
        "03_feature_engineering.py",
        "04_model_training.py",
        "05_predict.py",
        "06_generate_test_data.py",
        "06_visualization.py",
        "07_model_evaluation.py",
        "08_model_optimization.py",
        "09_ensemble_tuning.py",
        "10_hybrid_detector.py",
        "11_alert_system.py",
        "12_api_service.py",
    ],
    "tests": ["initial_test.py"],
    "streamlit_app": ["app.py"],
    "root_files": {
        ".gitignore": """# Ambiente Virtuale
venv/
.env
*.log
output/
__pycache__/
*.tmp
""",
        "requirements.txt": """# Librerie per la manipolazione e analisi dei dati
pandas           # Manipolazione di dati strutturati in DataFrame.
numpy            # Calcolo numerico efficiente con array multidimensionali.
scipy            # Operazioni scientifiche e ottimizzazioni matematiche avanzate.

# Librerie per il Machine Learning e l'analisi
scikit-learn     # Algoritmi di Machine Learning: classificazione, regressione e clustering.
joblib           # Salvataggio e caricamento di modelli ML e parallelizzazione.
xgboost          # Libreria ottimizzata per gradient boosting.
lightgbm         # Algoritmo rapido per il boosting su dataset grandi.
catboost         # Gradient boosting con supporto automatico per variabili categoriche.

# Librerie per visualizzazioni
matplotlib       # Creazione di grafici statici e personalizzati.
seaborn          # Grafici statistici avanzati con una sintassi semplice.
plotly           # Grafici interattivi e 3D per esplorazione dei dati.
altair           # Visualizzazioni dichiarative basate su JSON e Vega.
streamlit        # Creazione rapida di dashboard e applicazioni web interattive.

# Librerie per elaborazione e validazione
jsonschema       # Validazione di file JSON basati su schema.
pydantic         # Validazione dei dati con modelli Python.

# Librerie per integrazioni avanzate
requests         # Gestione di chiamate HTTP per API.
flask            # Framework leggero per creare API REST.
sqlalchemy       # ORM per la gestione di database relazionali.
pymysql          # Driver per connettere applicazioni Python a MySQL.

# Librerie per automazione e performance
openpyxl         # Lettura e scrittura di file Excel.
watchdog         # Monitoraggio automatico di file e cartelle.
psutil           # Monitoraggio delle performance del sistema.

# Librerie per la gestione di file e interfacce
python-dotenv    # Caricamento delle variabili di ambiente da file .env.
""",
        "readme.md": """# Progetto Data Science

## Struttura
- **data/**: Contiene i dati grezzi, processati e features.
- **scripts/**: Contiene gli script principali per EDA, preprocessing e training.
- **output/**: Modelli addestrati, predizioni e grafici.
- **tests/**: File di test iniziali.
"""
    }
}

def create_project_structure(project_name, base_path="C:\\Users\\utente"):
    project_path = os.path.join(base_path, project_name)
    print(f"Creazione del progetto '{project_name}' nella directory '{base_path}'...\n")
    
    os.makedirs(project_path, exist_ok=True)

    # Creazione delle cartelle e file
    for folder, items in PROJECT_STRUCTURE.items():
        if folder == "root_files":
            for file_name, content in items.items():
                with open(os.path.join(project_path, file_name), "w") as f:
                    f.write(content)
        else:
            folder_path = os.path.join(project_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            for item in items:
                open(os.path.join(folder_path, item), "w").close()

    print(f"✅ Progetto '{project_name}' creato con successo!")
    print(f"📂 Vai nella cartella del progetto con: cd {project_path}")

if __name__ == "__main__":
    project_name = input("Inserisci il nome del progetto: ").strip()
    if project_name:
        create_project_structure(project_name)
    else:
        print("❌ Nome del progetto non valido!")
