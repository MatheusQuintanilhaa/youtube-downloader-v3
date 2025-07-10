# 🎬 YouTube Downloader v3 - Tudo Embutido

![Python Version](https://img.shields.io/badge/Python-3.6+-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat-square)

> **Script Python profissional e otimizado para download de vídeos do YouTube**  
> *Com legendas e thumbnails automaticamente integradas ao arquivo final*

---

## ✨ Características Principais

### 🏆 Qualidade Premium

- **Melhor qualidade disponível** (até 8K se disponível)
- **1080p Full HD** (recomendado)
- **720p HD** (para conexões lentas)

### 📝 Legendas Inteligentes

- **Automáticas** em português e inglês
- **Embutidas permanentemente** no vídeo
- **Compatível** com todos os players

### 🖼️ Visual Profissional

- **Thumbnail como capa** do arquivo
- **Metadados completos** integrados
- **Arquivos organizados** automaticamente

### ⚡ Performance Otimizada

- **Interface amigável** com menu interativo
- **Limpeza automática** de arquivos temporários
- **Baseado em yt-dlp** para máxima velocidade

## 📋 Pré-requisitos

### 🐍 Python 3.6+

```bash
# Verificar versão instalada
python --version
```

### 📚 Biblioteca yt-dlp

```bash
# Instalar dependência principal
pip install yt-dlp
```

### 🔧 FFmpeg (Essencial)

> **⚠️ Importante:** O FFmpeg é obrigatório para embutir legendas e thumbnails!

#### 🪟 Windows

**Opção 1: Download Manual**

1. Baixe em: <https://ffmpeg.org/download.html>
2. Extraia e adicione `bin` ao PATH do sistema

**Opção 2: Chocolatey**

```powershell
choco install ffmpeg
```

#### 🍎 macOS

```bash
brew install ffmpeg
```

#### 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update && sudo apt install ffmpeg
```

### ✅ Verificação

```bash
# Confirmar se tudo está instalado
python --version
pip show yt-dlp
ffmpeg -version
```

## 🚀 Instalação e Uso

### 📦 Instalação Rápida

1. **Clone o repositório**

   ```bash
   git clone https://github.com/MatheusQuintanilhaa/youtube-downloader-v3.git
   cd youtube-downloader-v3
   ```

2. **Instale as dependências**

   ```bash
   pip install yt-dlp
   ```

3. **Execute o script**

   ```bash
   python youtube_downloader.py
   ```

### 🎯 Como Usar

> **💡 Dica:** Certifique-se de ter o FFmpeg instalado para melhor experiência!

1. **Execute o script** - O menu principal será exibido
2. **Escolha a qualidade:**
   - `1` → Melhor qualidade possível (pode ser 4K, 8K, etc.)
   - `2` → 1080p Full HD (recomendado)
   - `3` → 720p HD (para conexões lentas)
3. **Cole a URL** - Digite ou cole o link do vídeo do YouTube
4. **Aguarde o download** - O script fará tudo automaticamente! ✨

### 🔧 Exemplo de Uso

```bash
$ python youtube_downloader.py

==================================================
🎬 YouTube Downloader v3 - Tudo Embutido 🎬
==================================================

MENU DE OPÇÕES:
1. 🏆 Baixar vídeo em Melhor Qualidade Possível
2. 📺 Baixar vídeo em 1080p (Full HD)  
3. 💻 Baixar vídeo em 720p (HD)
4. ❌ Sair

Escolha uma opção (1-4): 2
Digite a URL do vídeo do YouTube: https://youtube.com/watch?v=...

🚀 Iniciando download...
✅ Download concluído!
```

## 📁 Estrutura do Projeto

```
youtube-downloader-v3/
│
├── 📄 youtube_downloader.py    # Script principal
├── 📖 README.md               # Documentação
├── 📋 LICENSE                 # Licença MIT
└── 📂 downloads/              # Pasta dos vídeos baixados
    └── 🎥 [seus vídeos].mp4
```

## 🎯 Funcionalidades em Detalhes

### 🏆 Download Inteligente

- **Formato otimizado**: Sempre busca MP4 com melhor qualidade de vídeo e áudio
- **Fallback automático**: Se a qualidade escolhida não existir, baixa a melhor disponível
- **Merge automático**: Combina vídeo e áudio em um único arquivo

### 📝 Sistema de Legendas

- **Multi-idioma**: Prioriza português (pt) e inglês (en)
- **Dupla fonte**: Legendas manuais do autor + legendas automáticas do YouTube
- **Embutidas permanentemente**: Funcionam em qualquer player de vídeo

### 🖼️ Thumbnail Integrada

- **Capa automática**: A thumbnail do YouTube vira a capa do arquivo MP4
- **Compatibilidade universal**: Windows Explorer, VLC, Plex, etc.
- **Qualidade preservada**: Mantém a resolução original da imagem

### 🧹 Limpeza Inteligente

- **Auto-cleanup**: Remove arquivos `.vtt`, `.webp` e temporários
- **Verificação segura**: Aguarda conclusão antes de limpar
- **Resultado final**: Apenas o arquivo MP4 completo

## ⚠️ Solução de Problemas

### ❌ "FFmpeg não encontrado"

**Problema:** Script avisa que FFmpeg não está instalado

**Solução:**

1. Instale o FFmpeg seguindo as instruções acima
2. Reinicie o terminal/prompt
3. Teste com: `ffmpeg -version`

### ❌ "Erro ao baixar"

**Possíveis causas:**

- **URL inválida**: Verifique se o link do YouTube está correto
- **Vídeo restrito**: Alguns vídeos podem estar privados ou bloqueados
- **Conexão instável**: Verifique sua internet

### ❌ "Arquivo final não encontrado"

**Soluções:**

- **Aguarde**: Vídeos grandes podem demorar para processar
- **Espaço em disco**: Verifique se há espaço suficiente
- **Permissões**: Execute como administrador se necessário

### 📝 Formato dos Arquivos

Os vídeos são salvos automaticamente como:

```text
Nome do Vídeo [Resolução].mp4
```

**Exemplo:**

```text
Como Programar em Python - Tutorial Completo [1080p].mp4
```

## 🔧 Personalização

### 📂 Alterar Pasta de Download

Edite a linha 41 no script:

```python
output_path: str = "sua_pasta_aqui"  # Mude para sua pasta preferida
```

### 🌍 Adicionar Mais Idiomas

Edite a linha 53 no script:

```python
'subtitleslangs': ['pt', 'en', 'es', 'fr', 'de'],  # Adicione códigos de idioma
```

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

### ⚖️ Uso Responsável e Legal

**Este software é uma ferramenta educacional e para uso pessoal.** Assim como outros projetos similares (youtube-dl, yt-dlp), ele é legal e amplamente usado pela comunidade de desenvolvedores.

#### ✅ **Usos Permitidos**

- Download para uso pessoal e privado
- Backup de seus próprios vídeos
- Uso educacional e de pesquisa
- Análise de conteúdo para fins acadêmicos

#### ❌ **Usos NÃO Recomendados**

- Redistribuição comercial de conteúdo baixado
- Violação dos Termos de Serviço do YouTube
- Download de conteúdo protegido por direitos autorais para distribuição

#### 📋 **Responsabilidades do Usuário**

- **Cumprir as leis locais** sobre direitos autorais
- **Respeitar os Termos de Serviço** do YouTube
- **Usar apenas para fins legítimos** conforme permitido em sua jurisdição
- **Não distribuir conteúdo** sem a devida autorização

**Nota Legal:** Os autores deste software não são responsáveis pelo uso inadequado da ferramenta. O usuário assume total responsabilidade pelo cumprimento das leis aplicáveis.

## 🤝 Suporte

Se encontrar problemas ou tiver sugestões, verifique:

1. Se todos os pré-requisitos estão instalados
2. Se a URL do vídeo está correta
3. Se há espaço suficiente no disco
4. Se o FFmpeg está funcionando corretamente

---

## 🛡️ Disclaimer

**Este script é para uso pessoal e educacional.**

- ✅ Use com responsabilidade
- ✅ Respeite os direitos autorais  
- ✅ Cumpra os Termos de Serviço do YouTube
- ✅ Não distribua conteúdo protegido

---

**⭐ Se este projeto te ajudou, considere dar uma estrela! ⭐**


