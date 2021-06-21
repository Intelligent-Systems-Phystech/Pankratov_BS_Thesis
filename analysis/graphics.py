#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


def plotexpresults(results,xarr,title,title1,title2,path):
    "results - результаты count_metrics_for_phi, лежащие в массиве с числом элементво кратным 8 и разделенные запятой. 
    "Результаты для нулевого и ненулевого регуляриазтора идут последовательно
    "xarr - координаты точек по оси x
    "title - название графика
    "title1,title2 - названия осей
    "path - путь сохранения графиков
    "
    "Выход - график, иллюстрирующий значения метрик
    numexps = len(results) // 8
    helreg0 = []
    helreg1 = []
    helreg2 = []
    helnoreg0 = []
    helnoreg1 = []
    helnoreg2 = []
    cosreg0 = []
    cosreg1 = []
    cosreg2 = []
    cosnoreg0 = []
    cosnoreg1 = []
    cosnoreg2 = []
    eucreg0 = []
    eucreg1 = []
    eucreg2 = []
    eucnoreg0 = []
    eucnoreg1 = []
    eucnoreg2 = []
    jenreg0 = []
    jenreg1 = []
    jenreg2 = []
    jennoreg0 = []
    jennoreg1 = []
    jennoreg2 = []
    for i in range (numexps):
        helreg0.append(results[8*i + 7][0])
        helreg1.append(results[8*i + 7][3])
        helreg2.append(results[8*i + 7][4])
        helnoreg0.append(results[8*i + 3][0])
        helnoreg1.append(results[8*i + 3][3])
        helnoreg2.append(results[8*i + 3][4])
        cosreg0.append(results[8*i + 4][0])
        cosreg1.append(results[8*i + 4][3])
        cosreg2.append(results[8*i + 4][4])
        cosnoreg0.append(results[8*i + 0][0])
        cosnoreg1.append(results[8*i + 0][3])
        cosnoreg2.append(results[8*i + 0][4])
        eucreg0.append(results[8*i + 5][0])
        eucreg1.append(results[8*i + 5][3])
        eucreg2.append(results[8*i + 5][4])
        eucnoreg0.append(results[8*i + 1][0])
        eucnoreg1.append(results[8*i + 1][3])
        eucnoreg2.append(results[8*i + 1][4])
        jenreg0.append(results[8*i + 6][0])
        jenreg1.append(results[8*i + 6][3])
        jenreg2.append(results[8*i + 6][4])
        jennoreg0.append(results[8*i + 2][0])
        jennoreg1.append(results[8*i + 2][3])
        jennoreg2.append(results[8*i + 2][4])
    plt.scatter(xarr,cosnoreg0,c=['red'], linewidths = 0.1)
    plt.scatter(xarr,cosreg0,c=['red'], linewidths = 0.25)
    plt.plot(xarr,cosnoreg0,'r-', label='Без регуляризатора, взаимно ближайшие темы',linewidth=1.0)
    plt.plot(xarr,cosreg0,'r-', label='Регуляризатор, взаимно ближайшие темы',linewidth=2.5)
    plt.scatter(xarr,cosnoreg1,c=['blue'], linewidths = 0.1)
    plt.scatter(xarr,cosreg1,c=['blue'], linewidths = 0.25)
    plt.plot(xarr,cosnoreg1,'b--', label='Без регуляризатора, невосстановленные темы',linewidth=1.0)
    plt.plot(xarr,cosreg1,'b--', label='Регуляризатор, невосстановленные темы',linewidth=2.5)
    plt.scatter(xarr,cosnoreg2,c=['green'], linewidths = 0.1)
    plt.scatter(xarr,cosreg2,c=['green'], linewidths = 0.25)
    plt.plot(xarr,cosnoreg2,'g-.', label='Без регуляризатора, ложные темы',linewidth=1.0)
    plt.plot(xarr,cosreg2,'g-.', label='Регуляризатор, ложные темы',linewidth=2.5)
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_4.eps',  bbox_inches='tight',format='eps', transparent=False)
    plt.show()
    plt.scatter(xarr,eucnoreg0,c=['red'], linewidths = 0.1)
    plt.scatter(xarr,eucreg0,c=['red'], linewidths = 0.25)
    plt.plot(xarr,eucnoreg0,'r-', label='Без регуляризатора, взаимно ближайшие темы',linewidth=1.0)
    plt.plot(xarr,eucreg0,'r-', label='Регуляризатор, взаимно ближайшие темы',linewidth=2.5)
    plt.scatter(xarr,eucnoreg1,c=['blue'], linewidths = 0.1)
    plt.scatter(xarr,eucreg1,c=['blue'], linewidths = 0.25)
    plt.plot(xarr,eucnoreg1,'b--', label='Без регуляризатора, невосстановленные темы',linewidth=1.0)
    plt.plot(xarr,eucreg1,'b--', label='Регуляризатор, невосстановленные темы',linewidth=2.5)
    plt.scatter(xarr,eucnoreg2,c=['green'], linewidths = 0.1)
    plt.scatter(xarr,eucreg2,c=['green'], linewidths = 0.25)
    plt.plot(xarr,eucnoreg2,'g-.', label='Без регуляризатора, ложные темы',linewidth=1.0)
    plt.plot(xarr,eucreg2,'g-.', label='Регуляризатор, ложные темы',linewidth=2.5)
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_3.eps',  bbox_inches='tight',format='eps', transparent=False)
    plt.show()
    plt.scatter(xarr,jennoreg0,c=['red'], linewidths = 0.1)
    plt.scatter(xarr,jenreg0,c=['red'], linewidths = 0.25)
    plt.plot(xarr,jennoreg0,'r-', label='Без регуляризатора, взаимно ближайшие темы',linewidth=1.0)
    plt.plot(xarr,jenreg0,'r-', label='Регуляризатор, взаимно ближайшие темы',linewidth=2.5)
    plt.scatter(xarr,jennoreg1,c=['blue'], linewidths = 0.1)
    plt.scatter(xarr,jenreg1,c=['blue'], linewidths = 0.25)
    plt.plot(xarr,jennoreg1,'b--', label='Без регуляризатора, невосстановленные темы',linewidth=1.0)
    plt.plot(xarr,jenreg1,'b--', label='Регуляризатор, невосстановленные темы',linewidth=2.5)
    plt.scatter(xarr,jennoreg2,c=['green'], linewidths = 0.1)
    plt.scatter(xarr,jenreg2,c=['green'], linewidths = 0.25)
    plt.plot(xarr,jennoreg2,'g-.', label='Без регуляризатора, ложные темы',linewidth=1.0)
    plt.plot(xarr,jenreg2,'g-.', label='Регуляризатор, ложные темы',linewidth=2.5)
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_2.eps', bbox_inches='tight',format='eps', transparent=False)
    plt.show()
    plt.scatter(xarr,helnoreg0,c=['red'], linewidths = 0.1)
    plt.scatter(xarr,helreg0,c=['red'], linewidths = 0.25)
    plt.plot(xarr,helnoreg0,'r-', label='Без регуляризатора, взаимно ближайшие темы',linewidth=1.0)
    plt.plot(xarr,helreg0,'r-', label='Регуляризатор, взаимно ближайшие темы',linewidth=2.5)
    plt.scatter(xarr,helnoreg1,c=['blue'], linewidths = 0.1)
    plt.scatter(xarr,helreg1,c=['blue'], linewidths = 0.25)
    plt.plot(xarr,helnoreg1,'b--', label='Без регуляризатора, невосстановленные темы',linewidth=1.0)
    plt.plot(xarr,helreg1,'b--', label='Регуляризатор, невосстановленные темы',linewidth=2.5)
    plt.scatter(xarr,helnoreg2,c=['green'], linewidths = 0.1)
    plt.scatter(xarr,helreg2,c=['green'], linewidths = 0.25)
    plt.plot(xarr,helnoreg2,'g-.', label='Без регуляризатора, ложные темы',linewidth=1.0)
    plt.plot(xarr,helreg2,'g-.', label='Регуляризатор, ложные темы',linewidth=2.5)
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_1.eps', bbox_inches='tight',format='eps', transparent=False)
    plt.show()


