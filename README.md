# Shortcuts_for_linux
Creating manual shortcuts for every keyboard button for any operating system . 

This program uses pyxhook library to hook our custom function OnKeyPress with every key being pressed .
It can be used for every operating system that supports python .

<h2>To enable these shortcuts with your every login then add following entires in .bash_profile file .</h2>

```
# .bash_profile

shortcuts(){
path_toscript/Shortcuts.py > /dev/null &
}

export -f shortcuts
shortcuts
```
