# Arquitetura do SPUR

## Visão geral

O SPUR é uma aplicação de monitoramento orientada à detecção de mudanças relevantes na localização de conteúdos digitais.

Seu funcionamento parte da comparação entre dois estados do ambiente monitorado:

```text
Estado anterior
      ↓
Nova observação
      ↓
Estado atual
      ↓
Comparação
      ↓
Mudança relevante?
   ├── Não → silêncio
   └── Sim → evento