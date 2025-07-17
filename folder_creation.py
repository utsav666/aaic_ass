
############ GPT-folder creationg
# import os

# # Define project structure
# structure = {
#     "gpt-api": [
#         "main.py",
#         "Dockerfile",
#         "requirements.txt",
#         "k8s/deployment.yaml",
#         "k8s/service.yaml"
#     ]
# }

# # Sample placeholder content for each file
# files_content = {
#     "main.py": "# FastAPI app code goes here\n",
#     "Dockerfile": "# Dockerfile for GPT API\n",
#     "requirements.txt": "# fastapi\n# uvicorn\n# openai\n",
#     "k8s/deployment.yaml": "# Kubernetes deployment YAML\n",
#     "k8s/service.yaml": "# Kubernetes service YAML\n"
# }

# # Create folders and files
# for root, files in structure.items():
#     for file in files:
#         file_path = os.path.join(root, file)
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         with open(file_path, 'w') as f:
#             f.write(files_content.get(os.path.basename(file), ""))

# print("✅ Project folder structure created successfully under 'gpt-api/'")
##################################################################################


####### ML-flow folder creation########################
import os

ROOT_DIR = "ml_flow_bert"

folders = [
    "data",
    "notebooks",
    "src",
    "models",
    "mlruns",
    "config"
]

files = {
    ".gitignore": "*.pyc\n__pycache__/\nmlruns/",
    "README.md": "# Sentiment Classification using BERT and Keras\n",
    "requirements.txt": "tensorflow\ntransformers\nmlflow\nscikit-learn\npandas\nnumpy\n",
    "config/params.yaml": "batch_size: 32\nepochs: 3\nlearning_rate: 0.0001\nmax_length: 128\n",
    "src/__init__.py": "",
    "src/data_loader.py": "# Load and preprocess data here\n",
    "src/model.py": "# Define Keras BERT model here\n",
    "src/train.py": "# Training logic with MLflow logging\n",
    "src/evaluate.py": "# Evaluation logic\n",
    "src/utils.py": "# Helper utilities\n",
    "run_experiment.py": "# Entrypoint for MLflow training\n"
}

def create_structure():
    # Create root project directory
    os.makedirs(ROOT_DIR, exist_ok=True)

    # Create subfolders
    for folder in folders:
        os.makedirs(os.path.join(ROOT_DIR, folder), exist_ok=True)

    # Create files
    for path, content in files.items():
        full_path = os.path.join(ROOT_DIR, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)

    print(f"✅ MLflow project structure created in ./{ROOT_DIR}/")

if __name__ == "__main__":
    create_structure()

