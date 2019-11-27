#  ____   ____        .__
#  \   \ /   /  ____  |__|  ____    ____
#   \   Y   /  /  _ \ |  |_/ ___\ _/ __ \
#    \     /  (  <_> )|  |\  \___ \  ___/
#     \___/    \____/ |__| \___  > \___  >
#                              \/      \/
#  __________                             .___
#  \______   \_____     ______  ____    __| _/
#   |    |  _/\__  \   /  ___/_/ __ \  / __ |
#   |    |   \ / __ \_ \___ \ \  ___/ / /_/ |
#   |______  /(____  //____  > \___  >\____ |
#          \/      \/      \/      \/      \/
#  _________          .__
#  \_   ___ \ _____   |  |    ____
#  /    \  \/ \__  \  |  |  _/ ___\
#  \     \____ / __ \_|  |__\  \___
#   \______  /(____  /|____/ \___  >
#          \/      \/            \/
#
import operator
import speech_recognition as s_r
from gtts import gTTS
import os
print("")
r = s_r.Recognizer()
my_mic_device = s_r.Microphone(device_index=1)
with my_mic_device as source:
    print("Say what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
my_string=r.recognize_google(audio)
print(my_string)
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'multiply'  : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]
def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)
Answer = (eval_binary_expr(*(my_string.split())))

tts = gTTS(text= str(Answer), lang='sw')
tts.save("answer.mp3")
os.system("answer.mp3")

print(Answer)

