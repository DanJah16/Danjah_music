from pytube import YouTube
from colorama import init, Fore, Style
import os
import wget

# Inicializar colorama
init(autoreset=True)

def select_resolution(video):
    available_resolutions = video.streams.filter(file_extension='mp4').order_by('resolution').desc()
    print(f"{Fore.YELLOW}{'-' * 40}")
    print(f"{Fore.CYAN}{'Resoluciones disponibles para el video:':^40}")
    for i, stream in enumerate(available_resolutions, start=1):
        print(f"  {i}. {Fore.GREEN}{stream.resolution:^10}{Style.RESET_ALL}")
    option = int(input(f"{Fore.YELLOW}{'Seleccione la resolución deseada: ':^40}{Style.RESET_ALL}"))
    return available_resolutions[option - 1]

def select_audio_quality(video):
    available_audio = video.streams.filter(only_audio=True).order_by('abr').desc()
    print(f"{Fore.YELLOW}{'-' * 40}")
    print(f"{Fore.CYAN}{'Calidades disponibles para el audio:':^40}")
    for i, stream in enumerate(available_audio, start=1):
        print(f"  {i}. {Fore.GREEN}{stream.abr:^10} kbps{Style.RESET_ALL}")
    option = int(input(f"{Fore.YELLOW}{'Seleccione la calidad deseada: ':^40}{Style.RESET_ALL}"))
    return available_audio[option - 1]

def reload_video(video_url):
    try:
        video = YouTube(video_url)
        print(f"{Fore.GREEN}{'-' * 40}")
        print(f"{Fore.MAGENTA}{'VIDEO ENCONTRADO.':^40} {video.title}")
        print(f"{'-' * 40}{Style.RESET_ALL}")

        print(f"{Fore.YELLOW}{'-' * 40}")
        print(f"{Fore.CYAN}{'OPCIONES DE DESCARGA:':^40}")
        print(f"{Fore.CYAN}{'1. Video (MP4)':^40}")
        print(f"{'  2. Solo Audio (MP3)':^40}")
        print(f"{'-' * 40}{Style.RESET_ALL}")

        option = input(f"{Fore.YELLOW}{'Seleccione la opción deseada: ':^40}{Style.RESET_ALL}")

        if option == "1":
            stream = select_resolution(video)
            print(f"{Fore.YELLOW}{'-' * 40}")
            print(f"{Fore.CYAN}{'DESCARGANDO VIDEO (MP4)':^40}")
            print(f"{'-' * 40}{Style.RESET_ALL}")
            file_name = "danjah_" + video.title + ".mp4"
            destination = os.path.join("/sdcard/", file_name)
            video_stream_url = stream.url
            wget.download(video_stream_url, destination)
            print(f"{Fore.GREEN}{'Descarga de video (MP4) completada.':^40}{Style.RESET_ALL}")
        elif option == "2":
            stream = select_audio_quality(video)
            print(f"{Fore.YELLOW}{'-' * 40}")
            print(f"{Fore.CYAN}{'DESCARGANDO AUDIO (MP3)':^40}")
            print(f"{'-' * 40}{Style.RESET_ALL}")
            file_name = "danjah_" + video.title + ".mp3"
            destination = os.path.join("/sdcard/", file_name)
            audio_stream_url = stream.url
            wget.download(audio_stream_url, destination)
            print(f"{Fore.GREEN}{'Descarga de audio (MP3) completada.':^40}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{'-' * 40}")
            print(f"{'Opción no válida. Asegúrese de seleccionar una opción correcta.':^40}")
            print(f"{'-' * 40}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}{'-' * 40}")
        print(f"{'ERROR DURANTE LA RECARGA:':^40} {e}")
        print(f"{'-' * 40}{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}{'-' * 40}")
    print(f"{'BIENVENIDO A DANJAH VIDEOS.':^40}")
    print(f"{'-' * 40}{Style.RESET_ALL}")
    video_url = input(f"{Fore.YELLOW}{'Ingresa la URL del video que deseas recargar: ':^40}{Style.RESET_ALL}")

    reload_video(video_url)
