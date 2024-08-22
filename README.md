# CLIPYLOAD
**CLIPY** - The non-blocking python command line loader!


**Key Features**:
- CLIPY uses built in python modules
- Simple/straightforward usage
- Fast implementation


Thanks to [**sindresorhus**](https://github.com/sindresorhus) for providing loads of [**spinners**](https://github.com/sindresorhus/cli-spinners/blob/main/spinners.json) !


# Installation
```bash
git clone https://github.com/era-net/clipyload.git
```


# Usage
There is just one main function called **`load`**() as shown in the [basic example](#basic). For more details see [The load() function](#the-load-function).


## Basic
```python
import clipyload as clipy
import time

def task():
    # simulating some work ...
    for _ in range(5):
        time.sleep(.8)

clipy.load(target=task, desc='working ...')
```

Output:
```
⣷ working ...
```


## Change the spinner
```python
clipy.load(task, desc='working ...', index='moon')
```

Output:
```
🌘  working ...
```

Choose a [different spinner](#spinners)!


## Move the spinner to the back
```python
clipy.load(task, desc='working', pos='end')
```

Output:
```
working ⣷
```

Keep on reading to see all the available parameters for the **`load`**() function.


# The load() function
**Parameters**:

**`target`**, <u>*function*</u> required

&emsp;Callback to a existing function.

**`desc`**, <u>*string*</u> default: empty string ""

&emsp;Description of the loading process.

**`pos`**, <u>*string*</u> default: "start"

&emsp;Where to put the spinner. Either "start" or "end".

**`index`**, <u>*string*</u> default: "dots2"

&emsp;Index of the desired [spinner](#spinners).

**`args`**, <u>*tuple*</u> default: ()

&emsp;To pass arguments to the callback (target) function.


# Spinners
```
index: "dots"                 ['⠋', '⠙', '⠹' ...]


index: "dots2"                ['⣾', '⣽', '⣻' ...]


index: "dots3"                ['⠋', '⠙', '⠚' ...]


index: "dots4"                ['⠄', '⠆', '⠇' ...]


index: "dots5"                ['⠋', '⠙', '⠚' ...]


index: "dots6"                ['⠁', '⠉', '⠙' ...]


index: "dots7"                ['⠈', '⠉', '⠋' ...]


index: "dots8"                ['⠁', '⠁', '⠉' ...]


index: "dots9"                ['⢹', '⢺', '⢼' ...]


index: "dots10"               ['⢄', '⢂', '⢁' ...]


index: "dots11"               ['⠁', '⠂', '⠄' ...]


index: "dots12"               ['⢀⠀', '⡀⠀', '⠄⠀' ...]


index: "dots13"               ['⣼', '⣹', '⢻' ...]


index: "dots14"               ['⠉⠉', '⠈⠙', '⠀⠹' ...]


index: "dots8Bit"             ['⠀', '⠁', '⠂' ...]


index: "sand"                 ['⠁', '⠂', '⠄' ...]


index: "line"                 ['-', '\\', '|', '/']


index: "line2"                ['⠂', '-', '–' ...]


index: "pipe"                 ['┤', '┘', '┴' ...]


index: "simpleDots"           ['.  ', '.. ', '...', '   ']


index: "simpleDotsScrolling"  ['.  ', '.. ', '...' ...]


index: "star"                 ['✶', '✸', '✹' ...]


index: "star2"                ['+', 'x', '*']


index: "flip"                 ['_', '_', '_' ...]


index: "hamburger"            ['☱', '☲', '☴']


index: "growVertical"         ['▁', '▃', '▄' ...]


index: "growHorizontal"       ['▏', '▎', '▍' ...]


index: "balloon"              [' ', '.', 'o' ...]


index: "balloon2"             ['.', 'o', 'O' ...]


index: "noise"                ['▓', '▒', '░']


index: "bounce"               ['⠁', '⠂', '⠄', '⠂']


index: "boxBounce"            ['▖', '▘', '▝', '▗']


index: "boxBounce2"           ['▌', '▀', '▐', '▄']


index: "triangle"             ['◢', '◣', '◤', '◥']


index: "binary"               ['010010', '001100', '100101' ...]


index: "arc"                  ['◜', '◠', '◝' ...]


index: "circle"               ['◡', '⊙', '◠']


index: "squareCorners"        ['◰', '◳', '◲', '◱']


index: "circleQuarters"       ['◴', '◷', '◶', '◵']


index: "circleHalves"         ['◐', '◓', '◑', '◒']


index: "squish"               ['╫', '╪']


index: "toggle"               ['⊶', '⊷']


index: "toggle2"              ['▫', '▪']


index: "toggle3"              ['□', '■']


index: "toggle4"              ['■', '□', '▪', '▫']


index: "toggle5"              ['▮', '▯']


index: "toggle6"              ['ဝ', '၀']


index: "toggle7"              ['⦾', '⦿']


index: "toggle8"              ['◍', '◌']


index: "toggle9"              ['◉', '◎']


index: "toggle10"             ['㊂', '㊀', '㊁']


index: "toggle11"             ['⧇', '⧆']


index: "toggle12"             ['☗', '☖']


index: "toggle13"             ['=', '*', '-']


index: "arrow"                ['←', '↖', '↑' ...]


index: "arrow2"               ['⬆️ ', '↗️ ', '➡️ ' ...]


index: "arrow3"               ['▹▹▹▹▹', '▸▹▹▹▹', '▹▸▹▹▹' ...]


index: "bouncingBar"          ['[    ', '[=   ', '[==  ' ...]


index: "bouncingBall"         ['( ●    )', '(  ●   )', '(   ●  )' ...]


index: "smiley"               ['😄 ', '😝 ']


index: "monkey"               ['🙈 ', '🙈 ', '🙉 ', '🙊 ']


index: "hearts"               ['💛 ', '💙 ', '💜 ' ...]


index: "clock"                ['🕛 ', '🕐 ', '🕑 ' ...]


index: "earth"                ['🌍 ', '🌎 ', '🌏 ']


index: "material"             ['█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁', '██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁', '███▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁' ...]


index: "moon"                 ['🌑 ', '🌒 ', '🌓 ' ...]


index: "runner"               ['🚶 ', '🏃 ']


index: "pong"                 ['▐⠂       ▌', '▐⠈       ▌', '▐ ⠂      ▌' ...]


index: "shark"                ['▐|\\____________▌', '▐_|\\___________▌', '▐__|\\__________▌' ...]


index: "dqpb"                 ['d', 'q', 'p', 'b']


index: "weather"              ['☀️ ', '☀️ ', '☀️ ' ...]


index: "christmas"            ['🌲', '🎄']


index: "grenade"              ['،  ', '′  ', ' ´ ' ...]


index: "point"                ['∙∙∙', '●∙∙', '∙●∙' ...]


index: "layer"                ['-', '=', '≡']


index: "betaWave"             ['ρββββββ', 'βρβββββ', 'ββρββββ' ...]


index: "fingerDance"          ['🤘 ', '🤟 ', '🖖 ' ...]


index: "fistBump"             ['🤜\u3000\u3000\u3000\u3000🤛 ', '🤜\u3000\u3000\u3000\u3000🤛 ', '🤜\u3000\u3000\u3000\u3000🤛 ' ...]


index: "soccerHeader"         [' 🧑⚽️       🧑 ', '🧑  ⚽️      🧑 ', '🧑   ⚽️     🧑 ' ...]


index: "mindblown"            ['😐 ', '😐 ', '😮 ' ...]


index: "speaker"              ['🔈 ', '🔉 ', '🔊 ', '🔉 ']


index: "orangePulse"          ['🔸 ', '🔶 ', '🟠 ' ...]


index: "bluePulse"            ['🔹 ', '🔷 ', '🔵 ' ...]


index: "orangeBluePulse"      ['🔸 ', '🔶 ', '🟠 ' ...]


index: "timeTravel"           ['🕛 ', '🕚 ', '🕙 ' ...]


index: "aesthetic"            ['▰▱▱▱▱▱▱', '▰▰▱▱▱▱▱', '▰▰▰▱▱▱▱' ...]


index: "dwarfFortress"        [' ██████£££  ', '☺██████£££  ', '☺██████£££  ' ...]
```