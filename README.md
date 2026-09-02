# 🤖 Python Automation Scripts

Coleção de scripts e ferramentas desenvolvidos em **Python** para automatizar tarefas repetitivas, otimizar processos e aumentar a produtividade.

O objetivo deste repositório é centralizar diferentes soluções de automação que podem ser utilizadas no dia a dia, incluindo automação do Windows, manipulação de arquivos, controle do sistema, integração com aplicações e outras tarefas.

## 📌 Objetivos

* ⚙️ Automatizar tarefas repetitivas
* 🚀 Aumentar a produtividade
* 🖥️ Automatizar tarefas no Windows
* 📁 Manipular arquivos e diretórios
* 🔧 Criar ferramentas auxiliares
* 🔗 Integrar diferentes aplicações e serviços
* 🐍 Praticar e explorar recursos do Python

## 📂 Estrutura do projeto

```text
automation-scripts/
│
├── windows/
│   ├── bloquear_tela.py
│   ├── mover_mouse.py
│   └── ...
│
├── arquivos/
│   ├── organizar_arquivos.py
│   └── ...
│
├── office/
│   ├── ...
│
├── network/
│   ├── ...
│
├── utils/
│   ├── ...
│
├── requirements.txt
└── README.md
```

A estrutura poderá ser modificada conforme novos scripts e categorias forem adicionados ao projeto.

## 🐍 Requisitos

* Python 3.10 ou superior
* Windows, Linux ou macOS, dependendo do script
* Bibliotecas adicionais indicadas no `requirements.txt`

Para verificar a versão do Python:

```bash
python --version
```

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/automation-scripts.git
```

Entre na pasta:

```bash
cd automation-scripts
```

Opcionalmente, crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Utilização

Cada script possui uma finalidade específica.

Por exemplo:

```bash
python windows/bloquear_tela.py
```

Antes de executar um script, consulte os comentários e instruções presentes no próprio arquivo para verificar possíveis configurações necessárias.

## 🛠️ Scripts

### 🔒 Bloqueio do Windows

Scripts relacionados ao controle e automação do sistema operacional Windows.

Exemplo:

```python
import ctypes

ctypes.windll.user32.LockWorkStation()
```

Esse comando solicita o bloqueio da sessão atual do Windows.

### 🖱️ Automação do mouse

Scripts para movimentação e controle do mouse podem ser utilizados para automatizar determinadas tarefas.

Dependendo da implementação, bibliotecas como `pyautogui` podem ser utilizadas.

## 📦 Dependências

As dependências utilizadas pelos scripts devem ser registradas no arquivo:

```text
requirements.txt
```

Exemplo:

```text
pyautogui
requests
psutil
```

Instalação:

```bash
pip install -r requirements.txt
```

## ⚠️ Observações

Alguns scripts podem depender diretamente do sistema operacional ou de configurações específicas do computador.

Antes de executar um script:

1. Leia o código.
2. Verifique as dependências.
3. Confirme quais permissões são necessárias.
4. Teste primeiro em um ambiente controlado.
5. Evite executar scripts desconhecidos sem entender o que eles fazem.

## 🔐 Segurança

Este repositório é destinado a **automação legítima e produtividade**.

Não armazene no repositório:

* Senhas
* Tokens de API
* Chaves privadas
* Credenciais
* Dados pessoais
* Arquivos de configuração contendo informações sensíveis

Utilize variáveis de ambiente ou arquivos `.env` para informações sensíveis.

Adicione o `.env` ao `.gitignore`:

```text
.env
```

## 🤝 Contribuição

Contribuições são bem-vindas.

Para contribuir:

```bash
git clone https://github.com/SEU-USUARIO/automation-scripts.git
```

Crie uma nova branch:

```bash
git checkout -b feature/novo-script
```

Adicione sua alteração:

```bash
git add .
```

Faça o commit:

```bash
git commit -m "feat: adiciona novo script de automação"
```

Envie a branch:

```bash
git push origin feature/novo-script
```

Depois, abra um **Pull Request**.

## 📋 Convenção de commits

Sempre que possível, utilize commits organizados:

```text
feat: adiciona novo script
fix: corrige erro no script
refactor: melhora implementação
docs: atualiza documentação
chore: atualiza dependências
```

## 📈 Roadmap

Algumas ideias para futuras automações:

* [ ] Automação de arquivos e pastas
* [ ] Automação do Windows
* [ ] Controle de mouse e teclado
* [ ] Automação de aplicações
* [ ] Integração com Microsoft 365
* [ ] Integração com Microsoft Teams
* [ ] Automação de e-mails
* [ ] Automação de tarefas administrativas
* [ ] Scripts para monitoramento do sistema
* [ ] Integração com APIs
* [ ] Interface gráfica para alguns scripts

## 📄 Licença

Este projeto pode ser distribuído sob a licença GNU General Public License v2.0

Consulte o arquivo `LICENSE` para mais informações.

---

### 👨‍💻 Autor

Desenvolvido para estudos, produtividade e automação de tarefas utilizando **Python**.

> **Automatize o que é repetitivo. Foque no que realmente importa.** 🐍⚙️

