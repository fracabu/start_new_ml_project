# 🛠️ **ML Project Generator con Supporto Streamlit**  

![ML Project Generator](/A_vintage-style_cartoon_illustration_with_a_nerdy_.jpeg)

Questo script Python **genera una struttura completa per progetti di Machine Learning** in pochi secondi.  
Include **cartelle organizzate**, script vuoti pronti all'uso e un file `requirements.txt` dettagliato per velocizzare l'avvio di nuovi progetti.

🔎 **Ideale per progetti di Data Science**: esplora i dati, addestra modelli e visualizza i risultati con **Streamlit**.

---

## **📂 Struttura Generata**

Esempio della struttura del progetto:

```
<nome_progetto>/
│
├── data/
│   ├── raw/          # Dati grezzi
│   ├── processed/    # Dati pre-processati
│   └── features/     # Features estratte
│
├── output/
│   ├── models/       # Modelli salvati
│   ├── predictions/  # Predizioni salvate
│   ├── evaluation/   # Metriche di valutazione
│   └── plots/        # Grafici generati
│
├── scripts/
│   ├── 01_generate_dataset.py      # Generazione dati
│   ├── 02_data_analysis.py         # Analisi esplorativa (EDA)
│   ├── 03_feature_engineering.py   # Ingegnerizzazione delle feature
│   ├── 04_model_training.py        # Training del modello
│   ├── 05_predict.py               # Predizioni preliminari
│   ├── 06_visualization.py         # Visualizzazione iniziale (Streamlit)
│   ├── 07_model_evaluation.py      # Valutazione del modello
│   ├── 08_model_optimization.py    # Ottimizzazione iperparametri
│   ├── 09_ensemble_tuning.py       # Modelli ensemble
│   ├── 10_hybrid_detector.py       # Detector ibrido
│   ├── 11_alert_system.py          # Sistema di alert
│   └── 12_api_service.py           # Servizio API per il deploy
│
├── streamlit_app/
│   └── app.py        # Dashboard interattiva con Streamlit
│
├── tests/
│   └── initial_test.py
│
├── .gitignore         # Regole per file ignorati da Git
├── requirements.txt   # Dipendenze dettagliate
└── readme.md          # Documentazione base del progetto
```

---

## **🆕 Changelog e Miglioramenti**

### Versione 1.1.0 (Dicembre 2024)

**🐛 Bug Fix:**
- Risolto il problema critico della creazione errata delle sottocartelle
- Corretta la generazione delle directory in `data/` e `output/` che venivano create come file invece di cartelle
- Aggiunto il supporto per `.gitkeep` nelle cartelle vuote

**✨ Nuove Funzionalità:**
- Implementato sistema di logging dettagliato durante la creazione del progetto
- Aggiunta gestione errori robusta con messaggi informativi
- Supporto UTF-8 esplicito per la creazione dei file
- Distinzione automatica tra file e cartelle durante la generazione

**🔧 Miglioramenti Tecnici:**
- Ottimizzata la logica di creazione delle directory
- Aggiunto dizionario `DIRECTORY_FOLDERS` per una migliore gestione della struttura
- Migliorato il feedback visuale durante la creazione del progetto
- Implementata validazione del nome del progetto

---

## **🔧 Come Usarlo**

1. **Scarica lo script** `start_new_project.py`.  
2. **Esegui lo script**:  
   ```bash
   python start_new_project.py
   ```  
3. **Inserisci il nome del progetto** quando richiesto:  
   ```plaintext
   Inserisci il nome del progetto: ml_pipeline_example
   ```  
4. La struttura del progetto sarà generata nella directory specificata.  

---

## **🚀 Fasi di Lavoro**

1. **Preparazione dei dati**  
   Utilizza i primi **cinque script** per:  
   - Generare i dati grezzi (`01_generate_dataset.py`)  
   - Analizzare i dati (`02_data_analysis.py`)  
   - Creare feature (`03_feature_engineering.py`)  

2. **Visualizzazione rapida con Streamlit**  
   Lo script **`06_visualization.py`** può essere lanciato con **Streamlit** per visualizzare i dati rapidamente:  
   ```bash
   streamlit run scripts/06_visualization.py
   ```  
   **Risultato**: Dashboard interattiva per esplorare statistiche e grafici.

3. **Training e Valutazione del Modello**  
   - Addestra il modello con **`04_model_training.py`**.  
   - Valuta le performance con **`07_model_evaluation.py`**.

4. **Dashboard Finale**  
   Utilizza lo script **`streamlit_app/app.py`** per lanciare la tua dashboard finale:  
   ```bash
   streamlit run streamlit_app/app.py
   ```

---

## **📝 File `requirements.txt`**

Le dipendenze sono organizzate in sezioni per chiarezza. Ecco un esempio:  

```plaintext
# Librerie per manipolazione dei dati
pandas
numpy
scipy

# Librerie per Machine Learning
scikit-learn
joblib
xgboost
lightgbm
catboost

# Librerie per visualizzazioni
matplotlib
seaborn
plotly
altair
streamlit

# Altre librerie utili
jsonschema
pydantic
requests
flask
sqlalchemy
pymysql
openpyxl
watchdog
psutil
python-dotenv
```

---

## **🔑 Perché Usarlo?**

- **Organizzazione chiara**: Tutte le fasi del ciclo ML hanno script dedicati.  
- **Visualizzazione immediata**: Integra **Streamlit** per una dashboard rapida.  
- **File `requirements.txt` completo**: Dipendenze pronte all'uso per installazione rapida.
- **Affidabilità migliorata**: Bug fix critici e gestione errori robusta
- **Feedback dettagliato**: Logging completo durante la creazione del progetto
- **Gestione Git ottimizzata**: Supporto per cartelle vuote con `.gitkeep`

---

## **📚 Risorse Utili**

- [Streamlit Documentation](https://docs.streamlit.io)  
- [Scikit-Learn Quickstart](https://scikit-learn.org/stable/getting_started.html)  
- [Pandas Documentation](https://pandas.pydata.org/docs/getting_started/index.html)  

--- 

Se vuoi provarlo o dare un'occhiata, fammelo sapere!  
su [LinkedIn](https://www.linkedin.com/in/francesco-~-capurso-5801031a9/) per discutere o condividere idee.
**Ogni contributo è benvenuto.** 💡  

---