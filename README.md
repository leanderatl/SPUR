# SPUR

**Content Relocation Monitor**

SPUR é uma aplicação de monitoramento desenvolvida para detectar mudanças relevantes na localização de conteúdos digitais.

O projeto surgiu a partir de um problema real observado em um fluxo de trabalho audiovisual: conteúdos previamente organizados podem ser realocados entre diferentes unidades de programação sem que essa alteração seja imediatamente percebida pelo profissional responsável.

O SPUR transforma essa mudança de localização em um evento detectável.

---

## Problema

Em estruturas de armazenamento organizadas por períodos, categorias ou unidades de programação, a movimentação de um arquivo pode representar uma alteração operacional importante.

Observar apenas o estado atual do armazenamento não permite determinar onde determinado conteúdo estava anteriormente.

O SPUR resolve esse problema preservando um estado conhecido e comparando-o com uma nova observação.

```text
ESTADO ANTERIOR
      ↓
NOVA VARREDURA
      ↓
ESTADO ATUAL
      ↓
COMPARAÇÃO
      ↓
MUDANÇA RELEVANTE?
   ├── NÃO → silêncio
   └── SIM → evento