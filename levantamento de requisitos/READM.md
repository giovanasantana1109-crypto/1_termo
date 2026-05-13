# 📋 Engenharia de Requisitos: Da Captação à Documentação

## 1. Técnicas de Elicitação de Requisitos

### 🧠 Brainstorming
Reunião técnica livre para geração de ideias e soluções sem julgamentos prévios.
*   **Foco:** Descoberta de requisitos inovadores e identificação de dores ocultas.
*   **Dinâmica:** Conduzido por um moderador; todas as ideias são registradas para posterior filtragem e priorização.

### 👥 Entrevistas
Conversas diretas e estruturadas com partes interessadas (*stakeholders*) para entender necessidades específicas.
*   **Entrevista Aberta:** Perguntas amplas; foco em entender o contexto geral do negócio.
*   **Entrevista Fechada:** Perguntas específicas; foco em detalhar regras de negócio e fluxos de trabalho.

---

## 2. Classificação de Requisitos

### ⚙️ Requisitos Funcionais (RF)
Definem **o que** o sistema deve fazer. Representam as funcionalidades e os serviços que o software deve fornecer.
*   *Exemplo 1:* O sistema deve permitir que o cliente consulte o saldo da conta corrente.
*   *Exemplo 2:* O sistema deve emitir um alerta em PDF quando o estoque atingir o nível crítico.

### 🛡️ Requisitos Não Funcionais (RNF)
Definem **como** o sistema deve fazer. Restringem os serviços do sistema, abordando critérios de qualidade, desempenho e segurança.
*   *Exemplo 1 (Desempenho):* A consulta de saldo não deve demorar mais do que 2 segundos para carregar.
*   *Exemplo 2 (Segurança):* Todas as senhas de usuários devem ser criptografadas no banco de dados utilizando SHA-256.

---

## 3. Alinhamento Visível e Validação

### 🎨 Prototipagem
Construção de modelos preliminares do sistema para validar os requisitos com o cliente antes do desenvolvimento.
*   **Baixa Fidelidade:** Desenhos em papel (*wireframes* básicos) focados na estrutura da informação.
*   **Alta Fidelidade:** Protótipos digitais interativos (ex: criados no Figma) focados na experiência do usuário (UX) e visual final.

### 📊 Diagramas (Modelagem)
Representações visuais que facilitam a comunicação técnica entre analistas e desenvolvedores.
*   **Diagrama de Casos de Uso (UML):** Mapeia os atores (usuários) e suas interações diretas com as funcionalidades do sistema.
*   **Diagrama de Fluxo de Dados (DFD):** Demonstra o caminho que os dados percorrem dentro do software, desde a entrada até o armazenamento.

---

## 4. Artefatos de Saída

### 📝 Relatórios Técnicos
Documentos formais que consolidam as decisões tomadas durante a fase de engenharia de requisitos.
*   **Especificação de Requisitos de Software (ERS):** Contém a descrição completa do comportamento do sistema a ser desenvolvido, servindo como o contrato técnico entre a equipe de desenvolvimento e o cliente.
