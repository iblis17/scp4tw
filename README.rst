scp4tw
===============================================================================

Simple `scp-wik-.cn <http://scp-wiki-cn.wikidot.com>`_ browser with bolt-on
OpenCC.


Dev Setup
----------------------------------------------------------------------

Install `OpenCC <https://github.com/BYVoid/OpenCC>`_ first.

::

    pip install -r requirements.txt
    cd scp4tw
    ./manager.py runserver

::

    cd scp4tw/static
    npm install

::

    npm install -g webpack
    npm run dev
