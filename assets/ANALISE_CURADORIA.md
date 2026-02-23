# 📊 Relatório de Análise e Curadoria de Dados

**Projeto:** CardioIA Fase 1 - FIAP  
**Dataset:** Heart Disease UCI (Cleveland Database)  
**Responsável:** Especialista em IoT e Dados Estruturados  
**Data:** 2024

---

## 🎯 Objetivo da Curadoria

Limpar e validar o dataset cardiovascular para garantir qualidade e integridade dos dados antes do treinamento de modelos de IA.

---

## 📋 Resumo Executivo

| Métrica                       | Valor           |
| ----------------------------- | --------------- |
| **Linhas originais**          | 303             |
| **Linhas após curadoria**     | 303             |
| **Linhas removidas**          | 0               |
| **Taxa de retenção**          | 100%            |
| **Valores ausentes tratados** | 6 (2% do total) |
| **Duplicatas removidas**      | 0               |
| **Outliers removidos**        | 0               |

✅ **Resultado:** Dataset de alta qualidade, pronto para uso em Machine Learning.

---

## 🔍 Análise do Dataset Bruto

### Dimensões

- **Linhas:** 303 pacientes
- **Colunas:** 14 variáveis clínicas
- **Tipo:** Dados tabulares estruturados

### Valores Ausentes Identificados

| Coluna                          | Valores Ausentes | Percentual |
| ------------------------------- | ---------------- | ---------- |
| **ca** (vasos por fluoroscopia) | 4                | 1.32%      |
| **thal** (perfusão miocárdica)  | 2                | 0.66%      |
| **Total**                       | 6                | 0.99%      |

**Análise:** Apenas 6 valores ausentes em 4.242 células (303 linhas × 14 colunas), representando menos de 1% dos dados. Excelente qualidade!

### Duplicatas

- **Total encontrado:** 0 linhas duplicadas
- **Ação:** Nenhuma remoção necessária

---

## 🔧 Processos de Curadoria Aplicados

### 1. Remoção de Duplicatas ✅

- **Método:** `drop_duplicates()`
- **Resultado:** 0 duplicatas encontradas
- **Impacto:** Nenhuma linha removida

### 2. Tratamento de Valores Ausentes ✅

#### Coluna `ca` (Número de Vasos)

- **Valores ausentes:** 4
- **Estratégia:** Imputação pela mediana
- **Valor imputado:** 0.00 (mediana)
- **Justificativa:** A mediana é robusta a outliers e representa o valor mais comum (0 vasos obstruídos)

#### Coluna `thal` (Perfusão Miocárdica)

- **Valores ausentes:** 2
- **Estratégia:** Imputação pela mediana
- **Valor imputado:** 3.00 (normal)
- **Justificativa:** Valor 3 representa perfusão normal, o mais frequente no dataset

### 3. Validação de Ranges ✅

Todos os valores estão dentro dos ranges clinicamente válidos:

| Variável     | Range Válido  | Valores no Dataset | Status    |
| ------------ | ------------- | ------------------ | --------- |
| **age**      | 0-120 anos    | 29-77 anos         | ✅ Válido |
| **trestbps** | 50-250 mm Hg  | 94-200 mm Hg       | ✅ Válido |
| **chol**     | 100-600 mg/dl | 126-564 mg/dl      | ✅ Válido |
| **thalach**  | 50-220 bpm    | 71-202 bpm         | ✅ Válido |

**Resultado:** Nenhum outlier extremo ou erro de digitação detectado.

### 4. Validação de Tamanho Mínimo ✅

- **Requisito:** Mínimo 100 linhas
- **Dataset curado:** 303 linhas
- **Status:** ✅ Aprovado (203% acima do mínimo)

---

## 📈 Estatísticas Descritivas do Dataset Curado

### Variáveis Demográficas

| Variável  | Média     | Desvio Padrão | Mín | Máx |
| --------- | --------- | ------------- | --- | --- |
| **Idade** | 54.4 anos | 9.0 anos      | 29  | 77  |

**Interpretação:** Amostra representa adultos e idosos, com boa distribuição etária.

### Variáveis Clínicas - Sinais Vitais

| Variável               | Média       | Desvio Padrão | Mín | Máx | Referência Normal |
| ---------------------- | ----------- | ------------- | --- | --- | ----------------- |
| **Pressão Arterial**   | 131.7 mm Hg | 17.6          | 94  | 200 | <120 mm Hg        |
| **Freq. Cardíaca Máx** | 149.6 bpm   | 22.9          | 71  | 202 | 220 - idade       |

**Interpretação:**

- Pressão média de 131.7 indica que muitos pacientes têm hipertensão leve (>120)
- Frequência cardíaca máxima dentro do esperado para testes de esforço

### Variáveis Laboratoriais

