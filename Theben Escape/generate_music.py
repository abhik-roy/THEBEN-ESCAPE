import magenta
import note_seq
from note_seq.protobuf import music_pb2
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel
from magenta.music.protobuf import generator_pb2

# Load the pre-trained model
model_config = configs.CONFIG_MAP['hier-multiperf_vel_2bar_big']
model = TrainedModel(model_config, batch_size=4,
                     checkpoint_dir_or_path='model.ckpt')

# Sample a sequence from the model
z, mu, sigma = model.sample(n=1, length=256, temperature=0.5)
sampled_seq = model.decode(z=z, temperature=0.5)

# Convert the sequence to an MML string
mml_string = note_seq.midi_to_note_sequence(
    sampled_seq.to_sequence()).to_melody_conversion().to_mml()

# Write the MML string to a file
with open('metal.mml', 'w') as f:
    f.write(mml_string)

# Convert the MML file to an audio file
converter_output = magenta.music.midi_io.midi_file_to_sequence_proto(
    'metal.midi')
audio_data = magenta.music.audio_io.sequence_to_pretty_midi(
    converter_output).synthesize(fs=44100)
magenta.music.audio_io.wav_data_to_audio_file(audio_data, 'metal.mp3')
