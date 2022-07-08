import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


# Requisito 12
def analyzer_menu():
    op_menu = [
        {
            "command": lambda input: get_tech_news(input),
            "description": "Popular o banco com notícias;\n",
            "prompt": "Digite quantas notícias serão buscadas:",
        },
        {
            "command": lambda input: search_by_title(input),
            "description": "Buscar notícias por título;\n",
            "prompt": "Digite o título:",
        },
        {
            "command": lambda input: search_by_date(input),
            "description": "Buscar notícias por data;\n",
            "prompt": "Digite a data no formato aaaa-mm-dd:",
        },
        {
            "command": lambda input: search_by_tag(input),
            "description": "Buscar notícias por tag;\n",
            "prompt": "Digite a tag:",
        },
        {
            "command": lambda input: search_by_category(input),
            "description": "Buscar notícias por categoria;\n",
            "prompt": "Digite a categoria:",
        },
        {
            "command": lambda: top_5_news(),
            "description": "Listar top 5 notícias;\n",
        },
        {
            "command": lambda: top_5_categories(),
            "description": "Listar top 5 categorias;\n",
        },
        {
            "command": lambda: "Encerrando script",
            "description": "Sair.",
        },
    ]

    print("Selecione uma das opções a seguir:")
    try:
        for index, entry in enumerate(op_menu):
            print(f' {index} - {entry["description"]}', end="")
    except (ValueError, IndexError):
        print("Opção inválida", file=sys.stderr)
