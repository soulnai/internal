Python Introduction Course
==========================

Document describes lectures feedback and additional materials.


Course is based on [The Hitchhiker’s Guide to Python!](https://python-guide.readthedocs.org/en/latest/)

# Project structure

- Practical lesson about the tools used to manage project life-cycle.
    - show common python structure and files that may reside there
    [Project template example](https://github.com/signalpillar/bootstrapy)

    - install Python
    - install Git
        [Example of git configuration](https://github.com/signalpillar/dotfiles/blob/master/.gitconfig)
    - configure pip, virtualenv
    - run first test

- General recommendations
    - more experiance in shell (bash, zsh) - manage project in the shell.
      Use Git shell for that on Windows
    - start with editor. Editor with auto-completion, PEP-8 + all kind of nifty things.
      Recommend to start with Sublime Text
    - More practice with Git
        - [git - the simple guide](https://rogerdudler.github.io/git-guide/)
        - [Git makes more sense when you understand X](http://think-like-a-git.net/sections/git-makes-more-sense-when-you-understand-x.html)
        - [Interactive Git tutorial](https://try.github.io/levels/1/challenges/1)

# Intro
- The Zen of Python, by [Tim Peters](http://c2.com/cgi/wiki?TimPeters)

```
In [1]: import this

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

- [PEP](http://legacy.python.org/dev/peps/)


## What Python runtime I should use?
Python 2.7/3.x ? - `It depends`

Some modules are written solely for 2.x or 3.x
Some modules support only 32bit or 64bit architecture

## Conventions

- [PEP-8](http://legacy.python.org/dev/peps/pep-0008/)
- [Docstrings](http://legacy.python.org/dev/peps/pep-0257/)
- [Good reading](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)
- [Google](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
- [Twitter](https://github.com/twitter/commons/blob/master/src/python/twitter/common/styleguide.md)

## Installation

apt-get/yum/brew

## Documentation

- [sphinx](http://sphinx-doc.org) (.md & .rst)
- [Rest viewer](https://mg.pov.lt/restview/) (restview)

## Environment

- GNU/Linux/OS X
- virtualenv ([virtualenv-wrapper](http://virtualenvwrapper.readthedocs.org/en/latest/))

### IDE vs Editor

- PyCharm
- Emacs/Vim/Sublime Text/Atom (PEP8 configured, pyflakes)

### Distribution
- Distribution question: Lib or App ?

- setup.py (distribution)
- pypi (https://pypi.python.org/pypi)
- pip/setup.py (package manager) (requirements.txt)

### Testing

Runner vs framework

- unittest
- nose
- pytest +++

## Resources/Documentation

- To start with:
    - [Dive In Python](http://www.diveintopython.net)
    - [Official Python Documentation](https://docs.python.org/2.7/)
    - [Learning Python for QA automation tasks](https://gist.github.com/diyan/5763644)
    - [Very nice Python+Selenium Guide](http://selenium-python.readthedocs.org/en/latest/installation.html)

## FAQ

* Where I can find different Python libraries?
  [PyPi](https://pypi.python.org/pypi)
