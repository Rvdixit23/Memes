try:
    import pydub
    from pydub import AudioSegment
    from pydub.playback import play
except ImportError:
    print("Install pydub for cool sound effects")
    print("To install run")
    print("pip install pydub")

from pathlib import Path

def doMachineLearning():
    print("You got placed for a job in Machine Learning")
    song = AudioSegment.from_wav(Path(__file__).parent.__str__() + "/victory.wav")
    play(song, True)

if __name__ == "__main__":
    doMachineLearning()