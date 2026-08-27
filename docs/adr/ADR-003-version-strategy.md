# ADR-003 — Estratégia de evolução V4 → V4.5 → V5

**Status:** Aceito  
**Data:** 27/08/2026  
**Projeto:** SPUR

## Contexto

A V4 do SPUR comprovou funcionalmente a capacidade de detectar realocações de conteúdo em macOS.

Essa versão passa a ser preservada como prova de conceito funcional e referência de comportamento.

Antes da reconstrução arquitetural da V5, foi definida uma etapa intermediária para validar o SPUR fora da máquina original de desenvolvimento.

## Decisão

A evolução do SPUR será dividida em três marcos:

### V4 — Proof of Concept

A V4 permanece congelada como referência funcional.

Seu objetivo foi comprovar que o conceito de monitoramento por comparação de estados funciona em um ambiente real.

### V4.5 — macOS Distribution Validation

A V4.5 terá como objetivo transformar a solução validada em uma aplicação funcional para instalação e teste em uma segunda máquina macOS.

Essa etapa deverá validar:

- instalação;
- configuração externa;
- acesso ao armazenamento configurado;
- criação de baseline;
- persistência de estado;
- detecção de realocação;
- notificações;
- logs;
- execução automática;
- comportamento fora da máquina original de desenvolvimento.

A V4.5 não representa ainda a arquitetura multiplataforma definitiva.

### V5 — Product Architecture

A V5 representará a transformação da prova de conceito em um produto de software estruturado.

Seus objetivos incluem:

- Core independente do sistema operacional;
- separação Core/Platform;
- suporte arquitetural a macOS e Windows;
- testes automatizados;
- documentação técnica;
- configuração desacoplada;
- maior testabilidade e manutenção;
- preparação para distribuição futura.

## Estratégia

```text
V4
POC funcional
      ↓
V4.5
Validação de distribuição macOS
      ↓
V5
Arquitetura de produto multiplataforma