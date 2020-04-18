import requests
import cloudinary

audio_file = open("some-audio.mp3", 'r')
audio_file = audio_file.read()
my_byte_array = bytearray(audio_file)

upload_url = "https://api.cloudinary.com/v1_1/dyed10v2u/video/upload"

res = requests.post(upload_url, json={
  'file': my_byte_array[0],
  'upload_preset': "zvitw4hs"
})

print(res.__dict__)

