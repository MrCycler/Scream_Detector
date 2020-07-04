import librosa as lr
import random

def sample_generator(out_path,base_path,scream_path):
  # lee el grito
  audio='arabic6'
  y_scream, sr = lr.load(scream_path.format(audio))
  # obtiene la duracion del grito
  duration = lr.get_duration(y=y_scream, sr=sr)
  # el grito dura 1 segundo
  y_reduce_scream = lr.effects.time_stretch(y_scream, duration)
  # lee el audio base
  y_base, sr = lr.load(base_path.format(audio))
  # obtiene la duracion base
  duration_base = lr.get_duration(y=y_base, sr=sr)
  if duration_base >2.9:
    # obtiene el indice inicial (aleatorio)
    init_index = random.randint(0,(y_base.size-y_reduce_scream.size-1))
    # Inicializa el audio de salida
    y_out = y_base
    # fusiona los audios
    i = 0
    while i < y_reduce_scream.size:
        y_out[i+init_index]=y_reduce_scream[i]+y_base[i+init_index]
        i = i + 1
    # guarda el audio
    lr.output.write_wav(out_path, y_out, sr)
    return (duration_base*init_index/y_base.size)
  else:
    return -1
