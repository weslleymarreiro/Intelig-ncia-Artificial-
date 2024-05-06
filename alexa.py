import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
from googletrans import Translator

audio = sr.Recognizer()
maquina = pyttsx3.init()
tradutor = Translator()

def fala_inicial():
    maquina.say("Olá! Há quanto tempo! Em que posso ajudar?")
    maquina.runAndWait()
    
def executa_comando():
    try:
       with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'traduza para mim' in comando:
                maquina.say("Por favor, digite o texto.")
                maquina.runAndWait()
                texto = input("Digite o texto: ").lower()
                traducao = tradutor.translate(texto, dest='en').text
                maquina.say(f"A tradução é: {traducao}")
                maquina.runAndWait()
            elif 'ana' in comando:
                comando = comando.replace('ana', '')
                maquina.say(comando)
                maquina.runAndWait()
            
    except Exception as e:
        print('Erro:', e)
        maquina.say("Desculpe, não entendi. Pode repetir?")
        maquina.runAndWait()
            
    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    fala_inicial()
    while True:
        comando = executa_comando()
        if comando:
            if 'que horas são' in comando:
                agora = datetime.datetime.now()
                hora = agora.strftime('%H:%M')
                dia = agora.strftime('%d')
                maquina.say(f"Agora são {hora} e hoje é dia {dia}.")
                maquina.runAndWait()
            elif 'procure por' in comando:
                procurar = comando.replace('procure por', '')
                wikipedia.set_lang('pt')
                resultado = wikipedia.summary(procurar,2)
                print(resultado)
                maquina.say(resultado)
                maquina.runAndWait()
            elif 'toque' in comando:
                musica = comando.replace('toque' ,'')
                resultado = pywhatkit.playonyt(musica)
                maquina.say('Tocando música')
                maquina.runAndWait()
            elif 'obrigado' in comando:
                maquina.say('Até mais!')
                maquina.runAndWait()
                break
        
comando_voz_usuario()