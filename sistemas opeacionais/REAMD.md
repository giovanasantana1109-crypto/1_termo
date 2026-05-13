# 🖥️ Sistemas Operacionais: Arquitetura, Operação via CLI e Segurança

## 1. Visão Geral e Indicação de Sistemas Operacionais
A escolha de um Sistema Operacional (S.O.) depende diretamente do cenário de aplicação, custo, desempenho e requisitos de segurança.

*   **Servidores e Infraestrutura de Nuvem:** Predomínio absoluto do **Linux** (devido à estabilidade, segurança e eficiência no uso de recursos).
*   **Estações de Trabalho Corporativas e Usuário Final:** Predomínio do **Windows** (pela vasta compatibilidade de softwares comerciais e facilidade de gerenciamento centralizado via Active Directory).
*   **Dispositivos Embarcados e IoT:** Versões customizadas de **Linux** (como Yocto ou Alpine) devido à leveza do kernel.

---

## 2. Ecossistemas: Windows e Distribuições Linux

### 🪟 Ecossistema Windows
*   **Características:** Proprietário, baseado no kernel NT, com forte apelo em interfaces gráficas (GUI) e compatibilidade com softwares legados.
*   **Segmentação:** Dividido em versões *Client* (Windows 10/11 para usuários) e *Server* (Windows Server para infraestrutura de rede).

### 🐧 Distribuições Linux (Distros)
O Linux não é um S.O. único, mas um Kernel. As distribuições combinam o kernel com ferramentas de sistema e gerenciadores de pacotes.
*   **Focadas em Servidores/Estabilidade:** Debian, Ubuntu Server, Red Hat Enterprise Linux (RHEL), Rocky Linux.
*   **Focadas em Desktop/Usuário:** Ubuntu Desktop, Linux Mint, Fedora.
*   **Focadas em Segurança/Pentest:** Kali Linux, Parrot OS.

---

## 3. Operação de S.O. via CLI (Interface de Linha de Comando)
A linha de comando é a ferramenta primária de administração de sistemas, pois permite automação através de scripts, consome menos recursos e funciona em servidores sem interface gráfica.

### 🌐 Comandos Universais (Conceito CLI)
Independentemente do sistema, a CLI opera sob a lógica de: `comando -opções argumento` (ex: listar arquivos, navegar em diretórios, mover arquivos).

---

## 4. Operação Prática do Windows via CLI (CMD e PowerShell)
No Windows, os administradores utilizam o **Prompt de Comando (CMD)** para tarefas legadas e o **PowerShell** (baseado em objetos e .NET) para automação avançada.

### 📁 Gerenciamento de Pastas (Diretórios)
*   `cd` : Navega entre diretórios (Ex: `cd C:\Users`).
*   `dir` : Lista os arquivos e pastas do diretório atual.
*   `mkdir` : Cria uma nova pasta (Ex: `mkdir AulaSO`).
*   `rmdir /s /q` : Remove uma pasta e todo o seu conteúdo de forma silenciosa.

### 👥 Gerenciamento de Usuários e Permissões
*   `net user` : Lista todos os usuários cadastrados na máquina.
*   `net user NomeUsuario Senha123 /add` : Cria um novo usuário no sistema.
*   `net localgroup Administradores NomeUsuario /add` : Eleva o usuário ao grupo de administradores.
*   `net user NomeUsuario /delete` : Exclui o usuário.

### ⚙️ Lidando com Variáveis de Ambiente
Variáveis de ambiente armazenam informações sobre o ambiente do sistema (como caminhos de programas executáveis).
*   Exibir uma variável existente: `echo %USERPROFILE%` ou `echo %PATH%`.
*   Criar uma variável temporária na sessão: `set MINHA_VARIAVEL=AulaSO`.
*   Criar uma variável permanente no sistema: `setx VAR_PERMANENTE "Valor"`.

---

## 5. Fundamentos de Segurança Cibernética no S.O.
A segurança do sistema operacional é a última barreira de defesa contra ameaças digitais.

*   **Princípio do Menor Privilégio (PoLP):** Usuários comuns e serviços do sistema devem rodar com o mínimo de permissões necessárias. Nunca utilize a conta de *Administrador* ou *root* para tarefas diárias.
*   **Mecanismos de Controle de Acesso:** 
    *   **UAC (User Account Control) no Windows:** Solicita confirmação ou credenciais administrativas antes de executar tarefas críticas.
    *   **Permissões de Arquivos (NTFS):** Controle estrito sobre quem pode Ler (Read), Escrever (Write) ou Executar (Execute) arquivos e pastas.
*   **Hardening do S.O.:** Processo de mapear e desativar serviços desnecessários, fechar portas lógicas não utilizadas e manter o sistema atualizado com os últimos patches de segurança para reduzir a superfície de ataque.
