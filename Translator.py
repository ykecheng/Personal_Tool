from tkinter import *
import  googletrans
import textblob
from tkinter import ttk, messagebox
import deepl

root = Tk()
root.title('Translator')
root.geometry("880x600")

deepl_translator_conn = deepl.Translator('ecc1526c-5ebe-05e6-424c-ffd36ff07789:fx')

def translate_it():
    translated_text.delete(1.0,END)
    deepl_translated_text.delete(1.0, END)
    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
                if from_language_key == 'zh-cn':
                    from_language_key = 'ZH'
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key
                if to_language_key == 'zh-cn':
                    to_language_key = 'ZH'
                to_deepl_language_key = to_language_key
                if to_language_key == 'en':
                    to_deepl_language_key = 'EN-US'
        words = textblob.TextBlob(original_text.get(1.0,END))

        google_words = words.translate(from_lang=from_language_key,to=to_language_key)
        deepl_words = deepl_translator_conn.translate_text(text=str(words),source_lang=from_language_key,target_lang=to_deepl_language_key).text
        #Output translated text  to screen
        translated_text.insert(1.0,google_words)
        deepl_translated_text.insert(1.0, deepl_words)
    except Exception as e:
        messagebox.showerror("Translator",e)

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)
    deepl_translated_text.delete(1.0, END)

#Grab Language List from GoogleTrans
languages = googletrans.LANGUAGES
#Convert to list
language_list = list(languages.values())

#Test boxes
original_text = Text(root,height = 10, width = 40)
original_text.grid(row=0,column=0,pady=20,padx=10)
original_text.insert(1.0,'Enter your words')

translator_button = Button(root,text = "Translate", font=("Helvetica",24),command=translate_it)
translator_button.grid(row=0,column=1,padx=10)

translated_text = Text(root,height = 10, width = 40)
translated_text.insert(1.0,'GOOGLE')
translated_text.grid(row=0,column=2,pady=20,padx=10)

deepl_translated_text = Text(root,height = 10, width = 40)
deepl_translated_text.insert(1.0,'DEEPL')
deepl_translated_text.grid(row=2,column=2,pady=20,padx=10)

#Combo boxes
original_combo = ttk.Combobox(root,width=50,values=language_list)
original_combo.current(14)
original_combo.grid(row=1,column=0)

translated_combo = ttk.Combobox(root,width=50,values=language_list)
translated_combo.current(46)
translated_combo.grid(row=1,column=2)

#clear
clear_button = Button(root, text= "Clear", command=clear)
clear_button.grid(row=2,column=1)
root.mainloop()
