---
name: magnum-peticiona
description: Skill de estilo, estrutura, redação e organização de pedidos para petições trabalhistas no padrão Magnum. Não substitui análise jurídica do caso concreto.
version: 2.0.0
language: pt-BR
---

# MagnumPeticiona

## 1. Finalidade

Reproduzir o padrão de peticionamento identificado no corpus de referência:
- arquitetura da peça;
- forma de narrar os fatos;
- vocabulário;
- extensão dos tópicos;
- ordem lógica;
- forma de concluir;
- agrupamento de pedidos;
- padrão de dano moral;
- quadro final de pedidos;
- revisão formal.

A skill é de FORMA E PADRÃO. Ela não decide, por si só, quais pedidos são juridicamente cabíveis.

## 2. Hierarquia obrigatória

1. fatos e documentos do caso atual;
2. instruções expressas do usuário;
3. análise jurídica do caso;
4. banco de modelos;
5. preferências estilísticas.

O modelo jamais pode superar os fatos do caso atual.

## 3. Proibições

Nunca:
- inventar fatos;
- inventar jornada;
- inventar salário;
- inventar função;
- importar nome, empresa, cidade, doença, rubrica ou data de outro processo;
- incluir pedido automaticamente porque existe no banco;
- criar jurisprudência;
- alterar toda a petição quando a instrução for “altere apenas o necessário”;
- separar como pedidos independentes subtópicos que pertencem à mesma família.

## 4. Estrutura padrão

### Preâmbulo
DOUTO JUÍZO DA VARA DO TRABALHO DE [LOCAL] – [UF].

Qualificação.

Fórmula de propositura nos termos do art. 840, §1º, da CLT.

### I – DAS CONSIDERAÇÕES INICIAIS
01. DECLARAÇÃO DE ADESÃO AO JUÍZO 100% DIGITAL
02. DA PROTEÇÃO DOS DADOS DA PARTE AUTORA

### II – DA RELAÇÃO JURÍDICA
01. CONTRATO DE TRABALHO
02. JORNADA DE TRABALHO

### III – DA FUNDAMENTAÇÃO JURÍDICA
01. ASSISTÊNCIA JUDICIÁRIA GRATUITA
Demais famílias aplicáveis.

### IV – ANTE AO EXPOSTO, RECLAMA
“IV – ANTE AO EXPOSTO, RECLAMA as seguintes verbas que deverão ser apuradas em liquidação de sentença:”

### V – REQUERIMENTOS
Notificação; procedência; provas; Juízo 100% Digital; proteção de dados; demais requerimentos efetivamente aplicáveis; valor da causa; fechamento.

## 5. Fórmula de construção dos tópicos

FATO → FUNDAMENTO → INCIDÊNCIA → PEDIDO.

Todo tópico de mérito deve terminar com requerimento expresso quando contiver uma pretensão.

Conectores compatíveis:
- Cumpre destacar;
- Ora;
- Denota-se;
- Não obstante;
- Destarte;
- Desta feita;
- Assim;
- Diante do exposto;
- Ante o exposto;
- No caso em tela;
- No âmbito do labor.

## 6. Famílias de pedidos

A numeração decimal indica pertencimento à mesma família.

Exemplo:
3
3.1
3.2
3.3

= UMA família de pedido.

Aplicar a mesma regra a:
- reversão da justa causa e seus fundamentos;
- doença ocupacional e responsabilidades/danos/perícia;
- intrajornada e horas laboradas no intervalo;
- trabalho extraturno, sobreaviso e celular próprio;
- bonificação, desempenho, liberalidade e diferenças;
- pedido principal e subsidiário.

Reflexos também pertencem ao pedido principal.

Consultar `references/pedido_catalogo.json`.

## 7. Dano moral/extrapatrimonial

Todo tópico de dano moral deve:
1. individualizar o fato gerador;
2. narrar a repercussão concreta;
3. ligar a conduta ao bem jurídico atingido;
4. terminar com a matriz obrigatória descrita em `references/dano-moral.md`;
5. adaptar fato gerador, valor, gênero, número e enquadramento ao caso concreto.

Nunca deixar no fechamento “ausência de anotação em CTPS” quando o dano decorrer de outro fato.

## 8. Modos

### CRIAR
Criar novo tópico ou peça no padrão.

### ADEQUAR
Preservar integralmente a peça-base e alterar somente o necessário.

### REVISAR
Corrigir formalmente sem reescrever desnecessariamente.

### BANCO
Recuperar modelo compatível sem decidir a pertinência jurídica.

### AUDITAR
Comparar fundamentação, pedidos e quadro final.

## 9. Regras de preservação

Quando o usuário disser:
- “mantenha na íntegra”;
- “não suprima”;
- “altere apenas o necessário”;
- “não mexa nos demais tópicos”;

a skill deve obedecer literalmente.

## 10. Validação final

Sempre executar:
- `references/checklist-consistencia.md`;
- `references/fontes-e-validacao.md`;
- `scripts/validate_petition.py`, quando o conteúdo estiver disponível como arquivo de texto/markdown.

## 11. Regra de saída

O texto deve parecer continuação natural das peças-modelo, não uma redação jurídica genérica produzida por IA.
