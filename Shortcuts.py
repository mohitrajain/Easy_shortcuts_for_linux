#!/usr/bin/python
import pyxhook
import time

import subprocess
import re

# create .mylogs directory first to maintain logs
logfile = '/home/username/.mylogs/shortcuts.log'

def logger(log):
    print 'a'
    with open(logfile, 'r') as file:
        file.write(time.asctime() + ' :  ' + log + '\n')

def execute_out(cmd):
    Command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    (out, err) = Command.communicate()
    if err:
        logger('Error Executing ' + cmd + ' \n' + err)
    return out

def execute(cmd):
    Command=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)

out = execute_out('ps aux | grep shortcuts.py').split('\n')
no = 0
lineno = []

for line in out:
    if re.findall(r'python.*shortcuts.py',line):
        no +=1
        lineno.append(out.index(line))
        if no == 2:
            execute('kill -9 ' + out[lineno[0]].split()[1])
            logger('Restarting')
            break

logger('Started listening')

start = 0

def OnKeyPress(event):

  global start

  # volume and play control
  if re.findall(r'(2690250[\d]*)',event.Key):
      volumebrightControl(event)

  if event.Key == 'Alt_L':
      start = 2

  # Lxde file manager
  if event.Ascii == 111 and start == 1:
      #print 'O Pressed '
      execute('nohup /usr/bin/pcmanfm >/dev/null &')
      start = 0
      logger('terminal Started')

  # FireFox
  if event.Ascii == 102 and start == 1:
      #print 'F Pressed '
      execute('nohup path_to_firefox >/dev/null &')
      start = 0

  # Google Chrome
  if event.Ascii == 103 and start == 1:
      #print 'G Pressed '
      execute('nohup /usr/bin/google-chrome >/dev/null &')
      start = 0

  # Virtual Box
  if event.Ascii == 118 and start == 1:
      #print 'V Pressed '
      execute('nohup /usr/bin/VirtualBox >/dev/null &')
      start = 0

  # Audacious
  if event.Ascii == 97 and start == 1:
      #print 'A Pressed '
      execute('nohup /usr/bin/audacious >/dev/null &')
      start = 0

  # Restart itself
  if event.Ascii == 114 and start == 1:
      #print 'R Pressed '
      execute('nohup path_to_script/Shortcuts.py >/dev/null &')
      start = 0

  # sublime
  if event.Ascii == 115 and start == 1:
      # print 's Pressed '
      execute('nohup  path_to_sublime_text >/dev/null &')
      start = 0

  # lock
  if event.Ascii == 108 and start == 1:
      # print 'l Pressed '
      execute('nohup  /usr/bin/i3lock >/dev/null &')
      start = 0

  else:
      start = start - 1

def volumebrightControl(event):

    global start
    start = 0

    if event.Key == '[269025042]':
        execute('amixer -q sset Master toggle')

    elif event.Key == '[269025041]':
        execute('amixer -q sset Master 10%-')

    elif event.Key == '[269025043]':
        execute('amixer -q sset Master 10%+')

    elif event.Key == '[269025046]':
        execute('pgrep audacious && /usr/bin/audacious -r')

    elif event.Key == '[269025044]':
        execute('pgrep audacious && /usr/bin/audacious -t')

    elif event.Key == '[269025047]':
        execute('pgrep audacious && /usr/bin/audacious -f')

    elif event.Key == '[269025027]':
        execute('xbacklight -dec 20')

    elif event.Key == '[269025026]':
        execute('xbacklight -inc 20')

new_hook=pyxhook.HookManager()

new_hook.KeyDown=OnKeyPress

new_hook.HookKeyboard()

new_hook.start()
