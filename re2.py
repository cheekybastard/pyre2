#!/usr/bin/env python

# Copyright (c) 2010, David Reiss and Facebook, Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Facebook nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import _re2

class Inst(object):
	kInstAlt 			= 0		# choose between out_ and out1_
	kInstAltMatch		= 1 	# Alt: out_ is [00-FF] and back, out1_ is match; or vice versa.
	kInstByteRange		= 2		# next (possible case-folded) byte must be in [lo_, hi_]
	kInstCapture		= 3		# capturing parenthesis number cap_
	kInstEmptyWidth		= 4		# empty-width special (^ $ ...); bit(s) set in empty_
	kInstMatch			= 5		# found a match!
	kInstNop			= 6		# no-op; occasionally unavoidable
	kInstFail			= 7		# never match; occasionally unavoidable

	kEmptyBeginLine        = 1<<0      # ^ - beginning of line
	kEmptyEndLine          = 1<<1      # $ - end of line
	kEmptyBeginText        = 1<<2      # \A - beginning of text
	kEmptyEndText          = 1<<3      # \z - end of text
	kEmptyWordBoundary     = 1<<4      # \b - word boundary
	kEmptyNonWordBoundary  = 1<<5      # \B - not \b
	kEmptyAllFlags         = (1<<6)-1

__all__ = [
    "error",
    "escape",
    "compile",
    "search",
    "match",
    "fullmatch",
	"Inst",
    ]

# Module-private compilation function, for future caching, other enhancements
_compile = _re2._compile

error = _re2.error
escape = _re2.escape

def compile(pattern):
    "Compile a regular expression pattern, returning a pattern object."
    return _compile(pattern)

def search(pattern, string):
    """Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found."""
    return _compile(pattern).search(string)

def match(pattern, string):
    """Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found."""
    return _compile(pattern).match(string)

def fullmatch(pattern, string):
    """Try to apply the pattern to the entire string, returning
    a match object, or None if no match was found."""
    return _compile(pattern).fullmatch(string)
