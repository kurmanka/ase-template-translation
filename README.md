ase-template-russian
====================

This is a translation-building kit for the StateExplorer app templates. 
It requires a specially-structured CVS file, and builds an ".aset" file,
that you can install into the [StateExplorer app](http://www.ivarjacobson.com/Alpha_State_Explorer_App/).




Directory structure
===================

 - src/
    - Template/
       - Essential lifecycle/ — an original State Board template from the App
          - locale/
          - resources/
          - stateboard.json
 - EssenceAlphaStateTranslation.csv — a translation CSV template, with a Russian translation inside of it
 - build-translation.py — a script to produce a translated template


build-translation.py
====================

Usage:

  $ python build-translation.py Path/To/Template Path/To/Translation.CSV Output/Path

Output/Path directory must not exist. It will be created, by copying the source 
template there first, then creating needed xml file(s) in the locale/ dir inside.



build-template.py (not working yet)
=================

Builds an .aset file from a translated template dir.

Usage:

  $ python build-template.py Path/To/Translation
  
  


How to install a (new) template into the app?
================================

Use iTunes to upload a Something.aset file into the StateExplorer. Then 
restart the App. (You may have to force it by first closing the app.) 
It should recognize and install the template upon next launch.

