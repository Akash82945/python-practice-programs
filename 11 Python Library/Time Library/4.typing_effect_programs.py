# import time 
# import sys
# import os

# os.system("cls" if os.name == 'nt' else 'clear')

# message = "Hii, My Name is Akash Kumar."

# for word in message:
#     sys.stdout.write(word)
#     sys.stdout.flush()
#     time.sleep(0.5)



# import time
# message = "Hii, my name is Akash Kumar"
# words = message.split()
# for char in words:
#     print(f" {char}",end="")
    # time.sleep(0.5)
    
    
    
# import time
# for i in range(5,0,-1):
#     print(f"Remaning Time {i} second",end="\r")
#     time.sleep(1)
# print("Programs is end")




# import time
# import sys

# print("File downloding....")
# for i in range(5):
#     sys.stdout.write('.')
#     sys.stdout.flush()
#     time.sleep(0.6)
    
    
    

import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

# शुरुआती 30 सेकंड का सटीक लिरिक्स डेटा
babuaan_30sec = [
    ("🎵 [शिल्पी राज]: गोरखपुर गया छपरा मऊ में...", 3.2),
    ("🎵 [शिल्पी राज]: गइनी गाज़ीपुर गोन्डा लखनऊ में...", 3.5),
    ("🎵 [शिल्पी राज]: हो गोरखपुर गया छपरा मऊ में...", 3.2),
    ("🎵 [शिल्पी राज]: गइनी गाज़ीपुर गोन्डा लखनऊ में...", 3.5),
    ("🎵 [शिल्पी राज]: कवनो सवाद नाहीं मिला...", 3.0),
    ("🎙️ [पवन सिंह]: अरे बना तारू टाइट तऽ हो जईबू ढीला...", 3.5),
    ("🎙️ [पवन सिंह]: प्रखंड हो या जिला, बबुआने से हिला! 🔥", 3.0),
    ("🎙️ [पवन सिंह]: हाँ, प्रखंड हो या जिला, बबुआने से हिला...", 3.0)
]


print("Babuan Song Lyrics. ===")
time.sleep(2) 

for line,delay in babuaan_30sec:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
    
    time.sleep(delay)
    print()