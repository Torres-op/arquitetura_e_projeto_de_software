from abc import ABC, abstractmethod

class AudioPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass

class AdvancedAudioPlayer(ABC):
    @abstractmethod
    def playVlc(self, file_name: str):
        pass

    @abstractmethod
    def playMp4(self, file_name: str):
        pass

class VlcPlayer(AdvancedAudioPlayer):
    def playVlc(self, file_name: str):
        print(f"Reproduzindo arquivo VLC. Nome: {file_name}")

    def playMp4(self, file_name: str):
        pass

class Mp4Player(AdvancedAudioPlayer):
    def playVlc(self, file_name: str):
        pass

    def playMp4(self, file_name: str):
        print(f"Reproduzindo arquivo MP4. Nome: {file_name}")

class MediaAdapter(AudioPlayer):
    def __init__(self, audio_type: str):
        self.advanced_music_player = None
        
        if audio_type.lower() == "vlc":
            self.advanced_music_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_music_player = Mp4Player()

    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "vlc":
            self.advanced_music_player.playVlc(file_name)
        elif audio_type.lower() == "mp4":
            self.advanced_music_player.playMp4(file_name)

class AudioPlayer(AudioPlayer):
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp3":
            print(f"Reproduzindo arquivo MP3. Nome: {file_name}") 
        elif audio_type.lower() in ["vlc", "mp4"]:
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)    
        else:
            print(f"Formato inválido. O tipo '{audio_type}' não é suportado.")


if __name__ == "__main__":
    audio_player = AudioPlayer()

    audio_player.play("mp3", "musica_classica.mp3")
    audio_player.play("mp4", "video_clipe.mp4")
    audio_player.play("vlc", "filme_longo.vlc")
    audio_player.play("avi", "video_antigo.avi")