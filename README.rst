scp4tw
===============================================================================

Simple `scp-wik-.cn <http://scp-wiki-cn.wikidot.com>`_ browser with bolt-on
OpenCC.


Dev Setup
----------------------------------------------------------------------

Install `OpenCC <https://github.com/BYVoid/OpenCC>`_ first.

Install python requirements::

    pip install -r requirements.txt

Install ui requirements::

    cd scp4tw/static
    npm install

and compile `build.js`::

    npm install -g webpack
    npm run dev

Then, run the development server::

    cd scp4tw
    ./manager.py runserver
