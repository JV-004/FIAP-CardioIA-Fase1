"""
Script de Curadoria de Dados - Heart Disease UCI Dataset
Responsável: Especialista em IoT e Dados Estruturados
Projeto: CardioIA Fase 1 - FIAP

Este script realiza a limpeza e validação do dataset cardiovascular.
"""

import pandas as pd
import numpy as np
import os


def load_dataset(filepath):
    """Carrega o dataset bruto"""
    print("=" * 70)
    print("📂 CARREGANDO DATASET")
    print("=" * 70)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    df = pd.read_csv(filepath)
    print(f"✅ Dataset carregado: {df.shape[0]} linhas x {df.shape[1]} colunas")
    return df


def analyze_raw_data(df):
    """Analisa o dataset bruto antes da limpeza"""
    print("\n" + "=" * 70)
    print("🔍 ANÁLISE DO DATASET BRUTO")
    print("=" * 70)

    print(f"\n📊 Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas")

    print("\n📋 Colunas:")
    print(df.columns.tolist())

    print("\n❓ Valores ausentes por coluna:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    missing_df = pd.DataFrame({
        'Valores Ausentes': missing,
        'Percentual (%)': missing_pct
    })
    print(missing_df[missing_df['Valores Ausentes'] > 0])

    print("\n🔢 Duplicatas:")
    duplicates = df.duplicated().sum()
    print(f"   Total de linhas duplicadas: {duplicates}")

    print("\n📈 Estatísticas descritivas (variáveis numéricas):")
    print(df.describe().round(2))

    print("\n🎯 Distribuição da variável target:")
    print(df['target'].value_counts())
    print(
        f"   Percentual com doença: {(df['target'].sum() / len(df) * 100):.1f}%")


def remove_duplicates(df):
    """Remove linhas duplicadas"""
    print("\n" + "=" * 70)
    print("🧹 REMOVENDO DUPLICATAS")
    print("=" * 70)

    initial_rows = len(df)
    df_clean = df.drop_duplicates()
    removed = initial_rows - len(df_clean)

    print(f"   Linhas removidas: {removed}")
    print(f"   Linhas restantes: {len(df_clean)}")

    return df_clean


def handle_missing_values(df):
    """Trata valores ausentes"""
    print("\n" + "=" * 70)
    print("🔧 TRATANDO VALORES AUSENTES")
    print("=" * 70)

    df_clean = df.copy()

    # Identificar colunas com valores ausentes
    missing_cols = df_clean.columns[df_clean.isnull().any()].tolist()

    if not missing_cols:
        print("   ✅ Nenhum valor ausente encontrado!")
        return df_clean

    print(f"\n   Colunas com valores ausentes: {missing_cols}")

    for col in missing_cols:
        missing_count = df_clean[col].isnull().sum()
        print(f"\n   📌 Coluna '{col}': {missing_count} valores ausentes")

        # Estratégia: imputação pela mediana para variáveis numéricas
        if df_clean[col].dtype in ['int64', 'float64']:
            median_value = df_clean[col].median()
            df_clean[col].fillna(median_value, inplace=True)
            print(f"      ✅ Imputados com mediana: {median_value:.2f}")
        else:
            # Para categóricas, usar moda
            mode_value = df_clean[col].mode()[0]
            df_clean[col].fillna(mode_value, inplace=True)
            print(f"      ✅ Imputados com moda: {mode_value}")

    return df_clean


def validate_ranges(df):
    """Valida ranges das variáveis e remove outliers extremos"""
    print("\n" + "=" * 70)
    print("✅ VALIDANDO RANGES")
    print("=" * 70)

    df_clean = df.copy()
    initial_rows = len(df_clean)

    # Definir ranges válidos baseados em conhecimento médico
    validations = {
        'age': (0, 120, 'anos'),
        'trestbps': (50, 250, 'mm Hg'),  # Pressão arterial
        'chol': (100, 600, 'mg/dl'),     # Colesterol
        'thalach': (50, 220, 'bpm')      # Frequência cardíaca
    }

    rows_removed = 0

    for col, (min_val, max_val, unit) in validations.items():
        if col in df_clean.columns:
            invalid_mask = (df_clean[col] < min_val) | (
                df_clean[col] > max_val)
            invalid_count = invalid_mask.sum()

            if invalid_count > 0:
                print(
                    f"\n   ⚠️  '{col}': {invalid_count} valores fora do range [{min_val}-{max_val} {unit}]")
                print(
                    f"      Valores inválidos: {df_clean.loc[invalid_mask, col].tolist()}")
                df_clean = df_clean[~invalid_mask]
                rows_removed += invalid_count
            else:
                print(
                    f"   ✅ '{col}': Todos os valores dentro do range [{min_val}-{max_val} {unit}]")

    final_rows = len(df_clean)
    print(f"\n   📊 Total de linhas removidas: {rows_removed}")
    print(f"   📊 Linhas restantes: {final_rows}")

    return df_clean


