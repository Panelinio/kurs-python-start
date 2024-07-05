sentence = "Kurs Pythona jest prosty i przyjemny"
print(len(sentence))
print(sentence[18:24])
print(sentence[7])
print(sentence[12])
print(sentence[-4])
#print(sentence[37]) - poza zakresem
sentence = sentence.replace("u","ó")
sentence = sentence.replace("rz", "ż")
print(sentence)