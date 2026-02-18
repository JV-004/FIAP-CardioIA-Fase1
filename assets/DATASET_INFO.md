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

### Variáveis Demográficas

#### **age** (Numérico)

- **Descrição:** Idade do paciente em anos
- **Range:** 29-77 anos
- **Tipo:** Contínuo

#### **sex** (Categórico)

- **Descrição:** Sexo biológico do paciente
- **Valores:**
  - `1` = Masculino
  - `0` = Feminino
- **Tipo:** Binário

---

### Variáveis Clínicas - Sintomas

#### **cp** (Categórico)

- **Descrição:** Tipo de dor no peito (chest pain)
- **Valores:**
  - `1` = Angina típica
  - `2` = Angina atípica
  - `3` = Dor não-anginosa
  - `4` = Assintomático
- **Tipo:** Ordinal

#### **exang** (Categórico)

- **Descrição:** Angina induzida por exercício
- **Valores:**
  - `1` = Sim
  - `0` = Não
- **Tipo:** Binário

---

### Variáveis Clínicas - Sinais Vitais

#### **trestbps** (Numérico)

- **Descrição:** Pressão arterial em repouso (resting blood pressure)
- **Unidade:** mm Hg (milímetros de mercúrio)
- **Range:** 94-200 mm Hg
- **Tipo:** Contínuo

#### **thalach** (Numérico)

- **Descrição:** Frequência cardíaca máxima alcançada durante teste de esforço
- **Unidade:** bpm (batimentos por minuto)
- **Range:** 71-202 bpm
- **Tipo:** Contínuo

---

### Variáveis Laboratoriais

#### **chol** (Numérico)

- **Descrição:** Colesterol sérico total
- **Unidade:** mg/dl (miligramas por decilitro)
- **Range:** 126-564 mg/dl
- **Tipo:** Contínuo

#### **fbs** (Categórico)

- **Descrição:** Glicemia em jejum > 120 mg/dl (fasting blood sugar)
- **Valores:**
  - `1` = Verdadeiro (glicemia > 120 mg/dl)
  - `0` = Falso (glicemia ≤ 120 mg/dl)
- **Tipo:** Binário

---

### Variáveis Eletrocardiográficas (ECG)

#### **restecg** (Categórico)

- **Descrição:** Resultados do eletrocardiograma em repouso
- **Valores:**
  - `0` = Normal
  - `1` = Anormalidade da onda ST-T (inversão da onda T e/ou elevação/depressão ST > 0.05 mV)
  - `2` = Hipertrofia ventricular esquerda provável ou definitiva (critérios de Estes)
- **Tipo:** Ordinal

#### **oldpeak** (Numérico)

- **Descrição:** Depressão do segmento ST induzida por exercício em relação ao repouso
- **Unidade:** mm (milímetros)
- **Range:** 0.0-6.2 mm
- **Tipo:** Contínuo

#### **slope** (Categórico)

- **Descrição:** Inclinação do segmento ST no pico do exercício
- **Valores:**
  - `1` = Ascendente (upsloping)
  - `2` = Plano (flat)
  - `3` = Descendente (downsloping)
- **Tipo:** Ordinal

---

### Variáveis de Imagem Cardiovascular

#### **ca** (Numérico)

- **Descrição:** Número de vasos principais coloridos por fluoroscopia
- **Range:** 0-3 vasos
- **Tipo:** Discreto
- **Nota:** 4 valores ausentes (1.3%)

#### **thal** (Categórico)

- **Descrição:** Resultado do teste de talassemia (perfusão miocárdica)
- **Valores:**
  - `3` = Normal
  - `6` = Defeito fixo
  - `7` = Defeito reversível
- **Tipo:** Categórico
- **Nota:** 2 valores ausentes (0.7%)

---

### Variável Alvo (Target)

#### **target** (Categórico)