def validate_minimum_size(df, min_rows=100):
    """Valida se o dataset tem o tamanho mínimo necessário"""
    print("\n" + "=" * 70)
    print("📏 VALIDANDO TAMANHO MÍNIMO")
    print("=" * 70)

    current_rows = len(df)
    print(f"   Linhas atuais: {current_rows}")
    print(f"   Mínimo requerido: {min_rows}")

    if current_rows < min_rows:
        raise ValueError(
            f"❌ Dataset insuficiente! Apenas {current_rows} linhas (mínimo: {min_rows})")

    print(
        f"   ✅ Dataset válido! {current_rows} linhas (>{min_rows} requerido)")
    return True


def generate_curation_report(df_original, df_curated):
    """Gera relatório de curadoria"""
    print("\n" + "=" * 70)
    print("📋 RELATÓRIO DE CURADORIA")
    print("=" * 70)

    print(f"\n📊 Resumo:")
    print(f"   Linhas originais: {len(df_original)}")
    print(f"   Linhas após curadoria: {len(df_curated)}")
    print(f"   Linhas removidas: {len(df_original) - len(df_curated)}")
    print(
        f"   Taxa de retenção: {(len(df_curated) / len(df_original) * 100):.1f}%")

    print(f"\n✅ Validações realizadas:")
    print(f"   ✓ Remoção de duplicatas")
    print(f"   ✓ Tratamento de valores ausentes")
    print(f"   ✓ Validação de ranges (idade, pressão, colesterol, freq. cardíaca)")
    print(f"   ✓ Verificação de tamanho mínimo (100 linhas)")

    print(f"\n📈 Estatísticas finais:")
    print(f"   Idade média: {df_curated['age'].mean():.1f} anos")
    print(f"   Pressão média: {df_curated['trestbps'].mean():.1f} mm Hg")
    print(f"   Colesterol médio: {df_curated['chol'].mean():.1f} mg/dl")
    print(f"   Freq. cardíaca média: {df_curated['thalach'].mean():.1f} bpm")

    print(f"\n🎯 Distribuição target:")
    target_counts = df_curated['target'].value_counts()
    print(
        f"   Sem doença (0): {target_counts[0]} ({target_counts[0]/len(df_curated)*100:.1f}%)")
    print(
        f"   Com doença (1): {target_counts[1]} ({target_counts[1]/len(df_curated)*100:.1f}%)")


def curate_dataset(input_file, output_file):
    """Função principal de curadoria"""
    print("\n" + "🩺" * 35)
    print("CURADORIA DE DADOS - CARDIO IA")
    print("🩺" * 35)

    # 1. Carregar dataset
    df_original = load_dataset(input_file)

    # 2. Análise inicial
    analyze_raw_data(df_original)

    # 3. Remover duplicatas
    df_clean = remove_duplicates(df_original)

    # 4. Tratar valores ausentes
    df_clean = handle_missing_values(df_clean)

    # 5. Validar ranges
    df_clean = validate_ranges(df_clean)

    # 6. Validar tamanho mínimo
    validate_minimum_size(df_clean, min_rows=100)

    # 7. Gerar relatório
    generate_curation_report(df_original, df_clean)

    # 8. Salvar dataset curado
    print("\n" + "=" * 70)
    print("💾 SALVANDO DATASET CURADO")
    print("=" * 70)
    df_clean.to_csv(output_file, index=False)
    print(f"   ✅ Dataset salvo: {output_file}")
    print(
        f"   📊 Dimensões finais: {df_clean.shape[0]} linhas x {df_clean.shape[1]} colunas")

    print("\n" + "🎉" * 35)
    print("CURADORIA CONCLUÍDA COM SUCESSO!")
    print("🎉" * 35 + "\n")

    return df_clean


if __name__ == "__main__":
    # Executar curadoria
    input_file = "heart_disease_raw.csv"
    output_file = "heart_disease_curated.csv"

    try:
        df_curated = curate_dataset(input_file, output_file)
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        raise
