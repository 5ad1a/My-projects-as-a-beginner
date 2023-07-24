#This programmes is a random joke generator, the jokes are stored in a list and output randomly

import random

a = 'What’s the best thing about Switzerland?\n\nI don’t know, but the flag is a big plus.'
b = 'Secretary: “Doctor, the invisible man has come. He says he has an appointment.”\n\nDoctor: “Tell him I can’t see him.”'
c = 'Why aren’t Koalas actual bears?\n\nThey don’t meet the KOALifications.'
d = 'Why are green beans the most Zen of all vegetables?\n\nBecause they’ve found their inner peas.'
e = 'What do you call bears with no ears?\n\nB–'
f = 'What did the 0 say to the 8?\n\nNice belt!'
g = 'What do you call sad coffee?\n\nDespresso.'
h = 'What do you give to a sick lemon?\n\nLemon aid!'
i = 'Why is Peter Pan always flying?\n\nHe neverlands.'
j = 'What’s a frog’s favorite soda?\n\nCroak-a-Cola!'
k = 'Did you hear about the mathematician who’s afraid of negative numbers?\n\nHe’ll stop at nothing to avoid them.'
l = 'A man tells his doctor, “Doc, help me. I’m addicted to Instagram”\n\nThe doctor replies, “Sorry, I don’t follow you …”'
m = 'Hear about the new restaurant called Karma?\n\nThere’s no menu: You get what you deserve.'
n = 'What do you call it when you walk into a cafe you’re sure you’ve been to before?\n\nDéjà brew'
o = 'Have you got anything to drink?\n\nWater\n\nI was thinking about something harder…\n\nI have ice.'

list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]

num = len(list)
r_num = random.randint(0, num)
print(list[r_num])