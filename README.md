# FIAP-CardioIA-Fase1

## 🩺 Projeto CardioIA - Batimentos de Dados

Ecossistema de cardiologia moderna integrando Machine Learning, Visão Computacional, IoT e Agentes Inteligentes.

### 👥 Integrantes da Equipe

- **[Seu Nome]** - Especialista em IoT e Dados Estruturados
- **[Nome]** - Arquiteto de Dados e Governança
- **[Nome]** - Analista de NLP
- **[Nome]** - Especialista em Visão Computacional

### 🎯 Objetivo do Projeto

Este projeto visa criar a base de dados fundamental para um sistema de IA cardiovascular, coletando e organizando três tipos de dados essenciais:

1. **Dados Numéricos (IoT)** - Parâmetros clínicos e dispositivos IoT
2. **Dados Textuais (NLP)** - Literatura médica para processamento de linguagem natural
3. **Dados Visuais (VC)** - Imagens de exames para visão computacional

### 📂 Estrutura do Repositório

```
FIAP-CardioIA-Fase1/
├── README.md           # Documentação principal
├── assets/             # Recursos do projeto (textos, scripts)
└── .gitignore         # Arquivos ignorados pelo Git
```

---

## 🔢 Dados Numéricos (IoT)

### Dataset: Heart Disease UCI (Cleveland Database)

**Descrição:** Dataset contendo 303 registros de pacientes com variáveis clínicas cardiovasculares coletados de instituições médicas nos EUA, Hungria e Suíça.

**Fonte Original:** [UCI Machine Learning Repository - Heart Disease](http://archive.ics.uci.edu/ml/datasets/Heart+Disease)

**Acesso ao Dataset:** 🔗 _[Link do Google Drive será adicionado após hospedagem]_

**Documentação Completa:** [📄 DATASET_INFO.md](assets/DATASET_INFO.md)

---

### 📊 Características do Dataset

- **Instâncias:** 303 pacientes
- **Variáveis:** 14 atributos clínicos
- **Formato:** CSV
- **Licença:** CC BY 4.0 (Creative Commons)
- **Tipo:** Dados reais anonimizados

---

### 🏥 Variáveis e Relevância Clínica

| Variável     | Descrição                                  | Relevância para IA                                                                                |
| ------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **age**      | Idade (29-77 anos)                         | Fator de risco primário; risco cardiovascular aumenta exponencialmente com idade                  |
| **sex**      | Sexo (1=M, 0=F)                            | Diferenças fisiológicas afetam manifestação de doenças cardíacas; sintomas específicos por gênero |
| **trestbps** | Pressão arterial em repouso (94-200 mm Hg) | Indica carga de trabalho do miocárdio; hipertensão causa hipertrofia ventricular                  |
| **chol**     | Colesterol sérico (126-564 mg/dl)          | Marcador de aterosclerose; preditor direto de eventos cardiovasculares                            |
| **thalach**  | Frequência cardíaca máxima (71-202 bpm)    | Reflete capacidade funcional do coração; valores baixos sugerem comprometimento                   |
| **cp**       | Tipo de dor no peito (1-4)                 | Fundamental para diagnóstico diferencial; angina típica tem alta especificidade                   |
| **exang**    | Angina induzida por exercício (0-1)        | Forte indicador de isquemia miocárdica; sugere obstrução coronariana                              |
| **oldpeak**  | Depressão ST (0.0-6.2 mm)                  | Marcador eletrofisiológico de isquemia; quanto maior, maior a probabilidade de doença             |
| **slope**    | Inclinação segmento ST (1-3)               | Morfologia do ECG fornece informações sobre natureza da isquemia                                  |
| **ca**       | Vasos principais (0-3)                     | Correlaciona-se com gravidade da doença e prognóstico                                             |
| **thal**     | Perfusão miocárdica (3,6,7)                | Defeitos indicam áreas com fluxo sanguíneo reduzido                                               |
| **target**   | Diagnóstico (0=ausente, 1=presente)        | Variável alvo para modelos de classificação                                                       |

---

### 🧠 Por que estas variáveis são importantes para IA?

O poder dos modelos de Machine Learning está na capacidade de identificar **interações complexas** entre variáveis:

- **Integração Multi-Variável:** A IA não analisa variáveis isoladamente, mas como um sistema integrado
- **Padrões Não-Lineares:** Captura relações complexas que escapam à análise humana
- **Estratificação de Risco:** Combina múltiplos fatores para prever não apenas presença, mas severidade da doença
- **Personalização:** Aprende padrões específicos por idade, sexo e perfil clínico

**Exemplo:** Um paciente jovem com colesterol alto pode ter risco similar a um paciente mais velho com colesterol normal - a IA identifica essas nuances.

---

### 📈 Estatísticas do Dataset

- **Idade média:** 54.4 anos
- **Distribuição por sexo:** 68% masculino, 32% feminino
- **Prevalência de doença:** 46% com doença cardíaca
- **Valores ausentes:** 6 valores (2% do total) em 2 variáveis (ca, thal)

---

### ✅ Curadoria Realizada

- ✅ Download automatizado via script Python
- ✅ Conversão da variável target para binária (0/1)
- ✅ Identificação de valores ausentes
- ✅ Validação de 303 linhas (> 100 requisito mínimo)
- ✅ Verificação de todas as colunas obrigatórias

---

### ⚖️ Governança e Ética

- **Anonimização:** ✅ Dataset não contém informações identificáveis (nomes, CPF, endereços)
- **Diversidade:** ✅ Inclui ambos os sexos e ampla faixa etária (29-77 anos)
- **Origem:** ✅ Dados reais de instituições médicas (Cleveland Clinic, Hungarian Institute, etc.)
- **Conformidade LGPD:** ✅ Dados públicos disponibilizados para pesquisa acadêmica
- **Transparência:** ✅ Fonte documentada e rastreável

---

## 📜 Dados Textuais (NLP)

_Seção em desenvolvimento..._

---

## 🖼️ Dados Visuais (Visão Computacional)

_Seção em desenvolvimento..._

---

## ⚖️ Governança e Ética de Dados

_Seção em desenvolvimento..._

---

## 📊 Status do Projeto

- [x] Estruturação inicial do repositório
- [x] Coleta de dados numéricos
- [x] Documentação técnica dos dados numéricos
- [ ] Curadoria e limpeza dos dados numéricos
- [ ] Hospedagem dos dados em nuvem
- [ ] Coleta de dados textuais
- [ ] Coleta de dados visuais
- [ ] Documentação completa
- [ ] Validação final

---

**FIAP - Faculdade de Informática e Administração Paulista**  
**Curso:** [Seu Curso]  
**Disciplina:** [Nome da Disciplina]  
**Ano:** 2024
