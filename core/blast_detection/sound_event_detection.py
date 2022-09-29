

import numpy as np
import pyaudio
from matplotlib import pyplot as plt
import pandas as pd
import sounddevice as sd

from keras_yamnet import params
from keras_yamnet.yamnet import YAMNet, class_names
from keras_yamnet.preprocessing import preprocess_input

from plot import Plotter

if __name__ == "__main__":

    ################### SETTINGS ###################
    plt_classes = [0,132,420,494] # Speech, Music, Explosion, Silence
    # plt_classes = [420]
    class_labels = True
    FORMAT = pyaudio.paFloat32
    CHANNELS = 1
    RATE = params.SAMPLE_RATE
    WIN_SIZE_SEC = 0.075
    CHUNK = int(WIN_SIZE_SEC * RATE)
    RECORD_SECONDS = 60

    print(sd.query_devices())
    MIC = None

    #################### MODEL #####################
    
    model = YAMNet(weights='C:/Users/admin/Desktop/desktop/gta/DistanceMeasure/core/blast_detection/keras_yamnet/yamnet.h5')
    yamnet_classes = class_names('C:/Users/admin/Desktop/desktop/gta/DistanceMeasure/core/blast_detection/keras_yamnet/yamnet_class_map.csv')

    #################### STREAM ####################
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT,
                        input_device_index=MIC,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")

    if plt_classes is not None:
        plt_classes_lab = yamnet_classes[plt_classes]
        n_classes = len(plt_classes)
    else:
        plt_classes = [k for k in range(len(yamnet_classes))]
        plt_classes_lab = yamnet_classes if class_labels else None
        n_classes = len(yamnet_classes)

    monitor = Plotter(n_classes=n_classes, FIG_SIZE=(12, 6), msd_labels=plt_classes_lab)

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        # Waveform
        data = preprocess_input(np.fromstring(
            stream.read(CHUNK), dtype=np.float32), RATE)
        curr_size = data.shape[0]
        pad_data = data
        if curr_size < 96:
            pad_data = np.zeros((96, 64))
            for j in range(46, 52, curr_size):
                pad_data[j:j+curr_size, 0:64] = data
        # pad_data = data
        prediction = model.predict(np.expand_dims(pad_data, 0))
        # print(prediction)
        print(prediction[0][plt_classes])
        monitor(pad_data.transpose(), np.expand_dims(prediction[0][plt_classes], -1))
        print(i)

    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
