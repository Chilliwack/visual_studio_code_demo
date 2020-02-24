# Visual Studio Code for Data Science

A quick demonstration. Some really fantastic scientific programmers
wait a long-time before trying a modern IDE.
Here are some reasons to take a look at Visual Studio Code.

## Preliminaries

1. Install Visual Studio Code (https://code.visualstudio.com/)
2. Add the following four key extensions (Code Runner 0.9.16, Python, and R, markdownlint).
    * Do this by clicking on the four box icon on the left side bar.
    * Search for the extensions by name and install
3. Ensure you have a python >= 3.6e environment available.

## Shortcuts for Mac

* ⌘ is the Command () key.
* ⌃ is the Control key.
* ⌥ is the Option (alt) key.
* ⇧ is the Shift key.
* ⇪ is the Caps Lock key.

## 1. Keyboard Shortcuts Aren't just for Emacs

### Select Panes with ⌘1,⌘2, ... #n

If n is greater than the number of open panes, this will create a new pane.

### Select Tabs within Panes with ⌃1,⌃2, ... ⌃n

Get to the 2nd tab in the leftmost pane [⌘1], then [⌃2].

### Select Explorer Pane with ⌘0

Once you are in the explorer you can use up and down keys to select files.

### Reveal File Paths Instantly

Click on the file panel Use the keyboard shortcut [⌥⌘C], and bam!, the full path is copied to your clipboard (e.g., `/Users/kmayerbl/active/demo_vsc/README.md`)

### Reveal Paths with Clicks

Instantly get to where  your code lives on your machine. Save time by right-click on a folder or file, and select [Reveal in Finder] or [Open in Terminal]. Need the path just click [Copy Path].

### Save one or Save all by Group

Take a look at icon on the browser panel.

## 2. Preview your README.md

VSC offers a live rendering of your markdown. To view it, right-click on your markdown file and select [Open Preview].

## 3. Run Script or Only Part of Script With ⌃⌥N

You can run a segment of a script by selecting the part you care about and hitting [⌃⌥N]. The results show up in the OUTPUT table.

## 4. Problems and Quick Their Quick Fixes

Linters help you find probelms quickly. These are reported in the Problems tab of the  Here are two examples. 

* No-trailing-spaces (see one line above)
* No-bare URLs (see in the first block)

Get to the problems quickly with this shortcut [⇧⌘ M].

## 5. Debugging

When we run python hi.py we see an error. Suppose we want to see where that error emerges.

* Breakpoints fn + F9 , or using the mouse by clicking in the left margin in the editor.
* Click the Bug with the play icon
* More: https://code.visualstudio.com/docs/python/debugging

## 6. Work on a Specific Unit Test

A great thing about VSCode is how it organizes your test. You can even run them one by one.

![tests](https://user-images.githubusercontent.com/46639063/75184229-ea3d8580-56f8-11ea-83d3-1ee87fec849c.png)

## 7. Peak Function is Some Serious Magic Beans

 Sometimes you don't want to search for where a variable or function is defined. VSCode has a peak funciton that lets examine externally referenced objects, and even edit them, directly from where an object is referenced. Let's look at what the French hello should be:

![peak](https://user-images.githubusercontent.com/46639063/75184186-d98d0f80-56f8-11ea-8e67-cd76626992f0.png)


## 8. Look at a Merge Confict

Let's look at a resolving a merge conflict.

I think we should start local!
I think we should think global!

## 9. settings.json

JSON file with all your settings. How to get to it. (see the common settings wheel at the lower left)

## 10. the .code-workspace file

What the heck is this for?


## Conclusions:

I am sure there are a ton of other great stuff one can do with Visual Studio Code. 
Hopefully this tutorial has heightened your interest.
