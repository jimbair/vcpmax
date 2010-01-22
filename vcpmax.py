#!/usr/bin/python
# Quick script to help me with VMWare VCP Training.
# Config built by hand from answers here:
# http://www.vmware.com/pdf/vsphere4/r40/vsp_40_config_max.pdf

config = 'config.txt'
raw = file(config, 'r')
lines = raw.read()
raw.close()

# split into sections
sections = lines.split('\n\n')

for section in sections:
    lines = section.split('\n')
    for line in lines:
        # Skip our headers
        if line.startswith('==='):
           continue 
        if line == '\n' or line == '':
            continue
        try:
            question, answer = line.split('___')
        except:
            print 'Skipping this bad line:'
            print line
            continue
        ourAnswer = raw_input("%s: " % (question,))
        ourAnswer = str(ourAnswer)
        if ourAnswer != answer:
            print "The correct answer is %s" % (answer)
        else:
            print "Correct!"
