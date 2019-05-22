from ExampleWatsonSTT import ExampleWatsonSTT
watson_stt = ExampleWatsonSTT()
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir("data/audio_files_16khz/"):
	audio_file_path = os.path.join(dir_path,"data/audio_files_16khz/", file)
	recognize_output = watson_stt.recognize(audio_file_path=audio_file_path)
	watson_stt.handle_recognize(recognize_output, file)
