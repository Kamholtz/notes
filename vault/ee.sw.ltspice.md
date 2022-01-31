---
id: 837f426d-08b5-4d99-ad3a-236e255e94b8
title: Ltspice
desc: ''
updated: 1623109107480
created: 1623108808130
---

## How to include an external subckt

### Including the subckt directly as a directive

[ZENER DIODES IN LTSPICE - Page 1](https://www.eevblog.com/forum/beginners/zener-diodes-in-ltspice/)

- See posts by "Jay_Diddy_B"

Note that the following passage taken from the above link is actually modified
to indicate the correct way to change the prefix as shown in bold

> The Diodes Inc model was included in a large file with all their Zener diodes. I cut out the one that was needed and pasted it into a SPICE directive.
>
> I drew the schematic in LTspice the normal way and included any zener diode from the library of parts. You do this to get the right symbol.
>
> A diode can be defined as an intrinsic diode which has the SPICE prefix D. In
> the case the diode was defined by a .SUBCIRCUIT statement, so the SPICE prefix
> has to be changed from 'D' to 'X'. *Ctrl + Right click* on the diode and change
> the Prefix to X. Change Value to match the name of the subcircuit.


** Including the library file
Create a directive that contains a ".lib" refernce to the file containing the
subckt.

e.g.

```bash
.lib "C:\Users\Carl\Google Drive\electronics\extra_models\zener.lib"
```


Where the file it references contains text similar to the following:

[[file:resources/personal/electronics/ltspice/example.lib][Example .lib file]]

```
=========================================================================================================

[BZX84C3V3]
,*SRC=BZX84C3V3;DI_BZX84C3V3;Diodes;Zener <=10V; 3.30V  0.350W   Diodes Inc.
,*SYM=HZEN
.SUBCKT DI_BZX84C3V3  1 2
,*        Terminals    A   K
D1 1 2 DF
DZ 3 1 DR
VZ 2 3 0.799
.MODEL DF D ( IS=43.7p RS=35.2 N=1.10
+ CJO=127p VJ=0.750 M=0.330 TT=50.1n )
.MODEL DR D ( IS=8.74f RS=79.5 N=3.00 )
.ENDS

=========================================================================================================

[BZX84C3V6]
,*SRC=BZX84C3V6;DI_BZX84C3V6;Diodes;Zener <=10V; 3.60V  0.350W   Diodes Inc.
,*SYM=HZEN
.SUBCKT DI_BZX84C3V6  1 2
,*        Terminals    A   K
D1 1 2 DF
DZ 3 1 DR
VZ 2 3 1.12
.MODEL DF D ( IS=40.1p RS=34.9 N=1.10
+ CJO=112p VJ=0.750 M=0.330 TT=50.1n )
.MODEL DR D ( IS=8.01f RS=74.5 N=3.00 )
.ENDS

=========================================================================================================
```

As described in the above section "Including the subckt directly as a
directive", a subckt can be referenced by changing the prefix of the symbol to
'X' and changing the value to the name of the subckt itself
