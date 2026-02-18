# Heart Disease UCI Dataset - Informações

## 📊 Visão Geral

- **Nome:** Heart Disease UCI (Cleveland Database)
- **Fonte Original:** UCI Machine Learning Repository
- **URL UCI:** http://archive.ics.uci.edu/ml/datasets/Heart+Disease
- **URL Kaggle:** https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci
- **Licença:** Creative Commons Attribution 4.0 International (CC BY 4.0)

## 📈 Características do Dataset

- **Número de Instâncias:** 303 pacientes
- **Número de Atributos:** 14 variáveis
- **Valores Ausentes:** Sim (6 valores ausentes em 2 colunas: ca e thal)
- **Tipo de Tarefa:** Classificação binária (presença/ausência de doença cardíaca)

## 🏥 Origem dos Dados

Os dados foram coletados de quatro instituições médicas:

1. Cleveland Clinic Foundation (Cleveland, Ohio, USA)
2. Hungarian Institute of Cardiology (Budapest, Hungary)
3. V.A. Medical Center (Long Beach, California, USA)
4. University Hospital (Zurich, Switzerland)

**Nota:** O dataset Cleveland é o mais utilizado em pesquisas de Machine Learning.

## 📋 Descrição das Variáveis

| Variável     | Tipo       | Descrição                                                   | Range/Valores                                                                  |
| ------------ | ---------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **age**      | Numérico   | Idade do paciente em anos                                   | 29-77 anos                                                                     |
| **sex**      | Categórico | Sexo do paciente                                            | 1 = masculino, 0 = feminino                                                    |
| **cp**       | Categórico | Tipo de dor no peito                                        | 1 = angina típica, 2 = angina atípica, 3 = dor não-anginosa, 4 = assintomático |
| **trestbps** | Numérico   | Pressão arterial em repouso (mm Hg)                         | 94-200 mm Hg                                                                   |
| **chol**     | Numérico   | Colesterol sérico (mg/dl)                                   | 126-564 mg/dl                                                                  |
| **fbs**      | Categórico | Glicemia em jejum > 120 mg/dl                               | 1 = verdadeiro, 0 = falso                                                      |
| **restecg**  | Categórico | Resultados eletrocardiográficos em repouso                  | 0 = normal, 1 = anormalidade ST-T, 2 = hipertrofia ventricular                 |
| **thalach**  | Numérico   | Frequência cardíaca máxima alcançada                        | 71-202 bpm                                                                     |
| **exang**    | Categórico | Angina induzida por exercício                               | 1 = sim, 0 = não                                                               |
| **oldpeak**  | Numérico   | Depressão ST induzida por exercício                         | 0.0-6.2                                                                        |
| **slope**    | Categórico | Inclinação do segmento ST de pico                           | 1 = ascendente, 2 = plano, 3 = descendente                                     |
| **ca**       | Numérico   | Número de vasos principais (0-3) coloridos por fluoroscopia | 0-3                                                                            |
| **thal**     | Categórico | Talassemia                                                  | 3 = normal, 6 = defeito fixo, 7 = defeito reversível                           |
| **target**   | Categórico | Diagnóstico de doença cardíaca                              | 0 = ausente, 1 = presente (valores 1-4 convertidos para 1)                     |

## 🎯 Variável Alvo (Target)

- **Original:** Valores de 0 a 4 (0 = sem doença, 1-4 = níveis de doença)
- **Convertido:** Binário (0 = sem doença, 1 = com doença)
- **Distribuição:** 164 pacientes sem doença (54%), 139 com doença (46%)

## 📊 Estatísticas Descritivas

- **Idade média:** 54.4 anos
- **Distribuição por sexo:** 206 homens (68%), 97 mulheres (32%)
- **Valores ausentes:**
  - ca: 4 valores ausentes (1.3%)
  - thal: 2 valores ausentes (0.7%)

## ✅ Adequação para o Projeto CardioIA

Este dataset é ideal para o projeto porque:

1. ✅ **Tamanho adequado:** 303 linhas (> 100 requisito mínimo)
2. ✅ **Variáveis relevantes:** Contém todas as variáveis clínicas obrigatórias (age, sex, trestbps, chol, thalach, target)
3. ✅ **Formato correto:** CSV com dados estruturados
4. ✅ **Fonte confiável:** UCI Machine Learning Repository (referência acadêmica)
5. ✅ **Dados reais:** Coletados de instituições médicas reais
6. ✅ **Anonimizado:** Não contém informações identificáveis (LGPD compliant)
7. ✅ **Bem documentado:** Amplamente usado em pesquisas de ML

## 📚 Referências

- Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J., Sandhu, S., Guppy, K., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. American Journal of Cardiology, 64, 304-310.

- UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/heart+disease

## 📝 Notas de Uso

- Os valores ausentes (?) foram identificados e precisam ser tratados na fase de curadoria
- A variável target foi convertida para binária para simplificar a classificação
- Todas as variáveis numéricas estão em suas unidades originais (não normalizadas)
