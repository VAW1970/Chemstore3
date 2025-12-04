# Chemstore - Sistema de Gerenciamento de Reagentes

Sistema Django para gerenciamento de reagentes químicos com interface admin moderna usando Jazzmin.

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Crie um superusuário:
```bash
python manage.py createsuperuser
```

4. Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

5. Acesse o admin em: http://127.0.0.1:8000/admin/

## Funcionalidades

- Gerenciamento de reagentes químicos
- Controle de validade com filtro de vencimento (30 dias)
- Localização e organização por setor e prateleira
- Interface admin moderna com Jazzmin
- Suporte a múltiplas unidades de medida (g, mL, kit, kg, un.)
- Ícone e logo personalizados
- **Relatório de Reagentes**: Relatório elegante e profissional com visual limpo, estatísticas de validade e otimização para impressão

## Configuração de Ícone e Logo

Para usar um ícone e logo personalizados:

1. Coloque o arquivo de ícone em `static/images/icon.png` (recomendado: 32x32 ou 64x64 pixels)
2. Coloque o arquivo de logo em `static/images/logo.png` (recomendado: 200x50 pixels ou proporção similar)
3. Formatos suportados: PNG, ICO, SVG
4. Reinicie o servidor Django após adicionar os arquivos

## Modelos

### Reagents
Modelo principal para armazenar informações sobre reagentes:
- Nome do reagente
- Marca
- Quantidade e unidade
- Data de validade
- Localização (local, prateleira, setor)
- Usuário responsável
- Data de verificação

### Filtros Admin
- **ExpiringSoonFilter**: Filtra reagentes que vencem em até 30 dias

## Relatório de Reagentes

O sistema inclui uma funcionalidade avançada de relatório de reagentes com as seguintes características:

### Funcionalidades do Relatório
- **Design Elegante**: Interface moderna com gradientes e layout profissional
- **Indicadores Visuais**: Status de validade com cores (normal, aviso, vencido)
- **Estatísticas Resumidas**: Contagem total, vencendo em 30 dias e vencidos
- **Informações Completas**: Nome, marca, quantidade, validade, localização e setor
- **Otimização para Impressão**: CSS específico para impressão sem elementos desnecessários
- **Responsivo**: Funciona bem em diferentes tamanhos de tela

### Como Acessar
1. Acesse o admin em: http://127.0.0.1:8000/admin/
2. Vá para "Reagentes" no menu lateral
3. Clique no botão "📊 Relatório de Reagentes"
4. Visualize ou imprima o relatório

### Recursos Técnicos
- Protegido por autenticação
- Dados em tempo real
- Indicadores visuais automáticos baseados nas datas de validade
- Botão de impressão integrado

"# Chemstore3"  