# In[3]:


def plotexptauresults(results,xarr,title,title1,title2,path):
    "results - результаты count_metrics_for_phi, лежащие в массиве с числом элементво кратным 4 и разделенные запятой.
    "xarr - координаты точек по оси x
    "title - название графика
    "title1,title2 - названия осей
    "path - путь сохранения графиков
    "
    "Выход - график, иллюстрирующий значения метрик
    numexps = len(results) // 4
    helreg0 = []
    helreg1 = []
    helreg2 = []
    cosreg0 = []
    cosreg1 = []
    cosreg2 = []
    eucreg0 = []
    eucreg1 = []
    eucreg2 = []
    jenreg0 = []
    jenreg1 = []
    jenreg2 = []
    for i in range (numexps):
        helreg0.append(results[4*i + 3][0])
        helreg1.append(results[4*i + 3][3])
        helreg2.append(results[4*i + 3][4])
        cosreg0.append(results[4*i + 0][0])
        cosreg1.append(results[4*i + 0][3])
        cosreg2.append(results[4*i + 0][4])
        eucreg0.append(results[4*i + 1][0])
        eucreg1.append(results[4*i + 1][3])
        eucreg2.append(results[4*i + 1][4])
        jenreg0.append(results[4*i + 2][0])
        jenreg1.append(results[4*i + 2][3])
        jenreg2.append(results[4*i + 2][4])
    plt.scatter(xarr,cosreg0,c=['red'], linewidths = 0.2)
    plt.plot(xarr,cosreg0,'r-', label='Взаимно ближайшие темы')
    plt.scatter(xarr,cosreg1,c=['blue'], linewidths = 0.2)
    plt.plot(xarr,cosreg1,'b--', label='Невосстановленные темы')
    plt.scatter(xarr,cosreg2,c=['green'], linewidths = 0.2)
    plt.plot(xarr,cosreg2,'g-.', label='Ложные темы')
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_4.eps', bbox_inches='tight', format='eps', transparent=False)
    plt.show()
    plt.scatter(xarr,eucreg0,c=['red'], linewidths = 0.2)
    plt.plot(xarr,eucreg0,'r-', label='Взаимно ближайшие темы')
    plt.scatter(xarr,eucreg1,c=['blue'], linewidths = 0.2)
    plt.plot(xarr,eucreg1,'b--', label='Невосстановленные темы')
    plt.scatter(xarr,eucreg2,c=['green'], linewidths = 0.2)
    plt.plot(xarr,eucreg2,'g-.', label='Ложные темы')
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_3.eps', bbox_inches='tight', format='eps', transparent=False)
    plt.show()
    plt.scatter(xarr,jenreg0,c=['red'], linewidths = 0.2)
    plt.plot(xarr,jenreg0,'r-', label='Взаимно ближайшие темы')
    plt.scatter(xarr,jenreg1,c=['blue'], linewidths = 0.2)
    plt.plot(xarr,jenreg1,'b--', label='Невосстановленные темы')
    plt.scatter(xarr,jenreg2,c=['green'], linewidths = 0.2)
    plt.plot(xarr,jenreg2,'g-.', label='Ложные темы')
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_2.eps', bbox_inches='tight', format='eps', transparent=False)
    plt.show()
    plt.scatter(xarr,helreg0,c=['red'], linewidths = 0.2)
    plt.plot(xarr,helreg0,'r-', label='Взаимно ближайшие темы')
    plt.scatter(xarr,helreg1,c=['blue'], linewidths = 0.2)
    plt.plot(xarr,helreg1,'b--', label='Невосстановленные темы')
    plt.scatter(xarr,helreg2,c=['green'], linewidths = 0.2)
    plt.plot(xarr,helreg2,'g-.', label='Ложные темы')
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.rcParams["figure.figsize"] = (6,5)
    plt.grid()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
    plt.savefig(path + '_1.eps', bbox_inches='tight', format='eps', transparent=False)
    plt.show()

