#!/usr/bin/env python3
"""
YouTube Downloader v3 - Tudo Embutido

Script otimizado para download de vídeos do YouTube em alta resolução.
v3 - Tudo Embutido: Legendas e thumbnail são inseridas no arquivo MP4 final.

DISCLAIMER: Esta ferramenta é destinada apenas para uso pessoal e educacional.
Os usuários são responsáveis por cumprir os Termos de Serviço do YouTube e
as leis de direitos autorais aplicáveis. Este software não encoraja ou
endossa qualquer violação de direitos autorais ou termos de serviço.

Requer: pip install yt-dlp
Licença: MIT (veja LICENSE)
"""

import yt_dlp
import os
import shutil
import time

def check_ffmpeg():
    """Verifica se o FFmpeg está disponível no PATH do sistema."""
    if shutil.which("ffmpeg"):
        print("✅ FFmpeg encontrado no sistema.")
        return True
    else:
        print("❌ AVISO: FFmpeg não foi encontrado no PATH do sistema.")
        print("   Para embutir legendas e thumbnails, o FFmpeg é essencial.")
        print("   Você pode baixá-lo em: https://ffmpeg.org/download.html" )
        return False

def cleanup_extra_files(output_path, final_filename):
    """Limpa arquivos extras (.vtt, .webp, etc.) após serem embutidos."""
    print("\n🧹 Realizando limpeza final de arquivos...")
    base_name = os.path.splitext(final_filename)[0]
    
    time.sleep(1) # Pausa para garantir que os arquivos não estejam em uso

    for filename in os.listdir(output_path):
        # Se o nome do arquivo começa com o nome base, mas não é o vídeo final
        if filename.startswith(base_name) and filename != final_filename:
            try:
                os.remove(os.path.join(output_path, filename))
                print(f"   🗑️ Arquivo extra removido: {filename}")
            except OSError as e:
                print(f"   ⚠️ Não foi possível remover {filename}: {e}")

def download_video(url: str, quality: str = '1080p', output_path: str = "downloads"):
    """
    Baixa um vídeo, embutindo legendas e thumbnail, e limpa os arquivos extras.
    """
    os.makedirs(output_path, exist_ok=True)

    format_selector = {
        'best': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '1080p': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '720p': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }

    output_template = os.path.join(output_path, '%(title)s [%(resolution)s].%(ext)s')

    ydl_opts = {
        'format': format_selector.get(quality, format_selector['best']),
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
        
        # --- Configurações para Embutir Tudo ---
        'writesubtitles': True,      # 1. Baixa as legendas
        'writeautomaticsub': True,
        'subtitleslangs': ['pt', 'en'],
        'embedsubtitles': True,      # 2. EMBUTE as legendas no vídeo
        
        'writethumbnail': True,      # 3. Baixa a thumbnail
        
        'postprocessors': [{
            'key': 'EmbedThumbnail', # 4. EMBUTE a thumbnail como capa
            'already_have_thumbnail': False,
        }],
        # -----------------------------------------
        
        'prefer_ffmpeg': True,
        'keepvideo': False,
        'quiet': True,
        'progress': True,
    }

    print(f"\n🚀 Iniciando download para: {url}")
    print(f"✨ Qualidade: {quality} | Modo: Tudo Embutido")
    print(f"📂 Salvando em: {output_path}")
    print("-" * 50)

    final_filename = ""
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            final_filename_template = ydl.prepare_filename(info_dict)
            final_filename = os.path.splitext(final_filename_template)[0] + '.mp4'

            print(f"⏳ Baixando e processando... Arquivo final: '{os.path.basename(final_filename)}'")
            ydl.download([url])
        
        print("\n✅ Download e processamento concluídos com sucesso!")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {e}")
    
    finally:
        # A limpeza agora vai apagar os arquivos .vtt e .webp originais
        if final_filename and os.path.exists(final_filename):
            cleanup_extra_files(output_path, os.path.basename(final_filename))
        else:
            # Se o arquivo final não foi criado, os temporários podem ter ficado
            print("⚠️ Arquivo final não encontrado. Verificando temporários...")
            cleanup_extra_files(output_path, "NenhumArquivoFinal")


def main():
    """Função principal com menu interativo."""
    print("=" * 50)
    print("🎬 YouTube Downloader v3 - Tudo Embutido 🎬")
    print("=" * 50)

    check_ffmpeg()

    while True:
        print("\nMENU DE OPÇÕES:")
        print("1. 🏆 Baixar vídeo em Melhor Qualidade Possível")
        print("2. 📺 Baixar vídeo em 1080p (Full HD)")
        print("3. 💻 Baixar vídeo em 720p (HD)")
        print("4. ❌ Sair")

        choice = input("\nEscolha uma opção (1-4): ").strip()

        if choice in ['1', '2', '3']:
            url = input("Digite a URL do vídeo do YouTube: ").strip()
            if not url:
                print("❌ URL inválida. Tente novamente.")
                continue

            quality_map = {'1': 'best', '2': '1080p', '3': '720p'}
            download_video(url, quality=quality_map[choice])

        elif choice == '4':
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha de 1 a 4.")

if __name__ == "__main__":
    main()
