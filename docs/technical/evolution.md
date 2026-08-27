# Evolução Técnica do SPUR

## Visão geral

O SPUR nasceu como uma solução para um problema operacional específico: detectar quando conteúdos previamente conhecidos são realocados dentro de uma estrutura de armazenamento.

O projeto evolui de forma incremental, utilizando cada versão para responder a uma pergunta técnica diferente.

---

## V1 — Conceito inicial

A primeira versão buscou validar a possibilidade de observar uma estrutura de arquivos e identificar alterações entre execuções.

O foco estava na viabilidade do monitoramento.

### Aprendizado

Monitorar uma estrutura ampla era tecnicamente possível, mas produzia um universo de análise maior do que o necessário para o problema real.

---

## V2 — Otimização da observação

A segunda versão buscou melhorar a eficiência da varredura e a organização do estado persistido.

O projeto começou a tratar de forma mais explícita:

- descoberta de arquivos;
- representação do estado;
- persistência;
- comparação entre execuções.

### Aprendizado

Reduzir processamento não era suficiente. Também era necessário melhorar a interpretação das mudanças encontradas.

---

## V3 — Identificação e comparação

A terceira versão aprimorou a identificação dos conteúdos e a lógica utilizada para reconhecer movimentações.

O desenvolvimento mostrou que uma solução tecnicamente mais abrangente não necessariamente produz uma solução operacionalmente melhor.

### Aprendizado

O escopo monitorado ainda era amplo demais em relação à necessidade original.

---

## V4 — Proof of Concept funcional

A V4 representa o primeiro marco funcional consolidado do SPUR.

A principal mudança foi a especialização do problema.

Em vez de tentar observar indiscriminadamente toda a estrutura, a solução passou a trabalhar com um recorte definido e com uma regra operacional específica.

A V4 validou comportamentos como:

- criação de baseline;
- catalogação de conteúdos;
- persistência do estado conhecido;
- comparação entre execuções;
- diferenciação entre conteúdo novo e conteúdo realocado;
- detecção de mudança de localização;
- agrupamento de realocações;
- silêncio quando nenhuma alteração relevante ocorre;
- geração de notificação;
- registro por logs;
- execução periódica.

### Resultado

A lógica principal foi validada em ambiente real por meio de um teste controlado de realocação.

A V4 passa a ser preservada como referência funcional.

Ela não será utilizada como base para crescimento indefinido do código.

---

## V4.5 — Validação de distribuição macOS

A V4.5 representa uma etapa intermediária entre a prova de conceito e a arquitetura de produto.

Seu objetivo é responder:

> O SPUR consegue funcionar corretamente em outra máquina, fora do ambiente original de desenvolvimento?

A versão deverá ser preparada para instalação e utilização em uma segunda máquina macOS.

### Critérios de validação

A V4.5 deverá demonstrar:

- instalação em outra máquina;
- configuração sem alteração do código-fonte;
- acesso ao armazenamento configurado;
- criação correta de baseline;
- persistência entre execuções;
- detecção de uma realocação;
- entrega de notificação;
- geração de logs;
- execução automática;
- funcionamento independente da máquina original.

### Limite arquitetural

A V4.5 não será tratada como a arquitetura definitiva do produto.

Seu objetivo é validar distribuição e uso externo da solução existente.

---

## V5 — Arquitetura de produto

A V5 representa uma mudança de natureza do projeto.

O objetivo deixa de ser apenas possuir uma automação funcional e passa a ser construir um software:

- organizado;
- testável;
- documentado;
- desacoplado;
- configurável;
- preparado para múltiplas plataformas.

A arquitetura será baseada na separação:

```text
SPUR V5
   │
   ├── CORE
   │
   │   ├── regras
   │   ├── estados
   │   ├── arquivos
   │   ├── eventos
   │   └── comparação
   │
   ├── PLATFORM
   │   ├── macOS
   │   └── Windows
   │
   ├── TESTS
   │
   └── DOCS