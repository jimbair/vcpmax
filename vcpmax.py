#!/usr/bin/python
# Quick script to help me with VMWare VCP Training.
# Config built by hand from answers here:
# http://www.vmware.com/pdf/vsphere4/r40/vsp_40_config_max.pdf
#
# Copyright (C) 2010  James Bair <james.d.bair@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

config = 'config.txt'
raw = file(config, 'r')
lines = raw.read()
raw.close()

# split into sections
sections = lines.split('\n\n')

# Work each section by line.
# This is in case we want to handle sections
# in the future in some fancy way.
for section in sections:
    lines = section.split('\n')
    for line in lines:
        # Skip our headers
        if line.startswith('===') and line.endswith('==='):
           print '\nNow working on %s\n' % (line.strip('='),)
           continue 
        # Skip any blank lines we inhereit
        if line == '\n' or line == '':
            continue
        try:
            question, answer = line.split('___')
        except:
            print 'Skipping this bad line:'
            print line
            continue
        ourAnswer = raw_input("%s: " % (question,))
        if ourAnswer != answer:
            print "The correct answer is %s" % (answer)
        else:
            print "Correct!"

print '\nAll done!'
