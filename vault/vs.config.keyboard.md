---
id: 11d5c065-7f38-4e70-a97c-c79e9fb9f05e
title: Keyboard
desc: ''
updated: 1617685751029
created: 1617685505367
---

[Scrolling through Visual Studio Intellisense list without mouse or keyboard arrows](https://stackoverflow.com/questions/18153541/scrolling-through-visual-studio-intellisense-list-without-mouse-or-keyboard-arro)

![](/assets/images/2021-04-06-15-05-10.png)

![](/assets/images/2021-04-06-15-06-36.png)

I have remapped CTRL+P to Edit.LineUp and CTRL+N to Edit.LineDown and this works in the Intellisense dropdown. For some reason the Intellisense dropdown dims out when pressing CTRL so it gets kind of hard to see the content in the dropdown. It's not a big problem though, since you can always release CTRL and it will light up again. I mostly use this method when I don't know the name of the method and want to browse for it.

If I know the name or part of the name it is often quicker to just type some of the letters in the method name. If I know for example that the name of the method I want is GetHashCode then I would just type "geh" or "has" or similar since that would be matched by intellisense.

Share
Improve this answer
Follow
edited Jul 27 '20 at 11:59

fat
4,96833 gold badges3737 silver badges6262 bronze badges
answered Sep 11 '13 at 14:50

Doktorn
67755 silver badges77 bronze badges
4
The dimming is a usability feature they added sometime around VS 2010. Intellisense would have a nasty habit of obscuring exactly the code you wanted to look at, which meant you had to close intellisense, read the code, and then reopen intellisense. Now, with a simple Ctrl press, it turns transparant so you can quickly read your code and let go of the key again, without leaving intellisense. – Bas Sep 11 '13 at 15:02
11
Hallelujah!! I didn't think anyone was going to solve this! Following your tip, I chose to use Alt+J and Alt+K which is closer to the J/K keys I use in Vim for up/down. Also, the Alt key doesn't dim the Intellisense window like Ctrl does. But the key thing here is that you identified the Edit.LineUp and Edit.LineDown commands as the source of the solution. So excited...thank you! – RSW Sep 11 '13 at 16:15
5
You can also setup Edit.CharLeft and Edit.CharRight to fully get rid of arrows keys. (I guess you already know this, but still...) – Alejandro Miralles Dec 20 '13 at 17:07
1
Edit.LineUp and Edit.LineDown are gone in VSCode 1.4.2; they should be selectPrevSuggestion and selectNextSuggestion – UnderBlue592 Feb 9 '20 at 3:08
