/***************** 
 * Macbeth1 Test *
 *****************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'macbeth1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
flowScheduler.add(relationship_scaleRoutineBegin());
flowScheduler.add(relationship_scaleRoutineEachFrame());
flowScheduler.add(relationship_scaleRoutineEnd());
flowScheduler.add(preMFQ_instrRoutineBegin());
flowScheduler.add(preMFQ_instrRoutineEachFrame());
flowScheduler.add(preMFQ_instrRoutineEnd());
flowScheduler.add(MFQ1RoutineBegin());
flowScheduler.add(MFQ1RoutineEachFrame());
flowScheduler.add(MFQ1RoutineEnd());
flowScheduler.add(MFQ2RoutineBegin());
flowScheduler.add(MFQ2RoutineEachFrame());
flowScheduler.add(MFQ2RoutineEnd());
flowScheduler.add(manipulationRoutineBegin());
flowScheduler.add(manipulationRoutineEachFrame());
flowScheduler.add(manipulationRoutineEnd());
flowScheduler.add(fakeiq_scale_instrRoutineBegin());
flowScheduler.add(fakeiq_scale_instrRoutineEachFrame());
flowScheduler.add(fakeiq_scale_instrRoutineEnd());
flowScheduler.add(fakeiq_scale2RoutineBegin());
flowScheduler.add(fakeiq_scale2RoutineEachFrame());
flowScheduler.add(fakeiq_scale2RoutineEnd());
flowScheduler.add(demographyRoutineBegin());
flowScheduler.add(demographyRoutineEachFrame());
flowScheduler.add(demographyRoutineEnd());
flowScheduler.add(debriefingRoutineBegin());
flowScheduler.add(debriefingRoutineEachFrame());
flowScheduler.add(debriefingRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var introClock;
var intro_text;
var space_instr_intro;
var intro_key_resp;
var relationship_scaleClock;
var space_instr_4;
var relationship_key_resp;
var relationship_instr;
var preMFQ_instrClock;
var instr_premfq;
var instr_premfq_key_resp;
var MFQ1Clock;
var mfq1_key_resp;
var space_instr;
var mfq1_instr;
var scale_instr_mfq1;
var MFQ2Clock;
var mfq2_key_resp;
var space_instr_2;
var scale_instr_mfq1_2;
var mfq1_instr_2;
var manipulationClock;
var manip_txt;
var manipulation_text;
var key_resp_2;
var fakeiq_scale_instrClock;
var instr_fakeiq;
var instr_fakeiq_key_resp;
var fakeiq_scale2Clock;
var space_instr_fake_iq;
var fakeiq2_key_resp;
var demographyClock;
var demo_key_resp;
var space_instr_3;
var debriefingClock;
var debriefing_text;
var debriefing_key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro_text',
    text: 'Dzień dobry,\n\nJesteśmy studentami Wydziału Psychologii Uniwersytetu Warszawskiego i przeprowadzamy badanie na temat wpływu jakości relacji z drugą osobą na funkcjonowanie poznawcze. Badanie będzie składać się z dwóch głównych części. W pierwszej części badania będziemy chcieli dowiedzieć się jak najwięcej na temat Pani/Pana bliskiej relacji z drugą osobą. W tym celu poprosimy o udzielenie odpowiedzi na zadane pytania oraz przypomnienie sobie pewnych wydarzeń z Pani/Pana życia. Druga część badania dotyczyć będzie funkcjonowania poznawczego. Poprosimy Panią/Pana o wykonanie kilku zadań, które będą sprawdzały Pani/Pana umiejętności w różnych obszarach poznawczych. \n\nW badaniu mogą wziąć udział wyłącznie osoby pełnoletnie. \n\nProsimy pamiętać, że badanie jest całkowicie anonimowe, a wyniki będą analizowane wyłącznie zbiorczo. Państwa odpowiedzi będą traktowane w sposób zupełnie poufny. Mogą Państwo zrezygnować z uczestnictwa w badaniu w dowolnym momencie. W razie wszelkich pytań zapraszamy do kontaktu pod adresem mailowym: k.zochniak@student.uw.edu.pl\n\nMaksymilian Koc, Aleksander Molak, Kamila Zochniak\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  space_instr_intro = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_instr_intro',
    text: 'Aby wziąć udział w badaniu, naciśnij spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  intro_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "relationship_scale"
  relationship_scaleClock = new util.Clock();
  space_instr_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_instr_4',
    text: 'Aby przejść do kolejnej części badania, naciśnij spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  relationship_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  relationship_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'relationship_instr',
    text: 'Prosimy o udzielenie odpowiedzi na poniższe pytania:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.43], height: 0.026,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "preMFQ_instr"
  preMFQ_instrClock = new util.Clock();
  instr_premfq = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_premfq',
    text: 'W tej części badania poprosimy Pana/Panią o odpowiedź na pytania dotyczące tego, co uważa Pan/Pani za dobre lub złe.\n\nAby kontynuować, prosimy nacisnąć spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_premfq_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "MFQ1"
  MFQ1Clock = new util.Clock();
  mfq1_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_instr',
    text: 'Aby przejść do kolejnej części badania, naciśnij spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  mfq1_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'mfq1_instr',
    text: 'Ludzie, oceniając w życiu codziennym, czy dane zachowanie jest dobre,\nczy złe, biorą pod uwagę różne kryteria. W jakim stopniu poniższe kryteria\nsą ważne dla Pani/Pana przy ocenie danego zachowania jako dobre lub złe? \nProsimy odpowiedzieć zgodnie z poniższą skalą, zaznaczając przy odpowiedniej liczbie:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.43], height: 0.023,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  scale_instr_mfq1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_instr_mfq1',
    text: '1 Zdecydowanie nieważne\n2 Nieważne\n3 Raczej nieważne\n4 Raczej ważne\n5 Ważne\n6 Zdecydowanie ważne',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.7), 0.26], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "MFQ2"
  MFQ2Clock = new util.Clock();
  mfq2_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_instr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_instr_2',
    text: 'Aby przejść do kolejnej części badania, naciśnij spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  scale_instr_mfq1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_instr_mfq1_2',
    text: '1 Zdecydowanie się nie zgadzam\n2 Nie zgadzam się\n3 Raczej się nie zgadzam\n4 Raczej się zgadzam\n5 Zgadzam się\n6 Zdecydowanie się zgadzam',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.7), 0.26], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  mfq1_instr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mfq1_instr_2',
    text: 'Prosimy o przeczytanie poniższych stwierdzeń i ustosunkowanie się\ndo nich zgodnie z poniższą skalą, zaznaczając przy odpowiedniej liczbie:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.43], height: 0.023,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "manipulation"
  manipulationClock = new util.Clock();
  manip_txt = "";
  
  manipulation_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'manipulation_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fakeiq_scale_instr"
  fakeiq_scale_instrClock = new util.Clock();
  instr_fakeiq = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_fakeiq',
    text: 'W tej części badania poprosimy Pana/Panią o rozwiązanie kilku zadań mierzących zdolności poznawcze. \n\nAby kontynuować, prosimy nacisnąć spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_fakeiq_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fakeiq_scale2"
  fakeiq_scale2Clock = new util.Clock();
  space_instr_fake_iq = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_instr_fake_iq',
    text: 'Aby przejść do kolejnej części badania, naciśnij spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  fakeiq2_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demography"
  demographyClock = new util.Clock();
  demo_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_instr_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_instr_3',
    text: 'Aby przejść do kolejnej części badania, naciśnij spację.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "debriefing"
  debriefingClock = new util.Clock();
  debriefing_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'debriefing_text',
    text: 'Dziękujemy za udział w badaniu “Tales of moderate(d) impurity”. Przypominamy, że udział w badaniu był anonimowy, a wyniki będą opracowywane wyłącznie zbiorczo. \n\nW niniejszym badaniu chcieliśmy sprawdzić, dlaczego niektórzy ludzie postrzegają dane zachowanie jako moralne, podczas gdy inni uważają przeciwnie, oraz czy przekonania te mają związek z wyborem różnych produktów. Spodziewamy się, że przypomnienie aktu uważanego przez osobę za niemoralny będzie prowadzić do częstszego wyboru produktów czyszczących.  \n\nW badaniu zostali Państwo losowo przydzieleni do jednego z dwóch warunków eksperymentalnych. Część z Państwa została poproszona o przypomnienie sobie intymnej sytuacji, podczas gdy część z osób badanych nie otrzymała takiej prośby. Dla niektórych osób taka prośba może być krępująca albo powodować nieprzyjemne bądź kłopotliwe uczucia lub myśli. Takie uczucia lub myśli mogą utrzymywać się przez jakiś czas po zakończeniu badania. Jest to zupełnie naturalne. \n\nDruga część badania, w której wzięli Państwo udział, dotyczyła wyboru produktów. Chcielibyśmy podkreślić, że nie było wśród nich wyborów poprawnych lub niepoprawnych. Zadanie służyło wyłącznie poznaniu preferencji uczestników badania dotyczących danych produktów. \n\nW dalszym ciągu mogą Państwo zrezygnować z udziału w badaniu. Aby to zrobić, należy zamknąć kartę przeglądarki, nie przechodząc na kolejny ekran. Jeżeli mają Państwo jakiekolwiek pytania lub wątpliwości związane z badaniem, prosimy o kontakt pod adresem ……………….\n\nJesteśmy Państwu bardzo wdzięczni za udział w badaniu. Rozwój nauki możliwy jest dzięki osobom takim jak Państwo!\n\nAby zakończyć badanie, prosimy nacisnąć spację.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  debriefing_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _intro_key_resp_allKeys;
var introComponents;
function introRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'intro'-------
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    intro_key_resp.keys = undefined;
    intro_key_resp.rt = undefined;
    _intro_key_resp_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(intro_text);
    introComponents.push(space_instr_intro);
    introComponents.push(intro_key_resp);
    
    for (const thisComponent of introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function introRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'intro'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro_text* updates
    if (t >= 0.0 && intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_text.tStart = t;  // (not accounting for frame time here)
      intro_text.frameNStart = frameN;  // exact frame index
      
      intro_text.setAutoDraw(true);
    }

    
    // *space_instr_intro* updates
    if (t >= 0.0 && space_instr_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_instr_intro.tStart = t;  // (not accounting for frame time here)
      space_instr_intro.frameNStart = frameN;  // exact frame index
      
      space_instr_intro.setAutoDraw(true);
    }

    
    // *intro_key_resp* updates
    if (t >= 0.0 && intro_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_key_resp.tStart = t;  // (not accounting for frame time here)
      intro_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { intro_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { intro_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { intro_key_resp.clearEvents(); });
    }

    if (intro_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = intro_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _intro_key_resp_allKeys = _intro_key_resp_allKeys.concat(theseKeys);
      if (_intro_key_resp_allKeys.length > 0) {
        intro_key_resp.keys = _intro_key_resp_allKeys[_intro_key_resp_allKeys.length - 1].name;  // just the last key pressed
        intro_key_resp.rt = _intro_key_resp_allKeys[_intro_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'intro'-------
    for (const thisComponent of introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('intro_key_resp.keys', intro_key_resp.keys);
    if (typeof intro_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('intro_key_resp.rt', intro_key_resp.rt);
        routineTimer.reset();
        }
    
    intro_key_resp.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _relationship_key_resp_allKeys;
var relationship_scaleComponents;
function relationship_scaleRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'relationship_scale'-------
    t = 0;
    relationship_scaleClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    relationship_key_resp.keys = undefined;
    relationship_key_resp.rt = undefined;
    _relationship_key_resp_allKeys = [];
    // keep track of which components have finished
    relationship_scaleComponents = [];
    relationship_scaleComponents.push(space_instr_4);
    relationship_scaleComponents.push(relationship_key_resp);
    relationship_scaleComponents.push(relationship_instr);
    
    for (const thisComponent of relationship_scaleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function relationship_scaleRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'relationship_scale'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = relationship_scaleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *space_instr_4* updates
    if (t >= 0.0 && space_instr_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_instr_4.tStart = t;  // (not accounting for frame time here)
      space_instr_4.frameNStart = frameN;  // exact frame index
      
      space_instr_4.setAutoDraw(true);
    }

    
    // *relationship_key_resp* updates
    if (t >= 0.0 && relationship_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      relationship_key_resp.tStart = t;  // (not accounting for frame time here)
      relationship_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { relationship_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { relationship_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { relationship_key_resp.clearEvents(); });
    }

    if (relationship_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = relationship_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _relationship_key_resp_allKeys = _relationship_key_resp_allKeys.concat(theseKeys);
      if (_relationship_key_resp_allKeys.length > 0) {
        relationship_key_resp.keys = _relationship_key_resp_allKeys[_relationship_key_resp_allKeys.length - 1].name;  // just the last key pressed
        relationship_key_resp.rt = _relationship_key_resp_allKeys[_relationship_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *relationship_instr* updates
    if (t >= 0.0 && relationship_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      relationship_instr.tStart = t;  // (not accounting for frame time here)
      relationship_instr.frameNStart = frameN;  // exact frame index
      
      relationship_instr.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of relationship_scaleComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function relationship_scaleRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'relationship_scale'-------
    for (const thisComponent of relationship_scaleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('relationship_key_resp.keys', relationship_key_resp.keys);
    if (typeof relationship_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('relationship_key_resp.rt', relationship_key_resp.rt);
        routineTimer.reset();
        }
    
    relationship_key_resp.stop();
    // the Routine "relationship_scale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instr_premfq_key_resp_allKeys;
var preMFQ_instrComponents;
function preMFQ_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'preMFQ_instr'-------
    t = 0;
    preMFQ_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instr_premfq_key_resp.keys = undefined;
    instr_premfq_key_resp.rt = undefined;
    _instr_premfq_key_resp_allKeys = [];
    // keep track of which components have finished
    preMFQ_instrComponents = [];
    preMFQ_instrComponents.push(instr_premfq);
    preMFQ_instrComponents.push(instr_premfq_key_resp);
    
    for (const thisComponent of preMFQ_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function preMFQ_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'preMFQ_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = preMFQ_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_premfq* updates
    if (t >= 0.0 && instr_premfq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_premfq.tStart = t;  // (not accounting for frame time here)
      instr_premfq.frameNStart = frameN;  // exact frame index
      
      instr_premfq.setAutoDraw(true);
    }

    
    // *instr_premfq_key_resp* updates
    if (t >= 0.0 && instr_premfq_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_premfq_key_resp.tStart = t;  // (not accounting for frame time here)
      instr_premfq_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instr_premfq_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instr_premfq_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instr_premfq_key_resp.clearEvents(); });
    }

    if (instr_premfq_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instr_premfq_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instr_premfq_key_resp_allKeys = _instr_premfq_key_resp_allKeys.concat(theseKeys);
      if (_instr_premfq_key_resp_allKeys.length > 0) {
        instr_premfq_key_resp.keys = _instr_premfq_key_resp_allKeys[_instr_premfq_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instr_premfq_key_resp.rt = _instr_premfq_key_resp_allKeys[_instr_premfq_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of preMFQ_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function preMFQ_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'preMFQ_instr'-------
    for (const thisComponent of preMFQ_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr_premfq_key_resp.keys', instr_premfq_key_resp.keys);
    if (typeof instr_premfq_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instr_premfq_key_resp.rt', instr_premfq_key_resp.rt);
        routineTimer.reset();
        }
    
    instr_premfq_key_resp.stop();
    // the Routine "preMFQ_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _mfq1_key_resp_allKeys;
var MFQ1Components;
function MFQ1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'MFQ1'-------
    t = 0;
    MFQ1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    mfq1_key_resp.keys = undefined;
    mfq1_key_resp.rt = undefined;
    _mfq1_key_resp_allKeys = [];
    // keep track of which components have finished
    MFQ1Components = [];
    MFQ1Components.push(mfq1_key_resp);
    MFQ1Components.push(space_instr);
    MFQ1Components.push(mfq1_instr);
    MFQ1Components.push(scale_instr_mfq1);
    
    for (const thisComponent of MFQ1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function MFQ1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'MFQ1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = MFQ1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mfq1_key_resp* updates
    if (t >= 0.0 && mfq1_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mfq1_key_resp.tStart = t;  // (not accounting for frame time here)
      mfq1_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { mfq1_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { mfq1_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { mfq1_key_resp.clearEvents(); });
    }

    if (mfq1_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = mfq1_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _mfq1_key_resp_allKeys = _mfq1_key_resp_allKeys.concat(theseKeys);
      if (_mfq1_key_resp_allKeys.length > 0) {
        mfq1_key_resp.keys = _mfq1_key_resp_allKeys[_mfq1_key_resp_allKeys.length - 1].name;  // just the last key pressed
        mfq1_key_resp.rt = _mfq1_key_resp_allKeys[_mfq1_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_instr* updates
    if (t >= 0.0 && space_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_instr.tStart = t;  // (not accounting for frame time here)
      space_instr.frameNStart = frameN;  // exact frame index
      
      space_instr.setAutoDraw(true);
    }

    
    // *mfq1_instr* updates
    if (t >= 0.0 && mfq1_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mfq1_instr.tStart = t;  // (not accounting for frame time here)
      mfq1_instr.frameNStart = frameN;  // exact frame index
      
      mfq1_instr.setAutoDraw(true);
    }

    
    // *scale_instr_mfq1* updates
    if (t >= 0.0 && scale_instr_mfq1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      scale_instr_mfq1.tStart = t;  // (not accounting for frame time here)
      scale_instr_mfq1.frameNStart = frameN;  // exact frame index
      
      scale_instr_mfq1.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MFQ1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MFQ1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'MFQ1'-------
    for (const thisComponent of MFQ1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('mfq1_key_resp.keys', mfq1_key_resp.keys);
    if (typeof mfq1_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('mfq1_key_resp.rt', mfq1_key_resp.rt);
        routineTimer.reset();
        }
    
    mfq1_key_resp.stop();
    // the Routine "MFQ1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _mfq2_key_resp_allKeys;
var MFQ2Components;
function MFQ2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'MFQ2'-------
    t = 0;
    MFQ2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    mfq2_key_resp.keys = undefined;
    mfq2_key_resp.rt = undefined;
    _mfq2_key_resp_allKeys = [];
    // keep track of which components have finished
    MFQ2Components = [];
    MFQ2Components.push(mfq2_key_resp);
    MFQ2Components.push(space_instr_2);
    MFQ2Components.push(scale_instr_mfq1_2);
    MFQ2Components.push(mfq1_instr_2);
    
    for (const thisComponent of MFQ2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function MFQ2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'MFQ2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = MFQ2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mfq2_key_resp* updates
    if (t >= 0.0 && mfq2_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mfq2_key_resp.tStart = t;  // (not accounting for frame time here)
      mfq2_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { mfq2_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { mfq2_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { mfq2_key_resp.clearEvents(); });
    }

    if (mfq2_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = mfq2_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _mfq2_key_resp_allKeys = _mfq2_key_resp_allKeys.concat(theseKeys);
      if (_mfq2_key_resp_allKeys.length > 0) {
        mfq2_key_resp.keys = _mfq2_key_resp_allKeys[_mfq2_key_resp_allKeys.length - 1].name;  // just the last key pressed
        mfq2_key_resp.rt = _mfq2_key_resp_allKeys[_mfq2_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_instr_2* updates
    if (t >= 0.0 && space_instr_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_instr_2.tStart = t;  // (not accounting for frame time here)
      space_instr_2.frameNStart = frameN;  // exact frame index
      
      space_instr_2.setAutoDraw(true);
    }

    
    // *scale_instr_mfq1_2* updates
    if (t >= 0.0 && scale_instr_mfq1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      scale_instr_mfq1_2.tStart = t;  // (not accounting for frame time here)
      scale_instr_mfq1_2.frameNStart = frameN;  // exact frame index
      
      scale_instr_mfq1_2.setAutoDraw(true);
    }

    
    // *mfq1_instr_2* updates
    if (t >= 0.0 && mfq1_instr_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mfq1_instr_2.tStart = t;  // (not accounting for frame time here)
      mfq1_instr_2.frameNStart = frameN;  // exact frame index
      
      mfq1_instr_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MFQ2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MFQ2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'MFQ2'-------
    for (const thisComponent of MFQ2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('mfq2_key_resp.keys', mfq2_key_resp.keys);
    if (typeof mfq2_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('mfq2_key_resp.rt', mfq2_key_resp.rt);
        routineTimer.reset();
        }
    
    mfq2_key_resp.stop();
    // the Routine "MFQ2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var manipulationComponents;
function manipulationRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'manipulation'-------
    t = 0;
    manipulationClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    manipulation_text.setText(manip_txt);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    manipulationComponents = [];
    manipulationComponents.push(manipulation_text);
    manipulationComponents.push(key_resp_2);
    
    for (const thisComponent of manipulationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function manipulationRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'manipulation'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = manipulationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *manipulation_text* updates
    if (t >= 0.0 && manipulation_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      manipulation_text.tStart = t;  // (not accounting for frame time here)
      manipulation_text.frameNStart = frameN;  // exact frame index
      
      manipulation_text.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of manipulationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function manipulationRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'manipulation'-------
    for (const thisComponent of manipulationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "manipulation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instr_fakeiq_key_resp_allKeys;
var fakeiq_scale_instrComponents;
function fakeiq_scale_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'fakeiq_scale_instr'-------
    t = 0;
    fakeiq_scale_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instr_fakeiq_key_resp.keys = undefined;
    instr_fakeiq_key_resp.rt = undefined;
    _instr_fakeiq_key_resp_allKeys = [];
    // keep track of which components have finished
    fakeiq_scale_instrComponents = [];
    fakeiq_scale_instrComponents.push(instr_fakeiq);
    fakeiq_scale_instrComponents.push(instr_fakeiq_key_resp);
    
    for (const thisComponent of fakeiq_scale_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function fakeiq_scale_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'fakeiq_scale_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fakeiq_scale_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_fakeiq* updates
    if (t >= 0.0 && instr_fakeiq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_fakeiq.tStart = t;  // (not accounting for frame time here)
      instr_fakeiq.frameNStart = frameN;  // exact frame index
      
      instr_fakeiq.setAutoDraw(true);
    }

    
    // *instr_fakeiq_key_resp* updates
    if (t >= 0.0 && instr_fakeiq_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_fakeiq_key_resp.tStart = t;  // (not accounting for frame time here)
      instr_fakeiq_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instr_fakeiq_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instr_fakeiq_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instr_fakeiq_key_resp.clearEvents(); });
    }

    if (instr_fakeiq_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instr_fakeiq_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instr_fakeiq_key_resp_allKeys = _instr_fakeiq_key_resp_allKeys.concat(theseKeys);
      if (_instr_fakeiq_key_resp_allKeys.length > 0) {
        instr_fakeiq_key_resp.keys = _instr_fakeiq_key_resp_allKeys[_instr_fakeiq_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instr_fakeiq_key_resp.rt = _instr_fakeiq_key_resp_allKeys[_instr_fakeiq_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fakeiq_scale_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fakeiq_scale_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'fakeiq_scale_instr'-------
    for (const thisComponent of fakeiq_scale_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr_fakeiq_key_resp.keys', instr_fakeiq_key_resp.keys);
    if (typeof instr_fakeiq_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instr_fakeiq_key_resp.rt', instr_fakeiq_key_resp.rt);
        routineTimer.reset();
        }
    
    instr_fakeiq_key_resp.stop();
    // the Routine "fakeiq_scale_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fakeiq2_key_resp_allKeys;
var fakeiq_scale2Components;
function fakeiq_scale2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'fakeiq_scale2'-------
    t = 0;
    fakeiq_scale2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    fakeiq2_key_resp.keys = undefined;
    fakeiq2_key_resp.rt = undefined;
    _fakeiq2_key_resp_allKeys = [];
    // keep track of which components have finished
    fakeiq_scale2Components = [];
    fakeiq_scale2Components.push(space_instr_fake_iq);
    fakeiq_scale2Components.push(fakeiq2_key_resp);
    
    for (const thisComponent of fakeiq_scale2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function fakeiq_scale2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'fakeiq_scale2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fakeiq_scale2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *space_instr_fake_iq* updates
    if (t >= 0.0 && space_instr_fake_iq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_instr_fake_iq.tStart = t;  // (not accounting for frame time here)
      space_instr_fake_iq.frameNStart = frameN;  // exact frame index
      
      space_instr_fake_iq.setAutoDraw(true);
    }

    
    // *fakeiq2_key_resp* updates
    if (t >= 0.0 && fakeiq2_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fakeiq2_key_resp.tStart = t;  // (not accounting for frame time here)
      fakeiq2_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fakeiq2_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fakeiq2_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fakeiq2_key_resp.clearEvents(); });
    }

    if (fakeiq2_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = fakeiq2_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _fakeiq2_key_resp_allKeys = _fakeiq2_key_resp_allKeys.concat(theseKeys);
      if (_fakeiq2_key_resp_allKeys.length > 0) {
        fakeiq2_key_resp.keys = _fakeiq2_key_resp_allKeys[_fakeiq2_key_resp_allKeys.length - 1].name;  // just the last key pressed
        fakeiq2_key_resp.rt = _fakeiq2_key_resp_allKeys[_fakeiq2_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fakeiq_scale2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fakeiq_scale2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'fakeiq_scale2'-------
    for (const thisComponent of fakeiq_scale2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fakeiq2_key_resp.keys', fakeiq2_key_resp.keys);
    if (typeof fakeiq2_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fakeiq2_key_resp.rt', fakeiq2_key_resp.rt);
        routineTimer.reset();
        }
    
    fakeiq2_key_resp.stop();
    // the Routine "fakeiq_scale2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _demo_key_resp_allKeys;
var demographyComponents;
function demographyRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'demography'-------
    t = 0;
    demographyClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    demo_key_resp.keys = undefined;
    demo_key_resp.rt = undefined;
    _demo_key_resp_allKeys = [];
    // keep track of which components have finished
    demographyComponents = [];
    demographyComponents.push(demo_key_resp);
    demographyComponents.push(space_instr_3);
    
    for (const thisComponent of demographyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function demographyRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'demography'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = demographyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demo_key_resp* updates
    if (t >= 0.0 && demo_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_key_resp.tStart = t;  // (not accounting for frame time here)
      demo_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demo_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demo_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demo_key_resp.clearEvents(); });
    }

    if (demo_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = demo_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _demo_key_resp_allKeys = _demo_key_resp_allKeys.concat(theseKeys);
      if (_demo_key_resp_allKeys.length > 0) {
        demo_key_resp.keys = _demo_key_resp_allKeys[_demo_key_resp_allKeys.length - 1].name;  // just the last key pressed
        demo_key_resp.rt = _demo_key_resp_allKeys[_demo_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_instr_3* updates
    if (t >= 0.0 && space_instr_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_instr_3.tStart = t;  // (not accounting for frame time here)
      space_instr_3.frameNStart = frameN;  // exact frame index
      
      space_instr_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of demographyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demographyRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'demography'-------
    for (const thisComponent of demographyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('demo_key_resp.keys', demo_key_resp.keys);
    if (typeof demo_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('demo_key_resp.rt', demo_key_resp.rt);
        routineTimer.reset();
        }
    
    demo_key_resp.stop();
    // the Routine "demography" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _debriefing_key_resp_allKeys;
var debriefingComponents;
function debriefingRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'debriefing'-------
    t = 0;
    debriefingClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    debriefing_key_resp.keys = undefined;
    debriefing_key_resp.rt = undefined;
    _debriefing_key_resp_allKeys = [];
    // keep track of which components have finished
    debriefingComponents = [];
    debriefingComponents.push(debriefing_text);
    debriefingComponents.push(debriefing_key_resp);
    
    for (const thisComponent of debriefingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function debriefingRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'debriefing'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = debriefingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *debriefing_text* updates
    if (t >= 0.0 && debriefing_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debriefing_text.tStart = t;  // (not accounting for frame time here)
      debriefing_text.frameNStart = frameN;  // exact frame index
      
      debriefing_text.setAutoDraw(true);
    }

    
    // *debriefing_key_resp* updates
    if (t >= 0.0 && debriefing_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debriefing_key_resp.tStart = t;  // (not accounting for frame time here)
      debriefing_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debriefing_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debriefing_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debriefing_key_resp.clearEvents(); });
    }

    if (debriefing_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = debriefing_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _debriefing_key_resp_allKeys = _debriefing_key_resp_allKeys.concat(theseKeys);
      if (_debriefing_key_resp_allKeys.length > 0) {
        debriefing_key_resp.keys = _debriefing_key_resp_allKeys[_debriefing_key_resp_allKeys.length - 1].name;  // just the last key pressed
        debriefing_key_resp.rt = _debriefing_key_resp_allKeys[_debriefing_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of debriefingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function debriefingRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'debriefing'-------
    for (const thisComponent of debriefingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('debriefing_key_resp.keys', debriefing_key_resp.keys);
    if (typeof debriefing_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debriefing_key_resp.rt', debriefing_key_resp.rt);
        routineTimer.reset();
        }
    
    debriefing_key_resp.stop();
    // the Routine "debriefing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
