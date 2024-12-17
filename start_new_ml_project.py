import os

# Project Structure
PROJECT_STRUCTURE = {
    "data": ["raw", "processed", "features"],  # These are directories
    "output": ["ensemble", "evaluation", "metrics", "models", "optimization", "plots", "predictions"],  # These are directories
    "scripts": [  # These are files
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
    "tests": ["initial_test.py"],  # This contains files
    "streamlit_app": ["app.py"],  # This contains files
    "root_files": {
        ".gitignore": """# Virtual Environment
venv/
.env
*.log
output/
__pycache__/
*.tmp
""",
        "requirements.txt": """# Libraries for data manipulation and analysis
pandas           # Manipulate structured data in DataFrames.
numpy            # Efficient numerical computation with multidimensional arrays.
scipy            # Scientific operations and advanced mathematical optimization.

# Libraries for Machine Learning and analysis
scikit-learn     # Machine Learning algorithms: classification, regression, and clustering.
joblib           # Save and load ML models; parallel processing.
xgboost          # Optimized gradient boosting library.
lightgbm         # Fast gradient boosting for large datasets.
catboost         # Gradient boosting with automatic handling for categorical features.

# Visualization Libraries
matplotlib       # Create static and customizable charts.
seaborn          # Advanced statistical charts with simple syntax.
plotly           # Interactive and 3D data visualizations.
altair           # Declarative visualizations based on JSON and Vega.
streamlit        # Quickly build interactive dashboards and web applications.

# Libraries for data validation and processing
jsonschema       # Validate JSON files against schemas.
pydantic         # Data validation using Python models.

# Libraries for advanced integrations
requests         # Manage HTTP requests for APIs.
flask            # Lightweight framework for creating REST APIs.
sqlalchemy       # ORM to manage relational databases.
pymysql          # Driver to connect Python applications to MySQL databases.

# Libraries for automation and performance
openpyxl         # Read and write Excel files.
watchdog         # Automatically monitor file and folder changes.
psutil           # Monitor system performance (CPU, memory, etc.).

# Libraries for environment management
python-dotenv    # Load environment variables from .env files.
""",
        "readme.md": """# Data Science Project

## Structure
- **data/**: Contains raw, processed, and feature-extracted data.
- **scripts/**: Includes main scripts for EDA, preprocessing, and training.
- **output/**: Trained models, predictions, and visualizations.
- **tests/**: Contains test scripts for initial validation.
"""
    }
}

# Define which folders should contain subdirectories instead of files
DIRECTORY_FOLDERS = {
    "data": True,
    "output": True,
    "scripts": False,
    "tests": False,
    "streamlit_app": False
}

def create_project_structure(project_name, base_path="C:\\Users\\utente"):
    """
    Creates a structured directory for a data science project.

    Args:
        project_name (str): The name of the project.
        base_path (str): The root directory where the project will be created.
    """
    project_path = os.path.join(base_path, project_name)
    print(f"Creating project '{project_name}' in directory '{base_path}'...\n")
    
    try:
        # Create main project directory
        os.makedirs(project_path, exist_ok=True)

        # Create directories and files
        for folder, items in PROJECT_STRUCTURE.items():
            if folder == "root_files":
                # Create root files
                for file_name, content in items.items():
                    file_path = os.path.join(project_path, file_name)
                    with open(file_path, "w", encoding='utf-8') as f:
                        f.write(content)
                    print(f"Created file: {file_name}")
            else:
                # Create main folder
                folder_path = os.path.join(project_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                print(f"Created directory: {folder}")

                # Process items based on whether they should be directories or files
                for item in items:
                    item_path = os.path.join(folder_path, item)
                    if DIRECTORY_FOLDERS.get(folder, False):
                        # Create as directory
                        os.makedirs(item_path, exist_ok=True)
                        # Add .gitkeep to keep empty directory in git
                        with open(os.path.join(item_path, '.gitkeep'), 'w') as f:
                            pass
                        print(f"Created subdirectory: {folder}/{item}")
                    else:
                        # Create as file
                        with open(item_path, "w", encoding='utf-8') as f:
                            pass
                        print(f"Created file: {folder}/{item}")

        print(f"\n✅ Project '{project_name}' created successfully!")
        print(f"📂 Navigate to the project folder with: cd {project_path}")

    except Exception as e:
        print(f"❌ Error creating project structure: {str(e)}")

if __name__ == "__main__":
    project_name = input("Enter the project name: ").strip()
    if project_name:
        create_project_structure(project_name)
    else:
        print("❌ Invalid project name!")