- **Descrição:** Diagnóstico de doença cardíaca
- **Valores Originais:** 0-4 (0 = sem doença, 1-4 = níveis de severidade)
- **Valores Convertidos:**
  - `0` = Ausência de doença cardíaca
  - `1` = Presença de doença cardíaca (valores 1-4 agrupados)
- **Tipo:** Binário (após conversão)
- **Distribuição:** 164 sem doença (54%), 139 com doença (46%)

## 📊 Estatísticas Descritivas

- **Idade média:** 54.4 anos
- **Distribuição por sexo:** 206 homens (68%), 97 mulheres (32%)
- **Valores ausentes:**
  - ca: 4 valores ausentes (1.3%)
  - thal: 2 valores ausentes (0.7%)

## 🧠 Relevância Clínica das Variáveis para IA

### Variáveis Principais (Obrigatórias)

#### 1. **age (Idade)**

**Relevância para IA:** A idade é um dos fatores de risco cardiovascular mais significativos. O risco de doença cardíaca aumenta exponencialmente com a idade devido ao envelhecimento natural do sistema cardiovascular, acúmulo de placas ateroscleróticas e perda de elasticidade arterial. Modelos de IA utilizam a idade como feature fundamental para estratificação de risco, pois ela se correlaciona fortemente com a probabilidade de eventos cardiovasculares.

#### 2. **sex (Sexo)**

**Relevância para IA:** Diferenças fisiológicas entre homens e mulheres afetam significativamente a manifestação e progressão de doenças cardíacas. Homens tendem a desenvolver doença coronariana mais cedo, enquanto mulheres têm proteção hormonal até a menopausa. A IA pode aprender padrões específicos de cada sexo, como sintomas atípicos em mulheres (fadiga, náusea) versus sintomas clássicos em homens (dor torácica), melhorando a precisão diagnóstica.

#### 3. **trestbps (Pressão Arterial em Repouso)**

**Relevância para IA:** A pressão arterial é um indicador direto da carga de trabalho do miocárdio e da resistência vascular. Valores elevados (hipertensão) causam hipertrofia ventricular esquerda e aumentam o risco de infarto e AVC. Modelos de IA utilizam este parâmetro para avaliar o estresse cardiovascular basal do paciente, identificando indivíduos em risco mesmo antes de sintomas clínicos aparecerem.

#### 4. **chol (Colesterol Sérico)**

**Relevância para IA:** O colesterol é um marcador bioquímico crucial para aterosclerose, processo que leva à formação de placas nas artérias coronárias. Níveis elevados de colesterol LDL ("ruim") estão diretamente associados ao risco de eventos cardiovasculares. A IA pode combinar este marcador com outros fatores para prever não apenas a presença de doença, mas também sua severidade e progressão.

#### 5. **thalach (Frequência Cardíaca Máxima)**

**Relevância para IA:** A frequência cardíaca máxima alcançada durante exercício reflete a capacidade funcional do coração e a reserva cardiovascular. Valores baixos sugerem comprometimento da função cardíaca ou isquemia induzida por esforço. Modelos de IA utilizam esta variável para avaliar a capacidade adaptativa do sistema cardiovascular sob estresse, um indicador importante de prognóstico.

#### 6. **target (Presença de Doença)**

**Relevância para IA:** Esta é a variável alvo (label) que o modelo de IA aprende a prever. Representa o diagnóstico confirmado de doença cardíaca, permitindo que algoritmos de aprendizado supervisionado identifiquem padrões complexos e não-lineares entre as features de entrada e o desfecho clínico.

### Variáveis Complementares

#### 7. **cp (Tipo de Dor no Peito)**

**Relevância para IA:** A caracterização da dor torácica é fundamental no diagnóstico diferencial. Angina típica tem alta especificidade para doença coronariana, enquanto dor atípica pode indicar outras condições. A IA pode aprender a ponderar este sintoma junto com outros fatores, melhorando a acurácia diagnóstica em casos ambíguos.

