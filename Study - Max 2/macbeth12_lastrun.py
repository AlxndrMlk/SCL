#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on May 21, 2020, at 20:40
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'macbeth'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\aleksander.molak\\Documents\\Personal\\Psych\\SOCIAL_COGN_LAB\\SCL\\Study - Max 2\\macbeth12_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "manipulation"
manipulationClock = core.Clock()
manip_txt = ''
manipulation_text = visual.TextStim(win=win, name='manipulation_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
manipulation_key_resp = keyboard.Keyboard()

# Initialize components for Routine "fakeiq_scale_instr"
fakeiq_scale_instrClock = core.Clock()
instr_fakeiq = visual.TextStim(win=win, name='instr_fakeiq',
    text='W tej części badania poprosimy Pana/Panią o rozwiązanie kilku zadań mierzących zdolności poznawcze. \n\nAby kontynuować, prosimy nacisnąć spację.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_fakeiq_key_resp = keyboard.Keyboard()

# Initialize components for Routine "fakeiq_scale2"
fakeiq_scale2Clock = core.Clock()
space_instr_fake_iq = visual.TextStim(win=win, name='space_instr_fake_iq',
    text='Aby przejść do kolejnej części badania, naciśnij na klawiaturze odpowiednią literę widniejącą przy poprawnej odpowiedzi.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fakeiq2_key_resp = keyboard.Keyboard()
FAKE_iq_1 = visual.TextStim(win=win, name='FAKE_iq_1',
    text='Paczka gum do żucia i cukierek kosztują łącznie 1,10 zł. Paczka gum do żucia kosztuje o złotówkę więcej niż cukierek. \nIle groszy kosztuje cukierek?\n\n\na. 10\nb. 50\nc. 100\nd. 5\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fakeiq_scale3"
fakeiq_scale3Clock = core.Clock()
space_instr_fake_iq_2 = visual.TextStim(win=win, name='space_instr_fake_iq_2',
    text='Aby przejść do kolejnej części badania, naciśnij na klawiaturze odpowiednią literę widniejącą przy poprawnej odpowiedzi.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fakeiq2_key_resp_2 = keyboard.Keyboard()
FAKE_iq_2 = visual.TextStim(win=win, name='FAKE_iq_2',
    text='Jeśli 5 maszynom stworzenie 5 produktów zajmuje 5 minut, to ile minut zajęłoby stworzenie 100 produktów przez 100 maszyn?\n\n\n\na. 100\nb. 5\nc. 10\nd. 50\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "article_instr"
article_instrClock = core.Clock()
article_instr_text = visual.TextStim(win=win, name='article_instr_text',
    text='Na następnym ekranie zobaczą Państwo artykuł prasowy.\n\nProszę policzyć ile zdań w tym artykule ma liczbę słów, która jest liczbą pierwszą.\n\nLiczba pierwsza, to taka liczba, która dzieli się przez siebie samą i przez 1. \n\nW tym zadaniu ważny jest czas - proszę starać się wykonać je najszybciej jak Pan(i) potrafi.\n\nPo zakończeniu zadania proszę wcisnąć spację.\n\nJeśli jest Pan(i) gotowa, żeby rozpocząć zadanie, prosze nacisnąć spację.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "article"
articleClock = core.Clock()
screenshot_list = [
     'screenshots\\C1_C3_N2_C2_N3_N4.png',
     'screenshots\\C1_C3_N4_C4_N5_N3.png',
     'screenshots\\C1_N1_C5_C2_N4_N3.png',
     'screenshots\\C1_N1_C6_C5_N4_N3.png',
     'screenshots\\C1_N3_C3_N6_N5_C6.png',
     'screenshots\\C1_N4_N3_C5_C6_N6.png',
     'screenshots\\C1_N4_N6_C6_N5_C4.png',
     'screenshots\\C1_N5_N6_C3_N3_C5.png',
     'screenshots\\C2_C6_N2_N3_C4_N4.png',
     'screenshots\\C2_N1_C1_C4_N4_N2.png',
     'screenshots\\C2_N1_C6_C4_N3_N4.png',
     'screenshots\\C2_N2_N6_N5_C5_C4.png',
     'screenshots\\C2_N6_N2_N4_C3_C4.png',
     'screenshots\\C3_N3_C1_C6_N6_N4.png',
     'screenshots\\C3_N3_N6_C5_N2_C6.png',
     'screenshots\\C3_N6_C5_N4_C1_N3.png',
     'screenshots\\C4_C1_N4_N5_C3_N2.png',
     'screenshots\\C4_N4_N5_C6_C3_N1.png',
     'screenshots\\C6_C1_C5_N4_N3_N6.png',
     'screenshots\\C6_C1_N2_N3_N1_C4.png',
     'screenshots\\C6_C2_N3_N5_C3_N4.png',
     'screenshots\\C6_C2_N4_N3_C3_N1.png',
     'screenshots\\C6_C3_N3_C2_N1_N2.png',
     'screenshots\\C6_C3_N6_N3_C1_N5.png',
     'screenshots\\C6_C4_N2_N1_C1_N6.png',
     'screenshots\\C6_C5_N3_N6_N1_C1.png',
     'screenshots\\C6_N2_N3_N5_C5_C2.png',
     'screenshots\\C6_N3_C5_C1_N6_N2.png',
     'screenshots\\C6_N4_C5_N1_C4_N6.png',
     'screenshots\\C6_N6_C5_C1_N2_N1.png',
     'screenshots\\C6_N6_N1_N2_C2_C1.png',
     'screenshots\\N1_C2_N3_N4_C5_C3.png',
     'screenshots\\N1_C5_N5_C3_C2_N2.png',
     'screenshots\\N1_N5_C5_N6_C1_C2.png',
     'screenshots\\N1_N5_C6_C4_N6_C3.png',
     'screenshots\\N2_C3_C6_C2_N6_N5.png',
     'screenshots\\N2_C6_N3_C2_C5_N1.png',
     'screenshots\\N2_N1_C3_N3_C5_C4.png',
     'screenshots\\N3_C4_N2_N5_C5_C2.png',
     'screenshots\\N3_N2_C3_C4_N1_C1.png',
     'screenshots\\N4_C6_C5_N5_C3_N1.png',
     'screenshots\\N4_N5_C1_C6_C4_N6.png',
     'screenshots\\N5_N2_C4_C6_N6_C3.png',
     'screenshots\\N6_C4_C1_C3_N5_N1.png',
     'screenshots\\N6_C4_N2_C1_C5_N4.png',
     'screenshots\\N6_C5_N1_C2_C3_N2.png',
     'screenshots\\N6_C5_N1_C3_C2_N4.png',
     'screenshots\\N6_N1_C4_N2_C6_C1.png',
     'screenshots\\N6_N3_C3_N5_C5_C2.png',
     'screenshots\\N6_N5_C2_N1_C1_C4.png'
]

shuffle(screenshot_list)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "article_ans"
article_ansClock = core.Clock()
article_ans_resp = keyboard.Keyboard()
article_ans_2 = visual.TextStim(win=win, name='article_ans_2',
    text='Proszę wskazać ile zdań w artykule zawierało liczbę słów, która jest liczbą pierwszą, wciskając na klawiaturze literę, która widnieje przy prawidłowej odpowiedzi.\n\n\n\na. 12\nb. 3\nc. 7\nd. 15\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "DV_measurement_instr"
DV_measurement_instrClock = core.Clock()
DV_measurement_instr_text = visual.TextStim(win=win, name='DV_measurement_instr_text',
    text="Na kolejnych ekranach zostaną Państwo poproszeni o wskazanie, które reklamy widzieli Państwo w trakcie badania. \n\nJeśli uważają Państwo, że dana reklama pojawiła się na ekranie w trakcie badania, proszę wcisnąć 'T'. \n\nJeżeli uważają Państwo, że dana reklama nie pojawiła się na ekranie w trakcie badania, proszę wcisnąć 'N'. \n\nAby przejść do nastepnego ekranu, prosze wcisnąć spację.",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "DV_measurement"
DV_measurementClock = core.Clock()
ad_images = visual.ImageStim(
    win=win,
    name='ad_images', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
DV_measurement_key_resp = keyboard.Keyboard()

# Initialize components for Routine "debriefing"
debriefingClock = core.Clock()
debriefing_text = visual.TextStim(win=win, name='debriefing_text',
    text='Dziękujemy za udział w badaniu “Tales of moderate(d) impurity”. Przypominamy, że udział w badaniu był anonimowy, a wyniki będą opracowywane wyłącznie zbiorczo. Państwa odpowiedzi będą traktowane w sposób całkowicie poufny. \n\nW niniejszym badaniu chcieliśmy sprawdzić, dlaczego niektórzy ludzie postrzegają dane zachowanie jako moralne, podczas gdy inni uważają przeciwnie, oraz czy przekonania te mają związek z przypominaniem sobie różnych produktów. Spodziewamy się, że przypomnienie aktu uważanego przez osobę za niemoralny będzie prowadzić do częstszego przypominania sobie produktów czyszczących.  \n\nW badaniu zostali Państwo losowo przydzieleni do jednego z dwóch warunków eksperymentalnych. Część z Państwa została poproszona o przypomnienie sobie sytuacji zbliżenia seksualnego, podczas gdy część osób badanych nie otrzymała takiej prośby. Dla niektórych osób takie zadanie może być krępujące albo powodować nieprzyjemne bądź kłopotliwe uczucia i myśli. Takie uczucia i myśli mogą utrzymywać się przez jakiś czas po zakończeniu badania. Jest to zupełnie naturalne. \n\nCzęść badania, w której wzięli Państwo udział, dotyczyła przypomnienia sobie wyświetlanych podczas czytania artykułu reklam, które przedstawiały różnorodne produkty. Chcieliśmy sprawdzić, czy przypomnienie sobie intymnej sytuacji wiąże się z lepszym zapamiętywaniem określonych reklam.\n\nJeżeli mają Państwo jakiekolwiek pytania lub wątpliwości związane z badaniem, prosimy o kontakt pod adresem k.zochniak@student.uw.edu.pl.\n\nJesteśmy Państwu bardzo wdzięczni za udział w badaniu. Rozwój nauki możliwy jest dzięki osobom takim jak Państwo!\n',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
debriefing_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "manipulation"-------
continueRoutine = True
# update component parameters for each repeat
text = """0Teraz poprosimy Panią/Pana o przypomnienie sobie sytuacji, w której odbyła Pani/odbył Pan angażującą rozmowę ze swoją najbliższą osobą.

Proszę przypomnieć sobie jak czuła/czuł się Pani/Pan w tej sytuacji, jakie odczucia pojawiały się w Pani/Pana ciele. Może Pani/Pan napisać historię tego zdarzenia na kartce, aby łatwiej było się Pani/Panu skupić.

Nie będziemy zadawać pytań na temat szczegółów historii oraz jej merytoryki. Jest ona wyłącznie Pani/Pana własnością. 






Jeżeli doświadczyła/doświadczył Pani/Pan wyżej opisanej sytuacji, prosimy wcisnąć klawisz 'T'.
W przeciwnym razie prosimy wcisnąć klawisz 'N'.**1Teraz poprosimy Panią/Pana o przypomnienie sobie sytuacji, w której odbyła Pani/odbył Pan stosunek seksualny, nie będąc wówczas z związku.

Proszę przypomnieć sobie jak czuła/czuł się Pani/Pan w tej sytuacji, jakie odczucia pojawiały się w Pani/Pana ciele. Może Pani/Pan napisać historię tego zdarzenia na kartce, aby łatwiej było się Pani/Panu skupić.

Nie będziemy zadawać pytań na temat szczegółów historii oraz jej merytoryki. Jest ona wyłącznie Pani/Pana własnością. 






Jeżeli doświadczyła/doświadczył Pani/Pan wyżej opisanej sytuacji, prosimy wcisnąć klawisz 'T'.
W przeciwnym razie prosimy wcisnąć klawisz 'N'."""

texts = text.split('**')

shuffle(texts)

manip_txt = texts[0][1:]

condition = texts[0][0]

#with open(r'.\instructions\instr_cntrl.txt', 'r', encoding = 'utf-8') as f:
#    instr_cntrl = f.read()
#    
#with open(r'.\instructions\instr_exprmntl.txt', 'r', encoding = 'utf-8') as f:
#    instr_exprmntl = f.read()
#
#condition = np.random.choice(['cntrl', 'exprmntl'])
#
#if condition == 'cntrl':
#    manip_txt = instr_cntrl
#else:
#    manip_txt = instr_exprmntl
manipulation_text.setText(manip_txt)
manipulation_key_resp.keys = []
manipulation_key_resp.rt = []
_manipulation_key_resp_allKeys = []
# keep track of which components have finished
manipulationComponents = [manipulation_text, manipulation_key_resp]
for thisComponent in manipulationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
manipulationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "manipulation"-------
while continueRoutine:
    # get current time
    t = manipulationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=manipulationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *manipulation_text* updates
    if manipulation_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        manipulation_text.frameNStart = frameN  # exact frame index
        manipulation_text.tStart = t  # local t and not account for scr refresh
        manipulation_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(manipulation_text, 'tStartRefresh')  # time at next scr refresh
        manipulation_text.setAutoDraw(True)
    
    # *manipulation_key_resp* updates
    waitOnFlip = False
    if manipulation_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        manipulation_key_resp.frameNStart = frameN  # exact frame index
        manipulation_key_resp.tStart = t  # local t and not account for scr refresh
        manipulation_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(manipulation_key_resp, 'tStartRefresh')  # time at next scr refresh
        manipulation_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(manipulation_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(manipulation_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if manipulation_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = manipulation_key_resp.getKeys(keyList=['t', 'n'], waitRelease=False)
        _manipulation_key_resp_allKeys.extend(theseKeys)
        if len(_manipulation_key_resp_allKeys):
            manipulation_key_resp.keys = _manipulation_key_resp_allKeys[-1].name  # just the last key pressed
            manipulation_key_resp.rt = _manipulation_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in manipulationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "manipulation"-------
for thisComponent in manipulationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('condition', condition)
thisExp.addData('manipulation_text.started', manipulation_text.tStartRefresh)
thisExp.addData('manipulation_text.stopped', manipulation_text.tStopRefresh)
# check responses
if manipulation_key_resp.keys in ['', [], None]:  # No response was made
    manipulation_key_resp.keys = None
thisExp.addData('manipulation_key_resp.keys',manipulation_key_resp.keys)
if manipulation_key_resp.keys != None:  # we had a response
    thisExp.addData('manipulation_key_resp.rt', manipulation_key_resp.rt)
thisExp.addData('manipulation_key_resp.started', manipulation_key_resp.tStartRefresh)
thisExp.addData('manipulation_key_resp.stopped', manipulation_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "manipulation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fakeiq_scale_instr"-------
continueRoutine = True
# update component parameters for each repeat
instr_fakeiq_key_resp.keys = []
instr_fakeiq_key_resp.rt = []
_instr_fakeiq_key_resp_allKeys = []
# keep track of which components have finished
fakeiq_scale_instrComponents = [instr_fakeiq, instr_fakeiq_key_resp]
for thisComponent in fakeiq_scale_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fakeiq_scale_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fakeiq_scale_instr"-------
while continueRoutine:
    # get current time
    t = fakeiq_scale_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fakeiq_scale_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_fakeiq* updates
    if instr_fakeiq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_fakeiq.frameNStart = frameN  # exact frame index
        instr_fakeiq.tStart = t  # local t and not account for scr refresh
        instr_fakeiq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_fakeiq, 'tStartRefresh')  # time at next scr refresh
        instr_fakeiq.setAutoDraw(True)
    
    # *instr_fakeiq_key_resp* updates
    waitOnFlip = False
    if instr_fakeiq_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_fakeiq_key_resp.frameNStart = frameN  # exact frame index
        instr_fakeiq_key_resp.tStart = t  # local t and not account for scr refresh
        instr_fakeiq_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_fakeiq_key_resp, 'tStartRefresh')  # time at next scr refresh
        instr_fakeiq_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_fakeiq_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_fakeiq_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_fakeiq_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_fakeiq_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _instr_fakeiq_key_resp_allKeys.extend(theseKeys)
        if len(_instr_fakeiq_key_resp_allKeys):
            instr_fakeiq_key_resp.keys = _instr_fakeiq_key_resp_allKeys[-1].name  # just the last key pressed
            instr_fakeiq_key_resp.rt = _instr_fakeiq_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fakeiq_scale_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fakeiq_scale_instr"-------
for thisComponent in fakeiq_scale_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_fakeiq.started', instr_fakeiq.tStartRefresh)
thisExp.addData('instr_fakeiq.stopped', instr_fakeiq.tStopRefresh)
# check responses
if instr_fakeiq_key_resp.keys in ['', [], None]:  # No response was made
    instr_fakeiq_key_resp.keys = None
thisExp.addData('instr_fakeiq_key_resp.keys',instr_fakeiq_key_resp.keys)
if instr_fakeiq_key_resp.keys != None:  # we had a response
    thisExp.addData('instr_fakeiq_key_resp.rt', instr_fakeiq_key_resp.rt)
thisExp.addData('instr_fakeiq_key_resp.started', instr_fakeiq_key_resp.tStartRefresh)
thisExp.addData('instr_fakeiq_key_resp.stopped', instr_fakeiq_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "fakeiq_scale_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fakeiq_scale2"-------
continueRoutine = True
# update component parameters for each repeat
fakeiq2_key_resp.keys = []
fakeiq2_key_resp.rt = []
_fakeiq2_key_resp_allKeys = []
# keep track of which components have finished
fakeiq_scale2Components = [space_instr_fake_iq, fakeiq2_key_resp, FAKE_iq_1]
for thisComponent in fakeiq_scale2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fakeiq_scale2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fakeiq_scale2"-------
while continueRoutine:
    # get current time
    t = fakeiq_scale2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fakeiq_scale2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_instr_fake_iq* updates
    if space_instr_fake_iq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_instr_fake_iq.frameNStart = frameN  # exact frame index
        space_instr_fake_iq.tStart = t  # local t and not account for scr refresh
        space_instr_fake_iq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_instr_fake_iq, 'tStartRefresh')  # time at next scr refresh
        space_instr_fake_iq.setAutoDraw(True)
    
    # *fakeiq2_key_resp* updates
    waitOnFlip = False
    if fakeiq2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fakeiq2_key_resp.frameNStart = frameN  # exact frame index
        fakeiq2_key_resp.tStart = t  # local t and not account for scr refresh
        fakeiq2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fakeiq2_key_resp, 'tStartRefresh')  # time at next scr refresh
        fakeiq2_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fakeiq2_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fakeiq2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fakeiq2_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = fakeiq2_key_resp.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
        _fakeiq2_key_resp_allKeys.extend(theseKeys)
        if len(_fakeiq2_key_resp_allKeys):
            fakeiq2_key_resp.keys = _fakeiq2_key_resp_allKeys[-1].name  # just the last key pressed
            fakeiq2_key_resp.rt = _fakeiq2_key_resp_allKeys[-1].rt
            # was this correct?
            if (fakeiq2_key_resp.keys == str('')) or (fakeiq2_key_resp.keys == ''):
                fakeiq2_key_resp.corr = 1
            else:
                fakeiq2_key_resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # *FAKE_iq_1* updates
    if FAKE_iq_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FAKE_iq_1.frameNStart = frameN  # exact frame index
        FAKE_iq_1.tStart = t  # local t and not account for scr refresh
        FAKE_iq_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FAKE_iq_1, 'tStartRefresh')  # time at next scr refresh
        FAKE_iq_1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fakeiq_scale2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fakeiq_scale2"-------
for thisComponent in fakeiq_scale2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('space_instr_fake_iq.started', space_instr_fake_iq.tStartRefresh)
thisExp.addData('space_instr_fake_iq.stopped', space_instr_fake_iq.tStopRefresh)
# check responses
if fakeiq2_key_resp.keys in ['', [], None]:  # No response was made
    fakeiq2_key_resp.keys = None
    # was no response the correct answer?!
    if str('').lower() == 'none':
       fakeiq2_key_resp.corr = 1;  # correct non-response
    else:
       fakeiq2_key_resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('fakeiq2_key_resp.keys',fakeiq2_key_resp.keys)
thisExp.addData('fakeiq2_key_resp.corr', fakeiq2_key_resp.corr)
if fakeiq2_key_resp.keys != None:  # we had a response
    thisExp.addData('fakeiq2_key_resp.rt', fakeiq2_key_resp.rt)
thisExp.addData('fakeiq2_key_resp.started', fakeiq2_key_resp.tStartRefresh)
thisExp.addData('fakeiq2_key_resp.stopped', fakeiq2_key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('FAKE_iq_1.started', FAKE_iq_1.tStartRefresh)
thisExp.addData('FAKE_iq_1.stopped', FAKE_iq_1.tStopRefresh)
# the Routine "fakeiq_scale2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fakeiq_scale3"-------
continueRoutine = True
# update component parameters for each repeat
fakeiq2_key_resp_2.keys = []
fakeiq2_key_resp_2.rt = []
_fakeiq2_key_resp_2_allKeys = []
# keep track of which components have finished
fakeiq_scale3Components = [space_instr_fake_iq_2, fakeiq2_key_resp_2, FAKE_iq_2]
for thisComponent in fakeiq_scale3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fakeiq_scale3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fakeiq_scale3"-------
while continueRoutine:
    # get current time
    t = fakeiq_scale3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fakeiq_scale3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_instr_fake_iq_2* updates
    if space_instr_fake_iq_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_instr_fake_iq_2.frameNStart = frameN  # exact frame index
        space_instr_fake_iq_2.tStart = t  # local t and not account for scr refresh
        space_instr_fake_iq_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_instr_fake_iq_2, 'tStartRefresh')  # time at next scr refresh
        space_instr_fake_iq_2.setAutoDraw(True)
    
    # *fakeiq2_key_resp_2* updates
    waitOnFlip = False
    if fakeiq2_key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fakeiq2_key_resp_2.frameNStart = frameN  # exact frame index
        fakeiq2_key_resp_2.tStart = t  # local t and not account for scr refresh
        fakeiq2_key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fakeiq2_key_resp_2, 'tStartRefresh')  # time at next scr refresh
        fakeiq2_key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fakeiq2_key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fakeiq2_key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fakeiq2_key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = fakeiq2_key_resp_2.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
        _fakeiq2_key_resp_2_allKeys.extend(theseKeys)
        if len(_fakeiq2_key_resp_2_allKeys):
            fakeiq2_key_resp_2.keys = _fakeiq2_key_resp_2_allKeys[-1].name  # just the last key pressed
            fakeiq2_key_resp_2.rt = _fakeiq2_key_resp_2_allKeys[-1].rt
            # was this correct?
            if (fakeiq2_key_resp_2.keys == str('')) or (fakeiq2_key_resp_2.keys == ''):
                fakeiq2_key_resp_2.corr = 1
            else:
                fakeiq2_key_resp_2.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # *FAKE_iq_2* updates
    if FAKE_iq_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FAKE_iq_2.frameNStart = frameN  # exact frame index
        FAKE_iq_2.tStart = t  # local t and not account for scr refresh
        FAKE_iq_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FAKE_iq_2, 'tStartRefresh')  # time at next scr refresh
        FAKE_iq_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fakeiq_scale3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fakeiq_scale3"-------
for thisComponent in fakeiq_scale3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('space_instr_fake_iq_2.started', space_instr_fake_iq_2.tStartRefresh)
thisExp.addData('space_instr_fake_iq_2.stopped', space_instr_fake_iq_2.tStopRefresh)
# check responses
if fakeiq2_key_resp_2.keys in ['', [], None]:  # No response was made
    fakeiq2_key_resp_2.keys = None
    # was no response the correct answer?!
    if str('').lower() == 'none':
       fakeiq2_key_resp_2.corr = 1;  # correct non-response
    else:
       fakeiq2_key_resp_2.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('fakeiq2_key_resp_2.keys',fakeiq2_key_resp_2.keys)
thisExp.addData('fakeiq2_key_resp_2.corr', fakeiq2_key_resp_2.corr)
if fakeiq2_key_resp_2.keys != None:  # we had a response
    thisExp.addData('fakeiq2_key_resp_2.rt', fakeiq2_key_resp_2.rt)
thisExp.addData('fakeiq2_key_resp_2.started', fakeiq2_key_resp_2.tStartRefresh)
thisExp.addData('fakeiq2_key_resp_2.stopped', fakeiq2_key_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('FAKE_iq_2.started', FAKE_iq_2.tStartRefresh)
thisExp.addData('FAKE_iq_2.stopped', FAKE_iq_2.tStopRefresh)
# the Routine "fakeiq_scale3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "article_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
article_instrComponents = [article_instr_text, key_resp_4]
for thisComponent in article_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
article_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "article_instr"-------
while continueRoutine:
    # get current time
    t = article_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=article_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *article_instr_text* updates
    if article_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        article_instr_text.frameNStart = frameN  # exact frame index
        article_instr_text.tStart = t  # local t and not account for scr refresh
        article_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(article_instr_text, 'tStartRefresh')  # time at next scr refresh
        article_instr_text.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in article_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "article_instr"-------
for thisComponent in article_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('article_instr_text.started', article_instr_text.tStartRefresh)
thisExp.addData('article_instr_text.stopped', article_instr_text.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "article_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "article"-------
continueRoutine = True
# update component parameters for each repeat
image.setImage(screenshot_list[0])
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
articleComponents = [image, key_resp_2]
for thisComponent in articleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
articleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "article"-------
while continueRoutine:
    # get current time
    t = articleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=articleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in articleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "article"-------
for thisComponent in articleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('screenshot', screenshot_list[0])
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "article" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "article_ans"-------
continueRoutine = True
# update component parameters for each repeat
article_ans_resp.keys = []
article_ans_resp.rt = []
_article_ans_resp_allKeys = []
# keep track of which components have finished
article_ansComponents = [article_ans_resp, article_ans_2]
for thisComponent in article_ansComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
article_ansClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "article_ans"-------
while continueRoutine:
    # get current time
    t = article_ansClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=article_ansClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *article_ans_resp* updates
    waitOnFlip = False
    if article_ans_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        article_ans_resp.frameNStart = frameN  # exact frame index
        article_ans_resp.tStart = t  # local t and not account for scr refresh
        article_ans_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(article_ans_resp, 'tStartRefresh')  # time at next scr refresh
        article_ans_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(article_ans_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(article_ans_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if article_ans_resp.status == STARTED and not waitOnFlip:
        theseKeys = article_ans_resp.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
        _article_ans_resp_allKeys.extend(theseKeys)
        if len(_article_ans_resp_allKeys):
            article_ans_resp.keys = _article_ans_resp_allKeys[-1].name  # just the last key pressed
            article_ans_resp.rt = _article_ans_resp_allKeys[-1].rt
            # was this correct?
            if (article_ans_resp.keys == str('')) or (article_ans_resp.keys == ''):
                article_ans_resp.corr = 1
            else:
                article_ans_resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # *article_ans_2* updates
    if article_ans_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        article_ans_2.frameNStart = frameN  # exact frame index
        article_ans_2.tStart = t  # local t and not account for scr refresh
        article_ans_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(article_ans_2, 'tStartRefresh')  # time at next scr refresh
        article_ans_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in article_ansComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "article_ans"-------
for thisComponent in article_ansComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if article_ans_resp.keys in ['', [], None]:  # No response was made
    article_ans_resp.keys = None
    # was no response the correct answer?!
    if str('').lower() == 'none':
       article_ans_resp.corr = 1;  # correct non-response
    else:
       article_ans_resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('article_ans_resp.keys',article_ans_resp.keys)
thisExp.addData('article_ans_resp.corr', article_ans_resp.corr)
if article_ans_resp.keys != None:  # we had a response
    thisExp.addData('article_ans_resp.rt', article_ans_resp.rt)
thisExp.addData('article_ans_resp.started', article_ans_resp.tStartRefresh)
thisExp.addData('article_ans_resp.stopped', article_ans_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('article_ans_2.started', article_ans_2.tStartRefresh)
thisExp.addData('article_ans_2.stopped', article_ans_2.tStopRefresh)
# the Routine "article_ans" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "DV_measurement_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
DV_measurement_instrComponents = [DV_measurement_instr_text, key_resp_3]
for thisComponent in DV_measurement_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DV_measurement_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "DV_measurement_instr"-------
while continueRoutine:
    # get current time
    t = DV_measurement_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DV_measurement_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *DV_measurement_instr_text* updates
    if DV_measurement_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DV_measurement_instr_text.frameNStart = frameN  # exact frame index
        DV_measurement_instr_text.tStart = t  # local t and not account for scr refresh
        DV_measurement_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DV_measurement_instr_text, 'tStartRefresh')  # time at next scr refresh
        DV_measurement_instr_text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DV_measurement_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "DV_measurement_instr"-------
for thisComponent in DV_measurement_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('DV_measurement_instr_text.started', DV_measurement_instr_text.tStartRefresh)
thisExp.addData('DV_measurement_instr_text.stopped', DV_measurement_instr_text.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "DV_measurement_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ads_paths.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "DV_measurement"-------
    continueRoutine = True
    # update component parameters for each repeat
    ad_images.setImage(ImageFile)
    DV_measurement_key_resp.keys = []
    DV_measurement_key_resp.rt = []
    _DV_measurement_key_resp_allKeys = []
    # keep track of which components have finished
    DV_measurementComponents = [ad_images, DV_measurement_key_resp]
    for thisComponent in DV_measurementComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DV_measurementClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "DV_measurement"-------
    while continueRoutine:
        # get current time
        t = DV_measurementClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DV_measurementClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ad_images* updates
        if ad_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ad_images.frameNStart = frameN  # exact frame index
            ad_images.tStart = t  # local t and not account for scr refresh
            ad_images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ad_images, 'tStartRefresh')  # time at next scr refresh
            ad_images.setAutoDraw(True)
        
        # *DV_measurement_key_resp* updates
        waitOnFlip = False
        if DV_measurement_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DV_measurement_key_resp.frameNStart = frameN  # exact frame index
            DV_measurement_key_resp.tStart = t  # local t and not account for scr refresh
            DV_measurement_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DV_measurement_key_resp, 'tStartRefresh')  # time at next scr refresh
            DV_measurement_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(DV_measurement_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(DV_measurement_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if DV_measurement_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = DV_measurement_key_resp.getKeys(keyList=['t', 'n'], waitRelease=False)
            _DV_measurement_key_resp_allKeys.extend(theseKeys)
            if len(_DV_measurement_key_resp_allKeys):
                DV_measurement_key_resp.keys = _DV_measurement_key_resp_allKeys[-1].name  # just the last key pressed
                DV_measurement_key_resp.rt = _DV_measurement_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DV_measurementComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DV_measurement"-------
    for thisComponent in DV_measurementComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ad_images.started', ad_images.tStartRefresh)
    trials.addData('ad_images.stopped', ad_images.tStopRefresh)
    # check responses
    if DV_measurement_key_resp.keys in ['', [], None]:  # No response was made
        DV_measurement_key_resp.keys = None
    trials.addData('DV_measurement_key_resp.keys',DV_measurement_key_resp.keys)
    if DV_measurement_key_resp.keys != None:  # we had a response
        trials.addData('DV_measurement_key_resp.rt', DV_measurement_key_resp.rt)
    trials.addData('DV_measurement_key_resp.started', DV_measurement_key_resp.tStartRefresh)
    trials.addData('DV_measurement_key_resp.stopped', DV_measurement_key_resp.tStopRefresh)
    # the Routine "DV_measurement" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "debriefing"-------
continueRoutine = True
# update component parameters for each repeat
debriefing_key_resp.keys = []
debriefing_key_resp.rt = []
_debriefing_key_resp_allKeys = []
# keep track of which components have finished
debriefingComponents = [debriefing_text, debriefing_key_resp]
for thisComponent in debriefingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debriefingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debriefing"-------
while continueRoutine:
    # get current time
    t = debriefingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debriefingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debriefing_text* updates
    if debriefing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefing_text.frameNStart = frameN  # exact frame index
        debriefing_text.tStart = t  # local t and not account for scr refresh
        debriefing_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefing_text, 'tStartRefresh')  # time at next scr refresh
        debriefing_text.setAutoDraw(True)
    
    # *debriefing_key_resp* updates
    waitOnFlip = False
    if debriefing_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefing_key_resp.frameNStart = frameN  # exact frame index
        debriefing_key_resp.tStart = t  # local t and not account for scr refresh
        debriefing_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefing_key_resp, 'tStartRefresh')  # time at next scr refresh
        debriefing_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(debriefing_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(debriefing_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if debriefing_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = debriefing_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _debriefing_key_resp_allKeys.extend(theseKeys)
        if len(_debriefing_key_resp_allKeys):
            debriefing_key_resp.keys = _debriefing_key_resp_allKeys[-1].name  # just the last key pressed
            debriefing_key_resp.rt = _debriefing_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debriefingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debriefing"-------
for thisComponent in debriefingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debriefing_text.started', debriefing_text.tStartRefresh)
thisExp.addData('debriefing_text.stopped', debriefing_text.tStopRefresh)
# check responses
if debriefing_key_resp.keys in ['', [], None]:  # No response was made
    debriefing_key_resp.keys = None
thisExp.addData('debriefing_key_resp.keys',debriefing_key_resp.keys)
if debriefing_key_resp.keys != None:  # we had a response
    thisExp.addData('debriefing_key_resp.rt', debriefing_key_resp.rt)
thisExp.addData('debriefing_key_resp.started', debriefing_key_resp.tStartRefresh)
thisExp.addData('debriefing_key_resp.stopped', debriefing_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "debriefing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
