# Hotkeys

Highly customizable hotkeys.

## Usage:

### The hotkeys

+ Start the app.py script. 
+ To shut down the script, hit **shift + esc** 
+ To enter and escape debug mode, hit **shift + alt_l + d**. Debug mode will print out the current input.
+ To add a new hotkey, edit the hotkeys.json. Your own hotkeys should contain
1) **key**: the hotkey to press. Always try out the combination in debug mode before editing the hotkeys.json.
2) **extras**: to hold alongside with the hotkey. Extras are "alt_l", "alt_gr", "shift", "shift_r", "ctrl_r", "ctrl_l". Should be a json array even if empty. 
3) **action**: the action you want to perform when the hotkey is pressed. The actions should be a shell command. In the example below, the **test.py** script is called with a "hello_world" argument.
```json 
,{
    "key":"A",     
    "extras":["shift","ctrl_l"],    
    "action":"test.py hello_world"
}
```

**!Shortcomings**:
+ If you use any extras, please be aware, that for example, if you use shift+a, the key must be **A** and **not** *a*. Best practice is to always check in debug mode.

+ The num pad numbers range from <95> to <106>. Use the <> brackets too. Num pad ',' is <110>.

### Soundboard

I recommend using [VB audio cable](https://vb-audio.com/Cable/).  
If the audio is cracklying, [this](https://www.youtube.com/watch?v=Gb-PsrIVChY) tutorial worked for me. 

+ find_out_sound_device.py: prints out all the available sound devices. Default hotkey is shift + alt_l + b

+ play_wav.py: plays a wav file on the specified device. First argument is the wav file, second argument is the device index. To find out the device index, you can use the find_out_sound_device.py. Example for usage:
```json 
,{
    "key":"?",
    "extras":["shift","alt_l"],
    "action":"play_wav.py sound.wav 7"
}
```
### Config

+ You can configure the escape and the debug mode hotkeys exactly like you would any other hotkey, the only difference is that you have to edit the config.json and they don't have actions. The config.json should contain the "escape" and "debug" json objects.
```json
{
    "escape":{
        "key":"esc",
        "extras":["shift"]
    },
    "debug":{
        "key":"D",
        "extras":["shift","alt_l"]
    }
}
```