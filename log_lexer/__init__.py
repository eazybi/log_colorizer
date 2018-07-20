#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import \
     Text, Comment, Literal, Operator, Keyword, Name, String, Error, Other

class LogLexer(RegexLexer):
    """
    For eazyBI log files.
    """
    name = 'Log'
    filenames = ['eazybi-*.log.*']
    aliases = ['loglexer','log']

    tokens = {
        'string': [
            (r'(\s|.)', String),
          ],
        'log_date': [
            # (r'^\d\d\d\d-\d\d-\d\d', Comment),
            include('log_time'),
            (r'^\d\d\d\d-\d\d-\d\d', Literal.Date),
        ],
        'log_time': [
            (r'\d\d:\d\d:\d\d', String),
            (r'\+\d\d\d\d', Comment),
            include('severity'),
        ],
        'severity': [
            (r'INFO', Name.Constant),
            (r'ERROR|FATAL', Error),
            include('session'),
        ],
        'session': [
            (r'\[', Comment, "inside_bracket"),
            # (r':', Comment, "inside_bracket"),
            # (r'\[\w*', Name.Attribute),
        ],
        'inside_bracket': [
          (r'\w\w\w\w\w\w\w\w', Name.Attribute),
          (r':', Comment),
          (r'\]', Comment, "#pop"),
        ],
        'request_start': [
          (r'(Started )', Text, "start_details")
        ],
        'start_details': [
          (r'GET |POST ', Keyword.Pseudo, "request_url"),
          (r'.*\n', Text, "#pop"),
        ],
        'request_url': [
          (r'".*"', Keyword.Pseudo, "#pop"),
        ],
        'request_end': [
          (r'(Completed )', Text, "request_details")
        ],
        'request_details': [
          (r'(2|3)\d\d.*in', Name.Attribute, "#pop")
        ],
        'other': [
          (r'(Rendered|Parameters|Processing|Filter|Redirected).*\n', Other),
        ],

        'root': [
            (r'\n', Text),
            include('log_date'),
            include("request_start"),
            include("request_end"),
            include("other"),
            (r'(\s|.)', Text),
        ]
    }
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal
class LogStyle(Style):
    """
    This style mimics the Monokai color scheme.
    """
    default_style = '#0f0'
    background_color = "#272822"
    highlight_color = "#49483e"
    styles = {
        # No corresponding class for the following:
        Text:                      "#f8f8f2", # class:  ''
        Whitespace:                "",        # class: 'w'
        Error:                     "#fff bg:#960050", # class: 'err'
        # Error:                     "#960050 bg:#1e0010", # class: 'err'
        Other:                     "",        # class 'x'
        Comment:                   "#75715e", # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "#aa7dfc",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'
        Keyword:                   "#66d9ef", # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "#f92672", # class: 'kn'
        Keyword.Pseudo:            "#fd971f",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "",        # class: 'kt'
        Operator:                  "#f92672", # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords
        Punctuation:               "#f8f8f2", # class: 'p'
        Name:                      "#f8f8f2", # class: 'n'
        Name.Attribute:            "#a6e22e", # class: 'na' - to be revised
        Name.Builtin:              "",        # class: 'nb'
        Name.Builtin.Pseudo:       "",        # class: 'bp'
        Name.Class:                "#a6e22e", # class: 'nc' - to be revised
        Name.Constant:             "#66d9ef", # class: 'no' - to be revised
        Name.Decorator:            "#a6e22e", # class: 'nd' - to be revised
        Name.Entity:               "",        # class: 'ni'
        Name.Exception:            "#a6e22e", # class: 'ne'
        Name.Function:             "#a6e22e", # class: 'nf'
        Name.Property:             "",        # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "",        # class: 'nn' - to be revised
        Name.Other:                "#a6e22e", # class: 'nx'
        Name.Tag:                  "#f92672", # class: 'nt' - like a keyword
        Name.Variable:             "",        # class: 'nv' - to be revised
        Name.Variable.Class:       "",        # class: 'vc' - to be revised
        Name.Variable.Global:      "",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "",        # class: 'vi' - to be revised
        Number:                    "#ae81ff", # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'
        Literal:                   "#ae81ff", # class: 'l'
        Literal.Date:              "#fd971f", # class: 'ld'
        String:                    "#e6db74", # class: 's'
        # String:                    "bg:#ansired #e6db74", # class: 's'
        String.Backtick:           "",        # class: 'sb'
        String.Char:               "",        # class: 'sc'
        String.Doc:                "",        # class: 'sd' - like a comment
        String.Double:             "",        # class: 's2'
        String.Escape:             "#ae81ff", # class: 'se'
        String.Heredoc:            "",        # class: 'sh'
        String.Interpol:           "",        # class: 'si'
        String.Other:              "",        # class: 'sx'
        String.Regex:              "",        # class: 'sr'
        String.Single:             "",        # class: 's1'
        String.Symbol:             "",        # class: 'ss'
        Generic:                   "",        # class: 'g'
        Generic.Deleted:           "",        # class: 'gd',
        Generic.Emph:              "italic",  # class: 'ge'
        Generic.Error:             "",        # class: 'gr'
        Generic.Heading:           "",        # class: 'gh'
        Generic.Inserted:          "",        # class: 'gi'
        Generic.Output:            "",        # class: 'go'
        Generic.Prompt:            "",        # class: 'gp'
        Generic.Strong:            "bold",    # class: 'gs'
        Generic.Subheading:        "",        # class: 'gu'
        Generic.Traceback:         "",        # class: 'gt'
    }
