Installation
============

.. Stable release
.. --------------

.. To install dreaminsg-integrated-model, run this command in your terminal:

.. .. code-block:: console

..     $ pip install dreaminsg_integrated_model

.. This is the preferred method to install dreaminsg-integrated-model, as it will always install the most recent stable release.

.. If you don't have `pip`_ installed, this `Python installation guide`_ can guide
.. you through the process.

.. .. _pip: https://pip.pypa.io
.. .. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for dreaminsg-integrated-model can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/srijithabalakrishnan/dreaminsg_integrated_model


Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/srijithabalakrishnan/dreaminsg_integrated_model


You may need to create a new Python environment that has all required packages and dependencies installed before start using the package.
Run the following comment.

.. code-block:: console

    $ conda env create --name infrarisk --file=environment.yml

We have observed that in certain instances, a few package conflicts when installing the environment. If so, please install the packages manually.