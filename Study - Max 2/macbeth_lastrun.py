#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on May 03, 2020, at 18:56
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
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\aleksander.molak\\Documents\\Personal\\Psych\\SOCIAL_COGN_LAB\\SCL\\Study - Max\\macbeth_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_text = visual.TextStim(win=win, name='intro_text',
    text='Dzień dobry,\n\nJesteśmy studentami Wydziału Psychologii Uniwersytetu Warszawskiego i przeprowadzamy badanie na temat wpływu jakości relacji z drugą osobą na funkcjonowanie poznawcze. Badanie będzie składać się z dwóch głównych części. W pierwszej części badania będziemy chcieli dowiedzieć się jak najwięcej na temat Pani/Pana bliskiej relacji z drugą osobą. W tym celu poprosimy o udzielenie odpowiedzi na zadane pytania oraz przypomnienie sobie pewnych wydarzeń z Pani/Pana życia. Druga część badania dotyczyć będzie funkcjonowania poznawczego. Poprosimy Panią/Pana o wykonanie kilku zadań, które będą sprawdzały Pani/Pana umiejętności w różnych obszarach poznawczych. \n\nW badaniu mogą wziąć udział wyłącznie osoby pełnoletnie. \n\nProsimy pamiętać, że badanie jest całkowicie anonimowe, a wyniki będą analizowane wyłącznie zbiorczo. Państwa odpowiedzi będą traktowane w sposób zupełnie poufny. Mogą Państwo zrezygnować z uczestnictwa w badaniu w dowolnym momencie. W razie wszelkich pytań zapraszamy do kontaktu pod adresem mailowym: k.zochniak@student.uw.edu.pl\n\nMaksymilian Koc, Aleksander Molak, Kamila Zochniak\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_instr_intro = visual.TextStim(win=win, name='space_instr_intro',
    text='Aby wziąć udział w badaniu, naciśnij spację.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
intro_key_resp = keyboard.Keyboard()

# Initialize components for Routine "relationship_scale"
relationship_scaleClock = core.Clock()
win.allowStencil = True
relationship_form = visual.Form(win=win, name='relationship_form',
    items='relationship_quest.xlsx',
    textHeight=0.02,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05)
space_instr_4 = visual.TextStim(win=win, name='space_instr_4',
    text='Aby przejść do kolejnej części badania, naciśnij spację.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
relationship_key_resp = keyboard.Keyboard()
relationship_instr = visual.TextStim(win=win, name='relationship_instr',
    text='Prosimy o udzielenie odpowiedzi na poniższe pytania:',
    font='Arial',
    pos=(0, 0.43), height=0.026, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "fakeiq_scale_instr"
fakeiq_scale_instrClock = core.Clock()
instr_fakeiq = visual.TextStim(win=win, name='instr_fakeiq',
    text='W tej części badania poprosimy Pana/Panią o rozwiązanie kilku zadań mierzących zdolności poznawcze. Po zdecydowaniu\nsię na którąś z odpowiedzi, prosimy nacisnąć odpowiedni numer na klawiaturze.\n\nAby kontynuować, prosimy nacisnąć spację.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_fakeiq_key_resp = keyboard.Keyboard()

# Initialize components for Routine "fakeiq_scale"
fakeiq_scaleClock = core.Clock()
image_raven = visual.ImageStim(
    win=win,
    name='image_raven', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "preMFQ_instr"
preMFQ_instrClock = core.Clock()
instr_premfq = visual.TextStim(win=win, name='instr_premfq',
    text='W tej części badania poprosimy Pana/Panią o odpowiedź na pytania dotyczące tego, co uważa Pan/Pani za dobre lub złe.\n\nAby kontynuować, prosimy nacisnąć spację.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_premfq_key_resp = keyboard.Keyboard()

# Initialize components for Routine "MFQ1"
MFQ1Clock = core.Clock()
win.allowStencil = True
MFQ_part1 = visual.Form(win=win, name='MFQ_part1',
    items='mfq1.xlsx',
    textHeight=0.02,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05)
mfq1_key_resp = keyboard.Keyboard()
space_instr = visual.TextStim(win=win, name='space_instr',
    text='Aby przejść do kolejnej części badania, naciśnij spację.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
mfq1_instr = visual.TextStim(win=win, name='mfq1_instr',
    text='Ludzie, oceniając w życiu codziennym, czy dane zachowanie jest dobre,\nczy złe, biorą pod uwagę różne kryteria. W jakim stopniu poniższe kryteria\nsą ważne dla Pani/Pana przy ocenie danego zachowania jako dobre lub złe? \nProsimy odpowiedzieć zgodnie z poniższą skalą, zaznaczając przy odpowiedniej liczbie:',
    font='Arial',
    pos=(0, 0.43), height=0.023, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
scale_instr_mfq1 = visual.TextStim(win=win, name='scale_instr_mfq1',
    text='1 Zdecydowanie nieważne\n2 Nieważne\n3 Raczej nieważne\n4 Raczej ważne\n5 Ważne\n6 Zdecydowanie ważne',
    font='Arial',
    pos=(-0.7, 0.26), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "MFQ2"
MFQ2Clock = core.Clock()
win.allowStencil = True
MFQ_part2 = visual.Form(win=win, name='MFQ_part2',
    items='mfq2.xlsx',
    textHeight=0.02,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05)
mfq2_key_resp = keyboard.Keyboard()
space_instr_2 = visual.TextStim(win=win, name='space_instr_2',
    text='Aby przejść do kolejnej części badania, naciśnij spację.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
scale_instr_mfq1_2 = visual.TextStim(win=win, name='scale_instr_mfq1_2',
    text='1 Zdecydowanie się nie zgadzam\n2 Nie zgadzam się\n3 Raczej się nie zgadzam\n4 Raczej się zgadzam\n5 Zgadzam się\n6 Zdecydowanie się zgadzam',
    font='Arial',
    pos=(-0.7, 0.26), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mfq1_instr_2 = visual.TextStim(win=win, name='mfq1_instr_2',
    text='Prosimy o przeczytanie poniższych stwierdzeń i ustosunkowanie się\ndo nich zgodnie z poniższą skalą, zaznaczając przy odpowiedniej liczbie:',
    font='Arial',
    pos=(0, 0.43), height=0.023, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

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
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "demography"
demographyClock = core.Clock()
win.allowStencil = True
demography_form = visual.Form(win=win, name='demography_form',
    items='demography.xlsx',
    textHeight=0.02,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05)
demo_key_resp = keyboard.Keyboard()
space_instr_3 = visual.TextStim(win=win, name='space_instr_3',
    text='Aby przejść do kolejnej części badania, naciśnij spację.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "debriefing"
debriefingClock = core.Clock()
debriefing_text = visual.TextStim(win=win, name='debriefing_text',
    text='Dziękujemy za udział w badaniu “Tales of moderate(d) impurity”. Przypominamy, że udział w badaniu był anonimowy, a wyniki będą opracowywane wyłącznie zbiorczo. \n\nW niniejszym badaniu chcieliśmy sprawdzić, dlaczego niektórzy ludzie postrzegają dane zachowanie jako moralne, podczas gdy inni uważają przeciwnie, oraz czy przekonania te mają związek z wyborem różnych produktów. Spodziewamy się, że przypomnienie aktu uważanego przez osobę za niemoralny będzie prowadzić do częstszego wyboru produktów czyszczących.  \n\nW badaniu zostali Państwo losowo przydzieleni do jednego z dwóch warunków eksperymentalnych. Część z Państwa została poproszona o przypomnienie sobie intymnej sytuacji, podczas gdy część z osób badanych nie otrzymała takiej prośby. Dla niektórych osób taka prośba może być krępująca albo powodować nieprzyjemne bądź kłopotliwe uczucia lub myśli. Takie uczucia lub myśli mogą utrzymywać się przez jakiś czas po zakończeniu badania. Jest to zupełnie naturalne. \n\nDruga część badania, w której wzięli Państwo udział, dotyczyła wyboru produktów. Chcielibyśmy podkreślić, że nie było wśród nich wyborów poprawnych lub niepoprawnych. Zadanie służyło wyłącznie poznaniu preferencji uczestników badania dotyczących danych produktów. \n\nW dalszym ciągu mogą Państwo zrezygnować z udziału w badaniu. Aby to zrobić, należy zamknąć kartę przeglądarki, nie przechodząc na kolejny ekran. Jeżeli mają Państwo jakiekolwiek pytania lub wątpliwości związane z badaniem, prosimy o kontakt pod adresem ……………….\n\nJesteśmy Państwu bardzo wdzięczni za udział w badaniu. Rozwój nauki możliwy jest dzięki osobom takim jak Państwo!\n\nAby zakończyć badanie, prosimy nacisnąć spację.\n',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
debriefing_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
intro_key_resp.keys = []
intro_key_resp.rt = []
_intro_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [intro_text, space_instr_intro, intro_key_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        intro_text.setAutoDraw(True)
    
    # *space_instr_intro* updates
    if space_instr_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_instr_intro.frameNStart = frameN  # exact frame index
        space_instr_intro.tStart = t  # local t and not account for scr refresh
        space_instr_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_instr_intro, 'tStartRefresh')  # time at next scr refresh
        space_instr_intro.setAutoDraw(True)
    
    # *intro_key_resp* updates
    waitOnFlip = False
    if intro_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp.frameNStart = frameN  # exact frame index
        intro_key_resp.tStart = t  # local t and not account for scr refresh
        intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp, 'tStartRefresh')  # time at next scr refresh
        intro_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_resp_allKeys.extend(theseKeys)
        if len(_intro_key_resp_allKeys):
            intro_key_resp.keys = _intro_key_resp_allKeys[-1].name  # just the last key pressed
            intro_key_resp.rt = _intro_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro_text.started', intro_text.tStartRefresh)
thisExp.addData('intro_text.stopped', intro_text.tStopRefresh)
thisExp.addData('space_instr_intro.started', space_instr_intro.tStartRefresh)
thisExp.addData('space_instr_intro.stopped', space_instr_intro.tStopRefresh)
# check responses
if intro_key_resp.keys in ['', [], None]:  # No response was made
    intro_key_resp.keys = None
thisExp.addData('intro_key_resp.keys',intro_key_resp.keys)
if intro_key_resp.keys != None:  # we had a response
    thisExp.addData('intro_key_resp.rt', intro_key_resp.rt)
thisExp.addData('intro_key_resp.started', intro_key_resp.tStartRefresh)
thisExp.addData('intro_key_resp.stopped', intro_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "relationship_scale"-------
continueRoutine = True
# update component parameters for each repeat
relationship_key_resp.keys = []
relationship_key_resp.rt = []
_relationship_key_resp_allKeys = []
# keep track of which components have finished
relationship_scaleComponents = [relationship_form, space_instr_4, relationship_key_resp, relationship_instr]
for thisComponent in relationship_scaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
relationship_scaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "relationship_scale"-------
while continueRoutine:
    # get current time
    t = relationship_scaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=relationship_scaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    relationship_form.draw()
    
    # *space_instr_4* updates
    if space_instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_instr_4.frameNStart = frameN  # exact frame index
        space_instr_4.tStart = t  # local t and not account for scr refresh
        space_instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_instr_4, 'tStartRefresh')  # time at next scr refresh
        space_instr_4.setAutoDraw(True)
    
    # *relationship_key_resp* updates
    waitOnFlip = False
    if relationship_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        relationship_key_resp.frameNStart = frameN  # exact frame index
        relationship_key_resp.tStart = t  # local t and not account for scr refresh
        relationship_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(relationship_key_resp, 'tStartRefresh')  # time at next scr refresh
        relationship_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(relationship_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(relationship_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if relationship_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = relationship_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _relationship_key_resp_allKeys.extend(theseKeys)
        if len(_relationship_key_resp_allKeys):
            relationship_key_resp.keys = _relationship_key_resp_allKeys[-1].name  # just the last key pressed
            relationship_key_resp.rt = _relationship_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *relationship_instr* updates
    if relationship_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        relationship_instr.frameNStart = frameN  # exact frame index
        relationship_instr.tStart = t  # local t and not account for scr refresh
        relationship_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(relationship_instr, 'tStartRefresh')  # time at next scr refresh
        relationship_instr.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in relationship_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "relationship_scale"-------
for thisComponent in relationship_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
relationship_formData = relationship_form.getData()
while relationship_formData['questions']:
    for dataTypes in relationship_formData.keys():
        thisExp.addData(dataTypes, relationship_formData[dataTypes].popleft())
    thisExp.nextEntry()
thisExp.addData('space_instr_4.started', space_instr_4.tStartRefresh)
thisExp.addData('space_instr_4.stopped', space_instr_4.tStopRefresh)
# check responses
if relationship_key_resp.keys in ['', [], None]:  # No response was made
    relationship_key_resp.keys = None
thisExp.addData('relationship_key_resp.keys',relationship_key_resp.keys)
if relationship_key_resp.keys != None:  # we had a response
    thisExp.addData('relationship_key_resp.rt', relationship_key_resp.rt)
thisExp.addData('relationship_key_resp.started', relationship_key_resp.tStartRefresh)
thisExp.addData('relationship_key_resp.stopped', relationship_key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('relationship_instr.started', relationship_instr.tStartRefresh)
thisExp.addData('relationship_instr.stopped', relationship_instr.tStopRefresh)
# the Routine "relationship_scale" was not non-slip safe, so reset the non-slip timer
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

# set up handler to look after randomisation of conditions etc
fakeiq_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fakeiq_images.xlsx'),
    seed=None, name='fakeiq_trials')
thisExp.addLoop(fakeiq_trials)  # add the loop to the experiment
thisFakeiq_trial = fakeiq_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFakeiq_trial.rgb)
if thisFakeiq_trial != None:
    for paramName in thisFakeiq_trial:
        exec('{} = thisFakeiq_trial[paramName]'.format(paramName))

for thisFakeiq_trial in fakeiq_trials:
    currentLoop = fakeiq_trials
    # abbreviate parameter names if possible (e.g. rgb = thisFakeiq_trial.rgb)
    if thisFakeiq_trial != None:
        for paramName in thisFakeiq_trial:
            exec('{} = thisFakeiq_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fakeiq_scale"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_raven.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    fakeiq_scaleComponents = [image_raven, key_resp]
    for thisComponent in fakeiq_scaleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fakeiq_scaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fakeiq_scale"-------
    while continueRoutine:
        # get current time
        t = fakeiq_scaleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fakeiq_scaleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_raven* updates
        if image_raven.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_raven.frameNStart = frameN  # exact frame index
            image_raven.tStart = t  # local t and not account for scr refresh
            image_raven.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_raven, 'tStartRefresh')  # time at next scr refresh
            image_raven.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fakeiq_scaleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fakeiq_scale"-------
    for thisComponent in fakeiq_scaleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fakeiq_trials.addData('image_raven.started', image_raven.tStartRefresh)
    fakeiq_trials.addData('image_raven.stopped', image_raven.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    fakeiq_trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        fakeiq_trials.addData('key_resp.rt', key_resp.rt)
    fakeiq_trials.addData('key_resp.started', key_resp.tStartRefresh)
    fakeiq_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "fakeiq_scale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'fakeiq_trials'


# ------Prepare to start Routine "preMFQ_instr"-------
continueRoutine = True
# update component parameters for each repeat
instr_premfq_key_resp.keys = []
instr_premfq_key_resp.rt = []
_instr_premfq_key_resp_allKeys = []
# keep track of which components have finished
preMFQ_instrComponents = [instr_premfq, instr_premfq_key_resp]
for thisComponent in preMFQ_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
preMFQ_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "preMFQ_instr"-------
while continueRoutine:
    # get current time
    t = preMFQ_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=preMFQ_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_premfq* updates
    if instr_premfq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_premfq.frameNStart = frameN  # exact frame index
        instr_premfq.tStart = t  # local t and not account for scr refresh
        instr_premfq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_premfq, 'tStartRefresh')  # time at next scr refresh
        instr_premfq.setAutoDraw(True)
    
    # *instr_premfq_key_resp* updates
    waitOnFlip = False
    if instr_premfq_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_premfq_key_resp.frameNStart = frameN  # exact frame index
        instr_premfq_key_resp.tStart = t  # local t and not account for scr refresh
        instr_premfq_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_premfq_key_resp, 'tStartRefresh')  # time at next scr refresh
        instr_premfq_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_premfq_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_premfq_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_premfq_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_premfq_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _instr_premfq_key_resp_allKeys.extend(theseKeys)
        if len(_instr_premfq_key_resp_allKeys):
            instr_premfq_key_resp.keys = _instr_premfq_key_resp_allKeys[-1].name  # just the last key pressed
            instr_premfq_key_resp.rt = _instr_premfq_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preMFQ_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "preMFQ_instr"-------
for thisComponent in preMFQ_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_premfq.started', instr_premfq.tStartRefresh)
thisExp.addData('instr_premfq.stopped', instr_premfq.tStopRefresh)
# check responses
if instr_premfq_key_resp.keys in ['', [], None]:  # No response was made
    instr_premfq_key_resp.keys = None
thisExp.addData('instr_premfq_key_resp.keys',instr_premfq_key_resp.keys)
if instr_premfq_key_resp.keys != None:  # we had a response
    thisExp.addData('instr_premfq_key_resp.rt', instr_premfq_key_resp.rt)
thisExp.addData('instr_premfq_key_resp.started', instr_premfq_key_resp.tStartRefresh)
thisExp.addData('instr_premfq_key_resp.stopped', instr_premfq_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "preMFQ_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MFQ1"-------
continueRoutine = True
# update component parameters for each repeat
mfq1_key_resp.keys = []
mfq1_key_resp.rt = []
_mfq1_key_resp_allKeys = []
# keep track of which components have finished
MFQ1Components = [MFQ_part1, mfq1_key_resp, space_instr, mfq1_instr, scale_instr_mfq1]
for thisComponent in MFQ1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MFQ1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MFQ1"-------
while continueRoutine:
    # get current time
    t = MFQ1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MFQ1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    MFQ_part1.draw()
    
    # *mfq1_key_resp* updates
    waitOnFlip = False
    if mfq1_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mfq1_key_resp.frameNStart = frameN  # exact frame index
        mfq1_key_resp.tStart = t  # local t and not account for scr refresh
        mfq1_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mfq1_key_resp, 'tStartRefresh')  # time at next scr refresh
        mfq1_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(mfq1_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(mfq1_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if mfq1_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = mfq1_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _mfq1_key_resp_allKeys.extend(theseKeys)
        if len(_mfq1_key_resp_allKeys):
            mfq1_key_resp.keys = _mfq1_key_resp_allKeys[-1].name  # just the last key pressed
            mfq1_key_resp.rt = _mfq1_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_instr* updates
    if space_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_instr.frameNStart = frameN  # exact frame index
        space_instr.tStart = t  # local t and not account for scr refresh
        space_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_instr, 'tStartRefresh')  # time at next scr refresh
        space_instr.setAutoDraw(True)
    
    # *mfq1_instr* updates
    if mfq1_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mfq1_instr.frameNStart = frameN  # exact frame index
        mfq1_instr.tStart = t  # local t and not account for scr refresh
        mfq1_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mfq1_instr, 'tStartRefresh')  # time at next scr refresh
        mfq1_instr.setAutoDraw(True)
    
    # *scale_instr_mfq1* updates
    if scale_instr_mfq1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scale_instr_mfq1.frameNStart = frameN  # exact frame index
        scale_instr_mfq1.tStart = t  # local t and not account for scr refresh
        scale_instr_mfq1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scale_instr_mfq1, 'tStartRefresh')  # time at next scr refresh
        scale_instr_mfq1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MFQ1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MFQ1"-------
for thisComponent in MFQ1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
MFQ_part1Data = MFQ_part1.getData()
while MFQ_part1Data['questions']:
    for dataTypes in MFQ_part1Data.keys():
        thisExp.addData(dataTypes, MFQ_part1Data[dataTypes].popleft())
    thisExp.nextEntry()
# check responses
if mfq1_key_resp.keys in ['', [], None]:  # No response was made
    mfq1_key_resp.keys = None
thisExp.addData('mfq1_key_resp.keys',mfq1_key_resp.keys)
if mfq1_key_resp.keys != None:  # we had a response
    thisExp.addData('mfq1_key_resp.rt', mfq1_key_resp.rt)
thisExp.addData('mfq1_key_resp.started', mfq1_key_resp.tStartRefresh)
thisExp.addData('mfq1_key_resp.stopped', mfq1_key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_instr.started', space_instr.tStartRefresh)
thisExp.addData('space_instr.stopped', space_instr.tStopRefresh)
thisExp.addData('mfq1_instr.started', mfq1_instr.tStartRefresh)
thisExp.addData('mfq1_instr.stopped', mfq1_instr.tStopRefresh)
thisExp.addData('scale_instr_mfq1.started', scale_instr_mfq1.tStartRefresh)
thisExp.addData('scale_instr_mfq1.stopped', scale_instr_mfq1.tStopRefresh)
# the Routine "MFQ1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MFQ2"-------
continueRoutine = True
# update component parameters for each repeat
mfq2_key_resp.keys = []
mfq2_key_resp.rt = []
_mfq2_key_resp_allKeys = []
# keep track of which components have finished
MFQ2Components = [MFQ_part2, mfq2_key_resp, space_instr_2, scale_instr_mfq1_2, mfq1_instr_2]
for thisComponent in MFQ2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MFQ2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MFQ2"-------
while continueRoutine:
    # get current time
    t = MFQ2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MFQ2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    MFQ_part2.draw()
    
    # *mfq2_key_resp* updates
    waitOnFlip = False
    if mfq2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mfq2_key_resp.frameNStart = frameN  # exact frame index
        mfq2_key_resp.tStart = t  # local t and not account for scr refresh
        mfq2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mfq2_key_resp, 'tStartRefresh')  # time at next scr refresh
        mfq2_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(mfq2_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(mfq2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if mfq2_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = mfq2_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _mfq2_key_resp_allKeys.extend(theseKeys)
        if len(_mfq2_key_resp_allKeys):
            mfq2_key_resp.keys = _mfq2_key_resp_allKeys[-1].name  # just the last key pressed
            mfq2_key_resp.rt = _mfq2_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_instr_2* updates
    if space_instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_instr_2.frameNStart = frameN  # exact frame index
        space_instr_2.tStart = t  # local t and not account for scr refresh
        space_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_instr_2, 'tStartRefresh')  # time at next scr refresh
        space_instr_2.setAutoDraw(True)
    
    # *scale_instr_mfq1_2* updates
    if scale_instr_mfq1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scale_instr_mfq1_2.frameNStart = frameN  # exact frame index
        scale_instr_mfq1_2.tStart = t  # local t and not account for scr refresh
        scale_instr_mfq1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scale_instr_mfq1_2, 'tStartRefresh')  # time at next scr refresh
        scale_instr_mfq1_2.setAutoDraw(True)
    
    # *mfq1_instr_2* updates
    if mfq1_instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mfq1_instr_2.frameNStart = frameN  # exact frame index
        mfq1_instr_2.tStart = t  # local t and not account for scr refresh
        mfq1_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mfq1_instr_2, 'tStartRefresh')  # time at next scr refresh
        mfq1_instr_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MFQ2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MFQ2"-------
for thisComponent in MFQ2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
MFQ_part2Data = MFQ_part2.getData()
while MFQ_part2Data['questions']:
    for dataTypes in MFQ_part2Data.keys():
        thisExp.addData(dataTypes, MFQ_part2Data[dataTypes].popleft())
    thisExp.nextEntry()
# check responses
if mfq2_key_resp.keys in ['', [], None]:  # No response was made
    mfq2_key_resp.keys = None
thisExp.addData('mfq2_key_resp.keys',mfq2_key_resp.keys)
if mfq2_key_resp.keys != None:  # we had a response
    thisExp.addData('mfq2_key_resp.rt', mfq2_key_resp.rt)
thisExp.addData('mfq2_key_resp.started', mfq2_key_resp.tStartRefresh)
thisExp.addData('mfq2_key_resp.stopped', mfq2_key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_instr_2.started', space_instr_2.tStartRefresh)
thisExp.addData('space_instr_2.stopped', space_instr_2.tStopRefresh)
thisExp.addData('scale_instr_mfq1_2.started', scale_instr_mfq1_2.tStartRefresh)
thisExp.addData('scale_instr_mfq1_2.stopped', scale_instr_mfq1_2.tStopRefresh)
thisExp.addData('mfq1_instr_2.started', mfq1_instr_2.tStartRefresh)
thisExp.addData('mfq1_instr_2.stopped', mfq1_instr_2.tStopRefresh)
# the Routine "MFQ2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "manipulation"-------
continueRoutine = True
# update component parameters for each repeat
with open(r'.\instructions\instr_cntrl.txt', 'r', encoding = 'utf-8') as f:
    instr_cntrl = f.read()
    
with open(r'.\instructions\instr_exprmntl.txt', 'r', encoding = 'utf-8') as f:
    instr_exprmntl = f.read()

condition = np.random.choice(['cntrl', 'exprmntl'])

if condition == 'cntrl':
    manip_txt = instr_cntrl
else:
    manip_txt = instr_exprmntl
manipulation_text.setText(manip_txt)
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
manipulationComponents = [manipulation_text, key_resp_2]
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
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "manipulation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demography"-------
continueRoutine = True
# update component parameters for each repeat
demo_key_resp.keys = []
demo_key_resp.rt = []
_demo_key_resp_allKeys = []
# keep track of which components have finished
demographyComponents = [demography_form, demo_key_resp, space_instr_3]
for thisComponent in demographyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demographyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demography"-------
while continueRoutine:
    # get current time
    t = demographyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demographyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    demography_form.draw()
    
    # *demo_key_resp* updates
    waitOnFlip = False
    if demo_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_key_resp.frameNStart = frameN  # exact frame index
        demo_key_resp.tStart = t  # local t and not account for scr refresh
        demo_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_key_resp, 'tStartRefresh')  # time at next scr refresh
        demo_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demo_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demo_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demo_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = demo_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _demo_key_resp_allKeys.extend(theseKeys)
        if len(_demo_key_resp_allKeys):
            demo_key_resp.keys = _demo_key_resp_allKeys[-1].name  # just the last key pressed
            demo_key_resp.rt = _demo_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_instr_3* updates
    if space_instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_instr_3.frameNStart = frameN  # exact frame index
        space_instr_3.tStart = t  # local t and not account for scr refresh
        space_instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_instr_3, 'tStartRefresh')  # time at next scr refresh
        space_instr_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demographyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demography"-------
for thisComponent in demographyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
demography_formData = demography_form.getData()
while demography_formData['questions']:
    for dataTypes in demography_formData.keys():
        thisExp.addData(dataTypes, demography_formData[dataTypes].popleft())
    thisExp.nextEntry()
# check responses
if demo_key_resp.keys in ['', [], None]:  # No response was made
    demo_key_resp.keys = None
thisExp.addData('demo_key_resp.keys',demo_key_resp.keys)
if demo_key_resp.keys != None:  # we had a response
    thisExp.addData('demo_key_resp.rt', demo_key_resp.rt)
thisExp.addData('demo_key_resp.started', demo_key_resp.tStartRefresh)
thisExp.addData('demo_key_resp.stopped', demo_key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_instr_3.started', space_instr_3.tStartRefresh)
thisExp.addData('space_instr_3.stopped', space_instr_3.tStopRefresh)
# the Routine "demography" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
