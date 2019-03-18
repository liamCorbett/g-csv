=====
g-csv
=====
Manages .csv files and uploads or pastes them to Google Sheets.

Usage
=====

Installation
------------

In a command window, enter: ``pip install gcsv``

Code
----

Use the following code example as a guide, replacing the following dummy strings with relevant information.

- ``my_csv_path``: the path to your CSV (e.g ``C:\reports\mycsv.csv``)
- ``my_spreadsheet_id``: the ID (or "key") of a spreadsheet; can be found in the spreadsheet URL after ``/d/`` but before ``/edit``
- ``my_worksheet_name``: the worksheet (or "tab") name of the paste destination
- ``start_row``: the starting row of the paste destination
- ``start_col``: the starting column of the paste destination

.. code-block:: python

    import gcsv

    csv = gcsv.GCSV(r'my_csv_path')

    csv.paste_to('my_spreadsheet_id',
                 'my_worksheet_name',
                 'start_row',
                 'start_col')