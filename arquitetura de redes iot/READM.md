# 🌐 Arquitetura de Redes IoT: Da Infraestrutura aos Protocolos

## 1. Infraestrutura Física: Ativos e Passivos de Redes
A base de qualquer rede de comunicação divide-se entre componentes que processam dados e componentes que apenas transmitem o sinal.

### ⚡ Ativos de Rede
Dispositivos que manipulam, direcionam ou geram dados na rede. Eles interagem ativamente com os pacotes de dados.
*   **Roteadores/Gateways IoT:** Direcionam o tráfego entre a rede local (sensores) e a nuvem.
*   **Switches:** Conectam múltiplos dispositivos dentro da mesma rede local.
*   **Pontos de Acesso (Access Points):** Permitem conexões sem fio na rede.

### 🔌 Passivos de Rede
Componentes que servem apenas como meio físico para o tráfego dos sinais elétricos ou ópticos. Eles não alteram os dados.
*   **Cabos:** Par trançado (UTP) ou fibra óptica.
*   **Conectores e Tomadas:** RJ-45, patch panels e racks estruturados.

---

## 2. Internet e Suas Derivações (Evolução da Rede)
A evolução da grande rede mundial para suportar bilhões de novos dispositivos conectados.

*   **Internet Tradicional:** Focada na interconexão de computadores e servidores para o consumo de dados humano (páginas web, streaming).
*   **Internet das Coisas (IoT):** Extensão da rede que conecta objetos cotidianos, sensores e atuadores à internet, permitindo automação e coleta de dados sem intervenção humana.
*   **Internet Industrial das Coisas (IIoT):** Aplicação da IoT em ambientes fabris e industriais. Exige altíssima confiabilidade, segurança crítica e baixíssima latência (tempo real).

---

## 3. Pesquisa de Dispositivos de Rede e Driver ESP32
O hardware no ecossistema IoT e como o sistema operacional se comunica com ele.

### 🔍 Pesquisa de Dispositivos de Rede IoT
Para implementar uma solução IoT, avalia-se o hardware com base em:
*   **Consumo de Energia:** Essencial para dispositivos alimentados por bateria.
*   **Alcance:** Curto alcance (Wi-Fi, Bluetooth) versus Longo alcance (LoRaWAN, NB-IoT).

### 🛠️ Driver ESP32
O ESP32 é um microcontrolador amplamente utilizado em projetos IoT devido ao Wi-Fi e Bluetooth integrados.
*   **Função do Driver:** O driver (como o CP210x ou CH340) permite que o sistema operacional do computador reconheça a placa via porta USB (conversão Serial-USB).
*   **Ambiente de Desenvolvimento:** Permite o envio de firmware através de ferramentas como a Arduino IDE, VS Code (PlatformIO) ou ESP-IDF.

---

## 4. Comunicação: Protocolo MQTT e IoT
O padrão de comunicação mais leve e eficiente utilizado na Internet das Coisas.

### 📡 Arquitetura Publish/Subscribe (Publicação/Assinatura)
Diferente do HTTP (onde o cliente pede e o servidor responde), o MQTT utiliza um intermediário central chamado **Broker**.

*   **Broker:** O servidor central que recebe e distribui todas as mensagens (ex: Mosquitto, HiveMQ).
*   **Topic (Tópico):** O canal de dados (ex: `casa/quarto/temperatura`).
*   **Publisher (Publicador):** O sensor que envia dados para um tópico.
*   **Subscriber (Assinante):** O dispositivo ou app que escuta um tópico para receber dados.

```text
[Sensor ESP32] ---> (Publica em: casa/quarto/temp) ---> [ MQTT BROKER ] ---> (Distribui para) ---> [Aplicativo Celular]
```

---

## 5. Artefatos Acadêmicos: Relatório Técnico em IoT
Documentação indispensável para registrar experimentos de bancada e projetos de redes.

### 📝 Estrutura Recomendada
1.  **Introdução:** Contextualização do problema IoT que a rede visa resolver.
2.  **Materiais Utilizados:** Lista de ativos, passivos e placas (ex: ESP32) aplicados.
3.  **Topologia da Rede:** Diagrama visual mostrando como os sensores se conectam ao Broker.
4.  **Resultados Obtidos:** Capturas de tela de logs do MQTT e medições de sensores.
5.  **Conclusão:** Análise crítica sobre o desempenho da arquitetura montada.
