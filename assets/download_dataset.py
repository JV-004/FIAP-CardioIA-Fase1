"""
Script para baixar o Heart Disease UCI Dataset
Fonte: UCI Machine Learning Repository
URL: http://archive.ics.uci.edu/ml/datasets/Heart+Disease
"""

import pandas as pd
import urllib.request

# URL do dataset Cleveland (o mais usado em pesquisas)
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

# Nomes das colunas conforme documentação UCI
column_names = [
    'age',        # idade em anos
    'sex',        # sexo (1 = masculino; 0 = feminino)
    'cp',         # tipo de dor no peito (1-4)
    'trestbps',   # pressão arterial em repouso (mm Hg)
    'chol',       # colesterol sérico (mg/dl)
    'fbs',        # glicemia em jejum > 120 mg/dl (1 = true; 0 = false)
    'restecg',    # resultados eletrocardiográficos em repouso (0-2)
    'thalach',    # frequência cardíaca máxima alcançada
    'exang',      # angina induzida por exercício (1 = sim; 0 = não)
    'oldpeak',    # depressão ST induzida por exercício
    'slope',      # inclinação do segmento ST de pico do exercício (1-3)
    'ca',         # número de vasos principais coloridos por fluoroscopia (0-3)
    'thal',       # 3 = normal; 6 = defeito fixo; 7 = defeito reversível
    # diagnóstico de doença cardíaca (0 = ausente, 1-4 = presente)
    'target'
]

print("Baixando dataset Heart Disease UCI...")
print(f"Fonte: {url}")

try:
    # Baixar o dataset
    df = pd.read_csv(url, names=column_names, na_values='?')

    # Informações sobre o dataset
    print(f"\n✅ Dataset baixado com sucesso!")
    print(f"📊 Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas")
    print(f"📋 Colunas: {', '.join(df.columns.tolist())}")
    print(f"\n🔍 Valores ausentes por coluna:")
    print(df.isnull().sum())

    # Converter target para binário (0 = sem doença, 1 = com doença)
    df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

    # Salvar como CSV
    output_file = "heart_disease_raw.csv"
    df.to_csv(output_file, index=False)
    print(f"\n💾 Dataset salvo como: {output_file}")

    # Estatísticas básicas
    print(f"\n📈 Estatísticas básicas:")
    print(f"   - Idade média: {df['age'].mean():.1f} anos")
    print(f"   - Sexo: {df['sex'].value_counts().to_dict()}")
    print(f"   - Target: {df['target'].value_counts().to_dict()}")

except Exception as e:
    print(f"❌ Erro ao baixar dataset: {e}")
    print("\nAlternativa: Baixe manualmente de:")
    print("https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci")
