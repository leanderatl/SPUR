# ADR-001 — Arquitetura multiplataforma e separação Core/Platform

**Status:** Aceito  
**Data:** 27/08/2026  
**Projeto:** SPUR  
**Versão relacionada:** V5

## Contexto

A V4 do SPUR validou funcionalmente a capacidade de detectar realocações de conteúdos por meio da comparação entre estados sucessivos.

Entretanto, a prova de conceito foi desenvolvida inicialmente para macOS e possui elementos específicos desse sistema operacional.

A V5 tem como objetivo transformar essa prova de conceito em uma aplicação estruturada, testável e preparada para funcionar em macOS e Windows.

## Decisão

O SPUR V5 adotará uma separação explícita entre duas camadas principais:

### Core

Responsável pela lógica independente do sistema operacional:

- catalogação de arquivos;
- representação dos conteúdos;
- gerenciamento de estado;
- comparação entre estados;
- detecção de realocações;
- geração de eventos;
- regras de domínio.

### Platform

Responsável pelas integrações específicas de cada sistema operacional:

- notificações;
- agendamento;
- integração com recursos do sistema;
- particularidades de acesso ao ambiente.

A arquitetura seguirá este princípio:

```text
              SPUR
               │
       ┌───────┴───────┐
       │               │
      CORE          PLATFORM
       │               │
       │         ┌─────┴─────┐
       │         │           │
       │       macOS       Windows
       │
  mesma lógica