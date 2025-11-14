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


"# Chemstore3"  
