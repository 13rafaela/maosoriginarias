from django.shortcuts import render

def home(request):

    produtos = [
        {
            "categoria": "BIOJOIA",
            "nome": "Colar Cobra Coral",
            "preco": "R$ 80,00",
            "imagem": "maos_originarias/img/colar.png",
        },
        {
            "categoria": "CERÂMICA",
            "nome": "Travessa de Barro",
            "preco": "R$ 120,00",
            "imagem": "maos_originarias/img/travessa.png",
        },
        {
            "categoria": "BIOJOIA",
            "nome": "Colar Cobra Coral",
            "preco": "R$ 75,00",
            "imagem": "maos_originarias/img/colardois.png",
        },
        {
            "categoria": "CERÂMICA",
            "nome": "Cumbuca de Barro",
            "preco": "R$ 40,00",
            "imagem": "maos_originarias/img/cumbuca.png",
        },
    ]

    context = {
        "produtos": produtos
    }

    return render(request, 'home.html', context)


def login(request):
    return render(request, 'login.html')


def produto(request):

    recomendados = [
        {
            "nome": "Vinho de Jenipapo",
            "descricao": "100% Natural e Orgânico",
            "preco": "R$ 60,00",
            "imagem": "maos_originarias/img/vinho.png",
        },
        {
            "nome": "Prato Grafite",
            "descricao": "Comunidade Potiguara Ibirapi",
            "preco": "R$ 130,00",
            "imagem": "maos_originarias/img/prato.png",
        },
        {
            "nome": "Trio de Guardiões da Mata",
            "descricao": "Comunidade Potiguara Ibirapi",
            "preco": "R$ 150,00",
            "imagem": "maos_originarias/img/trio.png",
        },
        {
            "nome": "Conjunto pulseiras e colar",
            "descricao": "Comunidade Potiguara Ibirapi",
            "preco": "R$ 100,00",
            "imagem": "maos_originarias/img/conjuto.png",
        },
    ]

    context = {
        "recomendados": recomendados
    }

    return render(request, 'produto.html', context)