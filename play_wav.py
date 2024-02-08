import pyaudio
import wave
import sys
import threading


def play_wav(file, device_index=7):
    """
    Playes a wave file on the specified device
    """
    # length of data to read.
    chunk = 1024
    # open the file for reading.
    wf = wave.open(file, 'rb')

    # create an audio object
    p = pyaudio.PyAudio()

    print("Playing " + file)
    #print(wf.getframerate())

    # open stream based on the wave object which has been input.
    stream = p.open(format =
                    p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True,
                    output_device_index=device_index)

    # read data (based on the chunk size)
    data = wf.readframes(chunk)
    
    # play stream (looping from beginning of file to the end)
    while data:
        # writing to the stream is what *actually* plays the sound.
        stream.write(data)
        data = wf.readframes(chunk)

    

    # cleanup stuff.
    wf.close()
    stream.close()    
    p.terminate()

if __name__ == "__main__":
    args = sys.argv[1:]
    thread = threading.Thread(target=play_wav(args[0], int(args[1]) if len(args) > 1 else 7))
    