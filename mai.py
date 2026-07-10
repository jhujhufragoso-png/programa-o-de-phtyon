# Mapeamento dos papéis do time de desenvolvimento
papeis_scrum = {
    "Product Owner (PO)": {
        "Responsabilidades": [
            "Validar as entregas (aceitar ou rejeitar resultados)",
            "Decidir o que será desenvolvido em cada Sprint"
        ],
        "Habilidades": ["Visão de negócio", "Comunicação clara", "Capacidade de priorização"]
    },
    "Scrum Master (SM)": {
        "Responsabilidades": [
            "Facilitar eventos como Daily, Planning, Review e Retrospective",
            "Remover impedimentos que atrapalham o time",
            "Proteger o time de interferências externas"
        ],
        "Habilidades": ["Liderança servidora", "Resolução de conflitos", "Conhecimento ágil"]
    },
    "Tech Lead (Líder Técnico)": {
        "Responsabilidades": [
            "Ajudar a equipe a resolver desafios técnicos complexos",
            "Mentoria para desenvolvedores menos experientes",
            "Participar de decisões sobre tecnologias e ferramentas"
        ],
        "Habilidades": ["Conhecimento técnico aprofundado", "Capacidade de mentoria"]
    },
    "Developers (Time de Desenvolvimento)": {
        "Responsabilidades": [
            "Auto-organização para distribuir tarefas",
            "Participar ativamente dos eventos do Scrum",
            "Estimar esforço das tarefas (Planning Poker)",
            "Ajudar a melhorar processos (Retrospectivas)"
        ],
        "Habilidades": ["Colaboração", "Autonomia", "Habilidades técnicas"]
    }
}

# Exibindo os dados formatados
for papel, info in papeis_scrum.items():
    print(f"=== {papel} ===")
    print("Responsabilidades:")
    for resp in info["Responsabilidades"]:
        print(f"  - {resp}")
    print(f"Habilidades Chave: {', '.join(info['Habilidades'])}")
    print("-" * 40)