from tkinter import *
import random
import time

window = Tk()
window.title('Type Speed Test')
window.geometry('700x700')
window.option_add("*Font", "arial 50")

def keyPress(event):
    if event.char.lower() == labelRight.cget('text')[0].lower():
        labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
        labelRight.configure(text=labelRight.cget('text')[1:])
    if not labelRight.cget('text'):
        stopTest()

def resetTest():
    global labelLeft, labelRight, timeLabel, startTime
    text = random.choice(text_samples).lower()
    labelLeft = Label(window, text='')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)
    labelRight = Label(window, text=text)
    labelRight.place(relx=0.5, rely=0.5, anchor=W)
    timeLabel = Label(window, text='00:00.000')
    timeLabel.place(relx=0.5, rely=0.4, anchor=S)
    window.bind('<Key>', keyPress)
    startTime = time.time()
    updateTimer()

def stopTest():
    window.unbind('<Key>')
    words = len(labelLeft.cget('text').split())
    Label(window, text=f'WPM: {words}', fg='black').place(relx=0.5, rely=0.4, anchor=CENTER)
def updateTimer():
    if labelRight.cget('text'):
        elapsed = time.time() - startTime
        mins, secs = divmod(elapsed, 60)
        millis = int((elapsed - int(elapsed)) * 1000)
        timeLabel.configure(text=f'{int(mins):02}:{int(secs):02}.{millis:03}')
        window.after(10, updateTimer)

text_samples = [
    "The quick brown fox jumps over the lazy dog while the sun sets behind the hills casting a golden hue across the valley Birds sing melodious tunes in the trees and the wind whispers softly through the leaves",
    "In the middle of the night the city lights shimmer like stars scattered across the skyline The streets are quiet with only the faint sound of distant traffic and the occasional footstep echoing through the alleyways",
    "As the waves crashed against the rocky shore the salty breeze filled the air The sky was painted in hues of orange pink and purple as the sun began its descent into the horizon marking the end of another beautiful day",
    "The forest was alive with the sound of rustling leaves and chirping crickets Sunlight filtered through the dense canopy above casting dappled shadows on the forest floor In the distance a stream trickled peacefully its water clear and cool",
    "Time is a river that flows without end and we are all travelers upon its waters Each moment like a droplet is swept away into the past never to return Yet the journey is what defines us shaping who we are and who we will become",
    "The mountain loomed in the distance its snow capped peak piercing the sky Climbing its rugged slopes was a challenge but for those who dared the reward was an unparalleled view of the world below stretching out in every direction",
    "A gentle breeze stirred the golden fields of wheat creating ripples that danced across the land The sun shone brightly casting long shadows and warming the earth In the distance a small farmhouse sat quietly its chimney puffing out a thin wisp of smoke",
    "In the depths of space distant stars twinkle like tiny diamonds scattered across a vast endless canvas Planets orbit around their suns while comets streak through the darkness their icy tails lighting up the cosmic expanse",
    "The sound of footsteps echoed down the empty hallway the only noise breaking the stillness of the night A door creaked open slowly revealing a dimly lit room filled with books maps and strange artifacts each with a story waiting to be discovered",
    "Beneath the surface of the ocean a world of wonder awaits Coral reefs teem with colorful fish while whales glide majestically through the deep blue waters The ocean is a vast mysterious realm home to creatures both familiar and unknown"
]


resetTest()
window.mainloop()
