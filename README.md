ase-template-russian
====================

This is a translation-building kit for the StateExplorer app templates. 
It requires a specially-structured CVS file, and builds an ".aset" file,
that you can install into the [StateExplorer app](http://www.ivarjacobson.com/Alpha_State_Explorer_App/).




Directory structure
===================

 - src/
    - Template/
       - Essential lifecycle/ —— a State Board template from the App
          - locale/
          - resources/
          - stateboard.json


build-translation.py (not working yet)
====================


Usage:

  $ python build-translation.py Path/To/Template Path/To/Translation.CSV Output/Path/




build-template.py (not working yet)
=================

Usage:

  $ python build-template.py Path/To/Translation
  


How to install a (new) template?
================================

Use iTunes to upload an something.aset file into the StateExplorer. Then 
restart the App. (You may have to force it by first closing the app.) 
It should recognize and install the template upon next launch.

