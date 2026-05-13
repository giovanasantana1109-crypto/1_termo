# 🐍 Lógica de Programação com Python: Interfaces, Git Limpo e Projetos

## 1. Interfaces Gráficas com PythonG (PythonGi / PyGObject)
Desenvolvimento de interfaces gráficas (GUI) modernas utilizando o ecossistema GNOME (GTK) nativamente no Python através do PyGObject.

### 🧩 Conceitos Fundamentais
*   **Main Loop:** Ciclo que escuta os eventos do sistema (cliques, digitação) e atualiza a interface.
*   **Widgets:** Componentes visuais da interface (Botões, Janelas, Caixas de texto).
*   **Sinais e Callbacks:** Vinculação de um evento do usuário a uma função lógica em Python.

### 💻 Exemplo Prático: Janela Básica com Botão
```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MinhaJanela(Gtk.Window):
    def __init__(self):
        super().__init__(title="Aula de PythonGi")
        self.set_default_size(300, 100)

        # Criando um botão
        self.botao = Gtk.Button(label="Clique Aqui")
        self.botao.connect("clicked", self.ao_clicar_no_botao)
        self.add(self.botao)

    def ao_clicar_no_botao(self, widget):
        print("Botão acionado! Lógica de programação executada.")

janela = MinhaJanela()
janela.connect("destroy", Gtk.main_quit)
janela.show_all()
Gtk.main()
```

---

## 2. Boas Práticas e Organização no GitHub (GitHub Clean)
Como manter repositórios acadêmicos e profissionais organizados, limpos e legíveis para avaliadores e recrutadores.

### 🗑️ O Arquivo `.gitignore` para Python
Evita o envio de arquivos temporários, caches e ambientes virtuais para a nuvem.
*   **Pastas a ignorar:** `__pycache__/`, `.venv/`, `.env`, `.pytest_cache/`.

### 📜 Padrões de Commits Limpos (Conventional Commits)
Mensagens padronizadas facilitam o rastreamento do histórico do código.
*   `feat:` Nova funcionalidade adicionada ao projeto.
*   `fix:` Correção de um bug ou erro de lógica.
*   `docs:` Alterações na documentação (ex: arquivo README.md).
*   `refactor:` Modificação no código que não altera seu comportamento final.

### 📖 README.md Eficiente
Todo repositório deve conter um guia explicando:
1. O que é o projeto.
2. Como instalar as dependências.
3. Como executar o código.

---

## 3. Estruturação e Organização de Projetos de Código (Code Projects)
Transição de scripts de arquivo único para arquiteturas de software organizadas e modulares.

### 📂 Estrutura Padrão de Diretórios
```text
meu_projeto/
│
├── .gitignore          # Arquivos ignorados pelo Git
├── README.md           # Documentação do projeto
├── requirements.txt    # Bibliotecas externas necessárias
│
├── src/                # Código-fonte do projeto
│   ├── __init__.py     # Transforma a pasta em um pacote Python
│   ├── main.py         # Ponto de entrada do programa
│   ├── interface.py    # Lógica de telas (PythonGi)
│   └── core.py         # Funções de lógica pura e cálculos
│
└── tests/              # Testes automatizados do sistema
    └── test_core.py
```

### 🛠️ Regras de Ouro para Escrita de Código
*   **Modularidade:** Divida problemas grandes em funções pequenas com responsabilidade única.
*   **Variáveis Semânticas:** Evite nomes como `x`, `a`, `b1`. Use `total_vendas`, `nome_usuario`.
*   **PEP 8:** Siga o guia de estilo oficial do Python (espaçamentos, quebras de linha e comentários).
