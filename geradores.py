from config import criar_cliente

client = criar_cliente()

def gerar_roteiro_narrativo(titulo_livro, autor_livro):
    prompt = f"""
    Crie um roteiro de vídeo completo e narrativo para o livro "{titulo_livro}" de {autor_livro} seguindo ESTAS REGRAS:

    1. Texto 100% contínuo sem títulos ou marcadores
    2. Tom conversacional como diálogo íntimo
    3. Estrutura invisível com introdução, 2 pontos-chave e conclusão
    4. Transições naturais entre ideias
    5. Inclua:
       - Gancho inicial impactante
       - 1 ensinamento principal com exemplo do autor
       - 1 história paradoxal do livro
       - 2 perguntas retóricas
       - Call-to-Action sutil no final
    6. Formato:
       - Sem aspas
       - Parágrafos curtos para respiração
       - Palavras de transição naturais (agora, mas atenção, veja só)
       - Duração de aproximadamente 1 minuto (100-150 palavras)

    Estilo do canal: Dark intellectual com suspense filosófico
    """


    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Você é um escritor-fantasma especializado em roteiros para booktubers dark"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.85,
        max_tokens=1200,
        top_p=0.95
    )

    return response.choices[0].message.content





def gerar_prompts_imagens(roteiro):
    prompt_imagens = f"""
    Com base neste roteiro de vídeo:
    {roteiro}

    Gere exatamente 10 prompts para IA de imagem seguindo estas regras:

    1. **Formato por prompt:**
       - [PT-BR]: Descrição detalhada em português.

    2. **Características obrigatórias:**
       - Estilo: Cinematográfico e artístico, com iluminação bem trabalhada.
       - Paleta de cores: Estética refinada, explorando tons contrastantes de forma harmônica.
       - Elementos: Simbologia conceitual e filosófica inspirada na narrativa.
       - Enquadramento: Uso de composições dinâmicas para impacto visual.

    3. **Requisitos de conteúdo:**
       - Representar 1 cena-chave por prompt.
       - Incluir elementos metafóricos do texto.
       - Usar analogias visuais dos conceitos do livro.
       - Variar entre cenas figurativas e abstratas.

    4. **Regras de moderação:**
       - Evitar qualquer conteúdo que infrinja políticas de IA.
       - Não incluir representações de pessoas reais ou imagens politicamente sensíveis.
       - Garantir que todas as descrições sigam diretrizes éticas.

    5. **Terminologia técnica:**
       - Incluir termos como "cinematic lighting", "detailed textures", "high-resolution".
       - Especificar "8K render", "artistic composition", "digital painting".
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Você é um diretor de arte especializado em gerar prompts para IAs visuais, garantindo conformidade com diretrizes de moderação."},
            {"role": "user", "content": prompt_imagens}
        ],
        temperature=0.8,
        max_tokens=2000,
        top_p=0.9
    )

    resultado = response.choices[0].message.content
    print("\n=== Prompts Gerados ===\n")
    print(resultado)
    return resultado