#### 8. **exang (Angina Induzida por Exercício)**

**Relevância para IA:** A presença de angina durante esforço físico é um forte indicador de isquemia miocárdica (falta de oxigênio no músculo cardíaco). Este sintoma sugere obstrução significativa das artérias coronárias. Modelos de IA utilizam esta feature para identificar pacientes com doença coronariana obstrutiva que requerem intervenção.

#### 9. **oldpeak (Depressão ST)**

**Relevância para IA:** A depressão do segmento ST no eletrocardiograma durante exercício é um marcador eletrofisiológico de isquemia. Quanto maior a depressão, maior a probabilidade de doença coronariana significativa. A IA pode quantificar este parâmetro contínuo para estratificação de risco mais precisa.

#### 10. **slope (Inclinação do Segmento ST)**

**Relevância para IA:** A morfologia do segmento ST fornece informações sobre a natureza da isquemia. Inclinação descendente é mais preocupante que ascendente. A IA pode aprender padrões sutis de ECG que escapam à análise visual humana.

#### 11. **ca (Número de Vasos Principais)**

**Relevância para IA:** O número de artérias coronárias com obstrução significativa (detectado por angiografia) correlaciona-se diretamente com a gravidade da doença e o prognóstico. Modelos de IA podem usar esta informação para prever não apenas presença, mas também extensão da doença.

#### 12. **thal (Talassemia)**

**Relevância para IA:** Defeitos de perfusão miocárdica detectados por cintilografia indicam áreas do coração com fluxo sanguíneo reduzido. Defeitos reversíveis sugerem isquemia, enquanto fixos indicam infarto prévio. A IA integra esta informação funcional com dados clínicos para diagnóstico mais preciso.

### 🎯 Integração Multi-Variável na IA

O poder dos modelos de Machine Learning está na capacidade de identificar **interações complexas** entre variáveis que não são óbvias para análise humana:

- **Exemplo 1:** Um paciente jovem (age baixo) com colesterol alto (chol elevado) pode ter risco similar a um paciente mais velho com colesterol normal.
- **Exemplo 2:** Mulheres (sex=0) com dor atípica (cp=2) podem ter doença coronariana significativa, um padrão que a IA pode aprender.
- **Exemplo 3:** A combinação de pressão alta (trestbps), frequência cardíaca baixa (thalach) e depressão ST (oldpeak) pode indicar isquemia severa.

A IA cardiovascular não analisa variáveis isoladamente, mas sim como um **sistema integrado**, capturando padrões multidimensionais que refletem a complexidade fisiológica do sistema cardiovascular.

## ✅ Adequação para o Projeto CardioIA

Este dataset é ideal para o projeto porque:

1. ✅ **Tamanho adequado:** 303 linhas (> 100 requisito mínimo)
2. ✅ **Variáveis relevantes:** Contém todas as variáveis clínicas obrigatórias (age, sex, trestbps, chol, thalach, target)
3. ✅ **Formato correto:** CSV com dados estruturados
4. ✅ **Fonte confiável:** UCI Machine Learning Repository (referência acadêmica)
5. ✅ **Dados reais:** Coletados de instituições médicas reais
6. ✅ **Anonimizado:** Não contém informações identificáveis (LGPD compliant)
7. ✅ **Bem documentado:** Amplamente usado em pesquisas de ML
8. ✅ **Diversidade demográfica:** Inclui ambos os sexos e ampla faixa etária
9. ✅ **Variáveis complementares:** Além das obrigatórias, possui features adicionais para análise mais profunda

## 📚 Referências

- Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J., Sandhu, S., Guppy, K., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. American Journal of Cardiology, 64, 304-310.

- UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/heart+disease

## 📝 Notas de Uso

- Os valores ausentes (?) foram identificados e precisam ser tratados na fase de curadoria
- A variável target foi convertida para binária para simplificar a classificação
- Todas as variáveis numéricas estão em suas unidades originais (não normalizadas)