| Variável       | Média       | Desvio Padrão | Mín | Máx | Referência Normal |
| -------------- | ----------- | ------------- | --- | --- | ----------------- |
| **Colesterol** | 246.7 mg/dl | 51.8          | 126 | 564 | <200 mg/dl        |

**Interpretação:** Colesterol médio de 246.7 está acima do ideal (<200), indicando risco cardiovascular elevado na amostra.

### Distribuição da Variável Alvo (Target)

| Categoria          | Quantidade | Percentual |
| ------------------ | ---------- | ---------- |
| **Sem doença (0)** | 164        | 54.1%      |
| **Com doença (1)** | 139        | 45.9%      |

**Interpretação:**

- Dataset **balanceado** (proporção próxima de 50/50)
- Excelente para treinamento de modelos de classificação
- Não requer técnicas de balanceamento (SMOTE, undersampling)

---

## 🎯 Qualidade dos Dados

### Pontos Fortes ✅

1. **Alta Completude:** 99% dos dados presentes (apenas 6 valores ausentes)
2. **Sem Duplicatas:** Nenhuma linha duplicada
3. **Ranges Válidos:** Todos os valores dentro de limites clínicos aceitáveis
4. **Tamanho Adequado:** 303 linhas (3x o mínimo requerido)
5. **Balanceamento:** Distribuição equilibrada entre classes (54% vs 46%)
6. **Diversidade:** Ambos os sexos representados (68% M, 32% F)
7. **Faixa Etária Ampla:** 29-77 anos (48 anos de amplitude)

### Limitações Identificadas ⚠️

1. **Valores Ausentes:** 6 valores em 2 colunas (ca, thal)
   - **Impacto:** Mínimo (< 1% dos dados)
   - **Mitigação:** Imputação pela mediana aplicada

2. **Desbalanceamento de Sexo:** 68% masculino vs 32% feminino
   - **Impacto:** Moderado - modelo pode ter viés para homens
   - **Mitigação:** Documentar limitação; considerar pesos de classe

3. **Amostra Única:** Dados apenas de 4 instituições
   - **Impacto:** Pode não generalizar para outras populações
   - **Mitigação:** Documentar origem; validar em dados externos

---

## 🧪 Validações de Integridade

### ✅ Checklist de Qualidade

- [x] Todas as 14 colunas obrigatórias presentes
- [x] Nenhum valor ausente após tratamento
- [x] Nenhuma duplicata
- [x] Todos os valores dentro de ranges válidos
- [x] Tamanho mínimo atingido (303 > 100)
- [x] Tipos de dados corretos (numéricos e categóricos)
- [x] Variável target presente e válida
- [x] Dataset balanceado (45.9% vs 54.1%)

---

## 💾 Arquivos Gerados

| Arquivo                     | Descrição                | Linhas | Status         |
| --------------------------- | ------------------------ | ------ | -------------- |
| `heart_disease_raw.csv`     | Dataset original baixado | 303    | ✅ Preservado  |
| `heart_disease_curated.csv` | Dataset após curadoria   | 303    | ✅ Gerado      |
| `curate_data.py`            | Script de curadoria      | -      | ✅ Documentado |
| `ANALISE_CURADORIA.md`      | Este relatório           | -      | ✅ Completo    |

---

## 🎓 Conclusões e Recomendações

### Conclusões

1. **Dataset de Alta Qualidade:** O Heart Disease UCI é um dataset excepcionalmente limpo e bem estruturado
2. **Pronto para ML:** Não requer limpeza adicional; pode ser usado diretamente para treinamento
3. **Curadoria Mínima:** Apenas 6 valores imputados; nenhuma linha removida
4. **Conformidade:** Atende todos os requisitos do projeto CardioIA Fase 1

### Recomendações para Uso em IA

1. **Normalização:** Considerar normalização/padronização das variáveis numéricas antes do treinamento
2. **Encoding:** Converter variáveis categóricas (cp, restecg, slope, thal) para one-hot encoding
3. **Feature Engineering:** Criar features derivadas (ex: IMC se peso/altura estivessem disponíveis)
4. **Validação Cruzada:** Usar k-fold cross-validation para avaliar modelos
5. **Métricas Balanceadas:** Usar F1-score, ROC-AUC além de acurácia
6. **Interpretabilidade:** Usar SHAP ou LIME para explicar predições

### Próximos Passos

1. ✅ Curadoria concluída
2. ⏭️ Hospedar dataset no Google Drive
3. ⏭️ Adicionar link público no README
4. ⏭️ Implementar testes de validação
5. ⏭️ Treinar modelos de classificação (opcional)

---

## 📚 Referências

- **Dataset Original:** UCI Machine Learning Repository
- **Método de Imputação:** Mediana (robusto a outliers)
- **Validação de Ranges:** Baseado em guidelines clínicos cardiovasculares
- **Ferramentas:** Python 3.x, Pandas, NumPy

---

**Relatório gerado automaticamente pelo script de curadoria**  
**Projeto CardioIA - FIAP 2024**
