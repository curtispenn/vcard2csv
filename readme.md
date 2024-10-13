# How to Use the vCard to CSV Script

## Prerequisites
- Ensure you have a folder on your Desktop containing the `.vcf` files you want to convert.

## Steps to Use the Script

1. **Open Terminal**
   - Find and open the **Terminal** application. You can find it in `Applications > Utilities`.

2. **Navigate to Your vCard Folder**
   - In the Terminal, type the following command to go to your vCard folder (replace `vCardFiles` with your actual folder name if different):
     ```bash
     cd ~/Desktop/vCardFiles
     ```
   - Press **Enter**.

3. **Run the Script**
   - To convert your vCard files to a CSV file, type the following command:
     ```bash
     python3 ~/Desktop/vcard2csv.py . output.csv
     ```
   - Here, `output.csv` is the name of the resulting CSV file. You can change this name if you prefer.

4. **Check the Output**
   - After the script finishes running, look in the `vCardFiles` folder for the `output.csv` file. You can open this file with any spreadsheet application (like Excel or Google Sheets) to view your contacts.

## Troubleshooting
- If you encounter any errors:
  - Make sure you’re in the correct folder.
  - Check that your vCard files have the `.vcf` extension.
  - Look for any error messages in the Terminal for guidance.

## Notes
- The script will only extract certain fields: Name, Cell phone, Work phone, Home phone, Email, and Note.

.. -*- coding: utf-8 -*-

============
vCard to CSV
============

:author: Nathaniel Beaver

This is a Python 2/3 script to turn a directory full of vCard files
into a single CSV file.
It can also be imported and used as a module.

Not all of the vCard fields are preserved; currently only these fields:

- Name
- Cell phone
- Work phone
- Home phone
- Email
- Note

(I used this to convert vCards from an old LG Rumor 2 cell phone,
so I have not needed to extract additional fields.)

------------
Dependencies
------------

If you encounter an error like this (Python 2)::

    Traceback (most recent call last):
      File "vcard2csv.py", line 2, in <module>
        import vobject # to parse vCard (vcf) files
    ImportError: No module named vobject

or this (Python 3)::

    Traceback (most recent call last):
      File "vcard2csv.py", line 2, in <module>
        import vobject
    ModuleNotFoundError: No module named 'vobject'


then you need to install the python `vobject`_ library,
which you can do with pip::

    pip install --user vobject

.. _vobject: http://vobject.skyhouseconsulting.com/

It is also in the major package managers.

https://src.fedoraproject.org/rpms/python-vobject

https://launchpad.net/ubuntu/+source/python-vobject

https://tracker.debian.org/pkg/python-vobject

https://security.archlinux.org/package/python-vobject

https://software.opensuse.org/package/python-vobject

https://software.opensuse.org/package/python2-vobject

https://software.opensuse.org/package/python3-vobject

-----
Usage
-----

The vCard files must have the suffix ``.vcf``.
Simply run the script in the directory containing the vCard files
and specify the output filename::

    python vcard2csv.py . foo.csv

Or point the script at a directory containing the ``.vcf`` files::

    python vcard2csv.py example-vcards foo.csv

For additional help and options, pass the ``-h`` flag::

    python vcard2csv.py -h

The script is compatible with both Python 2 and Python 3.

----
Bugs
----

Only a few of the vCard fields are preserved;
this may be undesirable.

vCard version 4.0 has not been implemented,
though it would probably be straightforward to do so.

See the `to-do list`_ for more.

.. _to-do list: todo.md

-------
License
-------

This project is licensed under the terms of the `MIT license`_.

.. _MIT license: LICENSE.txt
