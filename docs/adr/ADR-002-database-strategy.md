# ADR-002 — Estratégia de persistência e adoção de PostgreSQL

**Status:** Aceito  
**Data:** 27/08/2026  
**Projeto:** SPUR  
**Versão relacionada:** V5

## Contexto

A V4 do SPUR utiliza persistência simples para armazenar o estado necessário à comparação entre execuções.

Essa abordagem atende ao problema atualmente validado: conhecer o estado anterior, compará-lo com o estado atual e detectar realocações.

Durante o planejamento da V5, foi considerada a adoção de PostgreSQL.

Entretanto, a V5 tem como objetivo principal transformar a prova de conceito em uma aplicação organizada, testável e multiplataforma.

A introdução de um banco de dados relacional não é necessária para atingir esse objetivo neste momento.

## Decisão

PostgreSQL não será requisito inicial do SPUR V5.

A persistência deverá permanecer proporcional às necessidades atuais da aplicação.

A adoção de PostgreSQL será reavaliada quando surgirem requisitos concretos relacionados a:

- histórico consultável;
- auditoria;
- retenção permanente de eventos;
- consultas complexas;
- múltiplos consumidores;
- centralização de dados;
- integração com outros sistemas.

## Princípio arquitetural

A tecnologia de persistência não deve determinar a arquitetura do produto antes da existência de uma necessidade correspondente.

```text
NECESSIDADE ATUAL
       ↓
Persistência simples
       ↓
Atende aos requisitos?
   ├── SIM → manter
   │
   └── NÃO
        ↓
Identificar nova necessidade
        ↓
Avaliar PostgreSQL