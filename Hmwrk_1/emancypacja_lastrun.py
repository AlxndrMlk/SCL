#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on April 25, 2020, at 19:50
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
expName = 'emancypacja'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\aleksander.molak\\Documents\\Personal\\Psych\\SOCIAL_COGN_LAB\\SCL\\Hmwrk_1\\emancypacja_lastrun.py',
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

# Initialize components for Routine "ldt_instr"
ldt_instrClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='Na ekranie będą pojawiać się ciągi liter.\n\nWciśnij F gdy na ekranie pojawi się ciąg niebędący słowem.\nWciśnij J gdy na ekranie pojawi się ciąg będący słowem.\n\nPołóż palce wskazujące obu rąk na klawiszach F i J.\nNastępnie wciśnij spację, aby rozpocząć.',
    font='Arial',
    pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "ldt_task"
ldt_taskClock = core.Clock()
ldt_string = visual.TextStim(win=win, name='ldt_string',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ldt_key_resp = keyboard.Keyboard()
label_left = visual.TextStim(win=win, name='label_left',
    text='f = nie-słowo',
    font='Arial',
    pos=(-.53, .45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
label_right = visual.TextStim(win=win, name='label_right',
    text='j = słowo',
    font='Arial',
    pos=(.59, .45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ldt_feedback"
ldt_feedbackClock = core.Clock()
feed_text = ""
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "demographics"
demographicsClock = core.Clock()
to_finish = visual.TextStim(win=win, name='to_finish',
    text='Aby zakończyć, proszę wcisnąć spację',
    font='Arial',
    pos=(0, -.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
win.allowStencil = True
demo = visual.Form(win=win, name='demo',
    items='demografia2.xlsx',
    textHeight=0.02,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05)
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ldt_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
ldt_instrComponents = [instr, key_resp]
for thisComponent in ldt_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ldt_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ldt_instr"-------
while continueRoutine:
    # get current time
    t = ldt_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ldt_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        instr.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ldt_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ldt_instr"-------
for thisComponent in ldt_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr.started', instr.tStartRefresh)
thisExp.addData('instr.stopped', instr.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "ldt_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ldt_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli.xlsx'),
    seed=None, name='ldt_trials')
thisExp.addLoop(ldt_trials)  # add the loop to the experiment
thisLdt_trial = ldt_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLdt_trial.rgb)
if thisLdt_trial != None:
    for paramName in thisLdt_trial:
        exec('{} = thisLdt_trial[paramName]'.format(paramName))

for thisLdt_trial in ldt_trials:
    currentLoop = ldt_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLdt_trial.rgb)
    if thisLdt_trial != None:
        for paramName in thisLdt_trial:
            exec('{} = thisLdt_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ldt_task"-------
    continueRoutine = True
    # update component parameters for each repeat
    ldt_string.setText(strings)
    ldt_key_resp.keys = []
    ldt_key_resp.rt = []
    _ldt_key_resp_allKeys = []
    # keep track of which components have finished
    ldt_taskComponents = [ldt_string, ldt_key_resp, label_left, label_right]
    for thisComponent in ldt_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ldt_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ldt_task"-------
    while continueRoutine:
        # get current time
        t = ldt_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ldt_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ldt_string* updates
        if ldt_string.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldt_string.frameNStart = frameN  # exact frame index
            ldt_string.tStart = t  # local t and not account for scr refresh
            ldt_string.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldt_string, 'tStartRefresh')  # time at next scr refresh
            ldt_string.setAutoDraw(True)
        
        # *ldt_key_resp* updates
        waitOnFlip = False
        if ldt_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldt_key_resp.frameNStart = frameN  # exact frame index
            ldt_key_resp.tStart = t  # local t and not account for scr refresh
            ldt_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldt_key_resp, 'tStartRefresh')  # time at next scr refresh
            ldt_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ldt_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ldt_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ldt_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = ldt_key_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _ldt_key_resp_allKeys.extend(theseKeys)
            if len(_ldt_key_resp_allKeys):
                ldt_key_resp.keys = _ldt_key_resp_allKeys[0].name  # just the first key pressed
                ldt_key_resp.rt = _ldt_key_resp_allKeys[0].rt
                # was this correct?
                if (ldt_key_resp.keys == str(correct)) or (ldt_key_resp.keys == correct):
                    ldt_key_resp.corr = 1
                else:
                    ldt_key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *label_left* updates
        if label_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_left.frameNStart = frameN  # exact frame index
            label_left.tStart = t  # local t and not account for scr refresh
            label_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_left, 'tStartRefresh')  # time at next scr refresh
            label_left.setAutoDraw(True)
        
        # *label_right* updates
        if label_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_right.frameNStart = frameN  # exact frame index
            label_right.tStart = t  # local t and not account for scr refresh
            label_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_right, 'tStartRefresh')  # time at next scr refresh
            label_right.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ldt_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ldt_task"-------
    for thisComponent in ldt_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ldt_trials.addData('ldt_string.started', ldt_string.tStartRefresh)
    ldt_trials.addData('ldt_string.stopped', ldt_string.tStopRefresh)
    # check responses
    if ldt_key_resp.keys in ['', [], None]:  # No response was made
        ldt_key_resp.keys = None
        # was no response the correct answer?!
        if str(correct).lower() == 'none':
           ldt_key_resp.corr = 1;  # correct non-response
        else:
           ldt_key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for ldt_trials (TrialHandler)
    ldt_trials.addData('ldt_key_resp.keys',ldt_key_resp.keys)
    ldt_trials.addData('ldt_key_resp.corr', ldt_key_resp.corr)
    if ldt_key_resp.keys != None:  # we had a response
        ldt_trials.addData('ldt_key_resp.rt', ldt_key_resp.rt)
    ldt_trials.addData('ldt_key_resp.started', ldt_key_resp.tStartRefresh)
    ldt_trials.addData('ldt_key_resp.stopped', ldt_key_resp.tStopRefresh)
    ldt_trials.addData('label_left.started', label_left.tStartRefresh)
    ldt_trials.addData('label_left.stopped', label_left.tStopRefresh)
    ldt_trials.addData('label_right.started', label_right.tStartRefresh)
    ldt_trials.addData('label_right.stopped', label_right.tStopRefresh)
    # the Routine "ldt_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ldt_feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if ldt_key_resp.corr:
        feedback_text.color = "green"
        feed_text = "dobrze"
    else:
        feedback_text.color = "red"
        feed_text = "źle"
    feedback_text.setText(feed_text)
    # keep track of which components have finished
    ldt_feedbackComponents = [feedback_text]
    for thisComponent in ldt_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ldt_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ldt_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ldt_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ldt_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ldt_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ldt_feedback"-------
    for thisComponent in ldt_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ldt_trials.addData('feedback_text.started', feedback_text.tStartRefresh)
    ldt_trials.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'ldt_trials'


# ------Prepare to start Routine "demographics"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
demographicsComponents = [to_finish, demo, key_resp_2]
for thisComponent in demographicsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demographicsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demographics"-------
while continueRoutine:
    # get current time
    t = demographicsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demographicsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *to_finish* updates
    if to_finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        to_finish.frameNStart = frameN  # exact frame index
        to_finish.tStart = t  # local t and not account for scr refresh
        to_finish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(to_finish, 'tStartRefresh')  # time at next scr refresh
        to_finish.setAutoDraw(True)
    demo.draw()
    
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
    for thisComponent in demographicsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demographics"-------
for thisComponent in demographicsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('to_finish.started', to_finish.tStartRefresh)
thisExp.addData('to_finish.stopped', to_finish.tStopRefresh)
demoData = demo.getData()
while demoData['questions']:
    for dataTypes in demoData.keys():
        thisExp.addData(dataTypes, demoData[dataTypes].popleft())
    thisExp.nextEntry()
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "demographics" was not non-slip safe, so reset the non-slip timer
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
