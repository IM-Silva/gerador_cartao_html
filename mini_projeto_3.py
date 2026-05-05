print(" ___ Gerador de Cartão ___")
name = input(" Digite seu nome: ")
occupation = input("Digite sua profissão: ")
color = input(" Digite sua cor preferida em inglês: ")
codigo_html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Gerador de Cartão</title>
<style>
        body{{
            margin:0;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            background-color: rgb(27, 27, 33);
            color: rgb(24,24,24);
            font-family:Verdana, Geneva, Tahoma;
            display: flex;
            justify-content: center;
            align-items: center;
        }}  
        .card{{
            width : 25%;
            height:25%;
            border-radius: 20px;
            background-color:{color};
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
            
    </style>
</head>
<body>
    <div class="card">
        <h1>{name}</h1>
        <h3>{occupation}</h3>
    </div>
</body>
</html>
"""
print(codigo_html)