from pydub import AudioSegment
from pydub.playback import play
import sys

audio = AudioSegment.from_file(sys.argv[1])
play(audio)
