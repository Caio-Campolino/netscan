# NetScan

Ferramenta CLI de varredura de rede desenvolvida em Python, inspirada na saída do Nmap. O foco do projeto é o estudo de sockets, organização de código e extensibilidade para ambientes controlados.

## Estrutura do Projeto

```text
scanner_rede/
├── netscan                 # Entry point (Executável)
├── requirements.txt        # Dependências
├── README.md
└── netscan_pkg/            # Pacote principal
    ├── banner.py
    ├── core/               # Lógica de discovery
    └── utils/              # Loggers e helpers
```
---

## Instalação e Uso
Requer Python 3.10+. Recomendado uso em Linux ou WSL (Windows).

1. Configuração rápida:
```text
   git clone https://github.com/Caio-Campolino/scanner_rede.git
   cd scanner_rede
   pip install -r requirements.txt
   chmod +x netscan
```
2. Exemplos de execução:
```text
 Scan básico
./netscan 192.168.0.1

 Modo verboso
./netscan 192.168.0.1 -v

 Ajuda
./netscan -h
```
---
## Aviso Legal
Ferramenta desenvolvida estritamente para fins educacionais. O autor não se responsabiliza pelo uso indevido ou scans em redes sem autorização explícita.