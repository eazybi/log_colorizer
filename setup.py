# -*- coding: utf-8 -*-
"""
Setup for the eazyBI log file Lexer and style
"""
from setuptools import setup

__author__ = 'JVI/JVA'

setup(
    name='log file lexer',
    version='0.1.0',
    description=__doc__,
    author=__author__,
    packages=['log_lexer'],

    entry_points={
        'pygments.lexers': [
            'loglexer = log_lexer:LogLexer',
        ],
        'pygments.styles': [
            'logstyle = log_lexer:LogStyle'
        ]
    }
)
