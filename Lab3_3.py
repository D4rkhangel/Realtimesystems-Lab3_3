from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from random import randint
import random

Window.system_size = [300,600]
Window.clearcolor = (.83,.5,.5, .5)
LabelBase.register(name='Got',
                   fn_regular='BenguiatGothicC_Bold.ttf')

def solve(a, b, c, d, y, mutate_chance=0.1):
    num_pop = 4
    population = [[random.randint(0, int(y / 4)) for i in range(4)] for j in range(num_pop)]
    chance = mutate_chance
    counter = 0
    roots = [i[0] * a + i[1] * b + i[2] * c + i[3] * d for i in population]
    while y not in roots:
        deltas = [1 / abs(i - y) for i in roots]
        chances = [i / sum(deltas) for i in deltas]

        for i in range(int(num_pop / 2)):
            temp = random.uniform(0, 1)
            if temp < chances[0]:
                param1 = population[0]
            elif temp < chances[0] + chances[1]:
                param1 = population[1]
            elif temp < chances[0] + chances[1] + chances[2]:
                param1 = population[2]
            else:
                param1 = population[3]
            param2 = param1
            while param2 == param1:
                temp2 = random.uniform(0, 1)
                if temp2 < chances[0]:
                    param2 = population[0]
                elif temp2 < chances[0] + chances[1]:
                    param2 = population[1]
                elif temp2 < chances[0] + chances[1] + chances[2]:
                    param2 = population[2]
                else:
                    param2 = population[3]
            gene = random.randint(0, 3)
            param1[gene], param2[gene] = param2[gene], param1[gene]
            for j in range(4):
                temp = random.uniform(0, 1)
                if temp < chance:
                    param1[j] += random.choice([-1, 1])
                temp = random.uniform(0, 1)
                if temp < chance:
                    param2[j] += random.choice([-1, 1])
            population[2 * i] = param1
            population[2 * i + 1] = param2
        roots = [j[0] * a + j[1] * b + j[2] * c + j[3] * d for j in population]
        counter += 1
    return population[roots.index(y)], counter

class MainWidget(BoxLayout):
    orientation = 'vertical'
    def solve(self):
        a,b,c,d,y = float(self.a.txt.text), float(self.b.txt.text), float(self.c.txt.text), float(self.d.txt.text), float(self.igrek.txt.text)
        result, numgen = solve(a,b,c,d,y)
        self.x1.text = 'x1 = {0}'.format(result[0])
        self.x2.text = 'x2 = {0}'.format(result[1])
        self.x3.text = 'x3 = {0}'.format(result[2])
        self.x4.text = 'x4 = {0}'.format(result[3])
        mypopup = Factory.MyPopup()
        mypopup.numgen.text = str(numgen)
        mypopup.open()
        
class Lab3_3App(App):
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    Lab3_3App().run()
