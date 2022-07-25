
- Based off default PETG profile in Flash Print
- Height of 0.15mm in offset is to take into account the tape on the build platform

[Test your 3D printer! v3 by ctrlV](https://www.thingiverse.com/thing:1363023/files)

## Attempt #1

- Changes
  - 100% extrusion ratio
  - 0.2mm layer height
  - 0.3mm first layer
  - rather high z offset (~0.5mm in total)

## Attempt #2

- Changes
  - Reduced layer height to 0.1mm
  - First layer height of 0.28

## Attempt #3

- First layer height of 0.28mm (reduction of 0.02)
  - Based purely off other people’s profiles, no real reasoning behind it
- Adjusted the z-offset live, settled on about 0.15mm + 0.26mm = 0.41mm
  - This was the lowest offset I could use without colliding with existing filament resulting in build up around the nozzle

Under extruded at the beginning of each layer or after travel without extrusion

Over extruded at the end before retraction

Layer height seemed perfect

## Attempt #4

Attempting to address under extrusions at beginning, blob at end

[Under extrusion when starting outer wall](https://3dprinting.stackexchange.com/a/10710)

- Increase travel speed
- Increase retraction distance and speed
- Increase acceleration
- What is extra restart length
- Disable only retract when crossing outline

- Changes
  - Added extra retract length 0.1
  - Increased retract speed to 40mm/S (increase of 5mm/s)

- Outcomes
  - First layer/brim measured fairly close to correct height
  - No longer have gaps after travel (underextrusion at start)
  - Still seem to have blobs in some places

## Attempt 5 - Flow rate

Using the [[Flow Calibration Cube|3d-printing.calibration-tests#flow-calibration-cube]]

- Measurements:

  - 0.86 mm
  - 0.86 mm
  - 0.85 mm
  - 0.86 mm

- Ratio of expected wall thickness to actual wall thickness:
  - $0.80/((0.86 +0.86 + 0.85 + 0.86)/4) = 0.93$
- New flow rate = $0.93 \times 0.96 \approx 0.89$

The measured wall widths of the following print were:

- 0.74 mm
- 0.80 mm
- 0.77 mm
- 0.74 mm


## Investigating SuperSlicer

- [[3d-printing.slicer.super-slicer]]

References:

- [Has anybody successfully used Prusa Slicer with the FlashFor...](https://forum.prusaprinters.org/forum/prusaslicer/has-anybody-successfully-used-prusa-slicer-with-the-flashforge-adventurer-3/)
  - Python post processing script
  - Removing comments (verbose mode)
- Post processing script for Flash Forge Creator Pro [Using PrusaSlicer (Slic3r) with the FlashForge Creator Pro](https://www.dr-lex.be/software/ffcp-slic3r-profiles.html#using)
  - [FFCP-GCodeSnippets/make_fcp_x3g.pl at master · DrLex0/FFCP-GCodeSnippets](https://github.com/DrLex0/FFCP-GCodeSnippets/blob/master/make_fcp_x3g.pl)

Super Slicer profile sourced from:

- Adventurer 4 printer settings: [SUPERSLICER, SIMPLIFY3D, and CURA Setup For Adventurer 4](https://www.youtube.com/watch?v=QMkjMrHNxME)
- PETG Filament settings: [Tips And Tricks For The Perfect PETG Settings - Things No One Else Tells You!](https://www.youtube.com/watch?v=FTos-G1QXeE)

![](assets/images/2022-03-19-17-50-12.png)

![](/assets/images/2022-03-19-17-50-22.png)

![](/assets/images/2022-03-19-17-50-50.png)


Teaching tech filament profiles: [SuperSlicer/filament at main · teachingtechYT/SuperSlicer](https://github.com/teachingtechYT/SuperSlicer/tree/main/filament)
  - Also has printer profiles but none for flashforge

The gcode that super slicer produces isn't entirely compatible with the Adventurer 4:

- Temperature commands set the hotend index once but omit it afterwards
  - Regex for finding commands that don't end with a hotend index
  - `^M140 S\d+ +$`
  - Replacement for adding the hotend index: $0T0



[[3d-printing.config.live-z-offset]]: 0.44mm

Overview:

![](assets/images/2022-03-20-12-35-15.png)

Flaws:

![](assets/images/2022-03-20-12-36-12.png)

Good intralayer in some spots

![](assets/images/2022-03-20-12-42-33.png)

Bottom left, end of print:

![](assets/images/2022-03-20-12-42-12.png)

Centre:

![Centre](assets/images/2022-03-20-12-37-01.png)

Super Slicer, second last step...

![](assets/images/2022-03-20-12-40-56.png)


## Increasing Extrusion Width

- Increased the extrusion with from 111% to 125%

Observations

- Maybe slightly stronger but not markedly so
- Still brittle enough to break while flexing the print


## 2022.03.27

- Began using [[3d-printing.slicer.flashprint]] again instead of [[3d-printing.slicer.super-slicer]] after experiencing frequent poor bed adhesion.
- Also trialing use of gluestick for poor bed adhesion

Observations

- First layer sticks well. This could be attributed to:
  - Use of raft (which was enabled by default)
    - 4x the path width (1.6mm) and lower print speed (10m/s) for the bottom layer of the raft
    ![flash print settings](/assets/images/2022-03-27-13-00-56.png)
  -




## Useful videos

[Supercharge your PETG 3D prints with these tips](https://www.youtube.com/watch?v=T3Y0atseU9k)