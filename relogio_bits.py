#!/usr/bin/env python
import Tkinter

relogio = Tkinter.Label()

relogio.pack()
relogio['text'] = '0'
relogio['font'] = 'Helvetica 120 bold'

contador = 0

def tictac():
    global contador
    agora = '{0:b}'.format(contador)
    contador += 1
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(1000, tictac)

tictac()
relogio.mainloop()
