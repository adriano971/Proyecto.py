"""Este modulo contiene las siguientes funciones destinadas a la inscripción de mensajes"""
"""encrypTex() y decrypTex()"""
    
def encrypTex(tex):    #Esta funcion realiza la codificacion de una cadena de texto.
    dic_1={"A":"%", "B":",", "C":"/", "D":":", "E":"(", "F":"]", "G":"[", "H":"+", "I":"-", "J":")", "K":";", "L":"@", "M":"$", "N":"<", "O":">", "P":"=", "Q":"_", "R":"*", "S":"!", "T":"π", "U":"×", "V":"^", "W":"÷", "X":"•", "Y":".", "Z":"?", " ":" "}
    texto=tex.upper()
    encryp=""
    for i in texto:
        if i in dic_1:
            encryp+=dic_1[i]
        else:
            encryp+=i
    return encryp.lower()



def decrypTex(tex):    #Esta funcion realiza la decodificación de la cadena de texto codificada por la funcion encrypTex.
    dic_2={"%":"A", ",":"B", "/":"C", ":":"D", "(":"E", "]":"F", "[":"G", "+":"H", "-":"I", ")":"j", ";":"K", "@":"L", "$":"M", "<":"N", ">":"O", "=":"P", "_":"Q", "*":"R", "!":"S", "π":"T", "×":"U", "^":"V", "÷":"W", "•":"X", ".":"Y", "?":"z", " ":" "}
    texto=tex.upper()
    decryp=""
    for i in texto:
        if i in dic_2:
            decryp+=dic_2[i]
        else:
            decryp+=i
    return decryp.lower()