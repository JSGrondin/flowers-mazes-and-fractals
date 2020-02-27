#!/usr/bin/env python3
# coding: utf-8

# loading packages
import json
import sys

if __name__ == "__main__":

    params = sys.argv[1]
    n = sys.argv[2]


    # open output text file
    workfile = open('./output', 'w')

    # open json file
    json_file = open(params, 'r')
    data = json.load(json_file)

    # open preambule text file and copy all lines till begin
    pre = open('./preambule', 'r')
    lines = pre.readlines()
    for line in lines:
        workfile.write(line)
    workfile.write('\n')
    pre.close()

    # writing default parameters
    workfile.write(f'/L:d {data["parameters"]["step"]} def % deplacement par defaut\n')
    workfile.write(f'/L:a {data["parameters"]["angle"]} def % angle par defaut\n')
    workfile.write('\n')
    workfile.write('\n')

    # function to convert step to eps string
    dict_vocab = {'F': 'dup F', '[': 'gsave', '+': 'L:a T:turn', ']':'grestore', '-':'L:a neg T:turn'}

    # writing each rules
    for key, f in enumerate(data['rules']['F']):
        workfile.write(f'/F{key+1}\n')
        workfile.write('\n')
        workfile.write('{\n')
        for key, step in enumerate(f):
            if step == 'F' and ('F' not in f[(key+1):]):
                workfile.write('\t' + step +'\n')
            else:
                workfile.write('\t' + dict_vocab[step] + '\n')

        workfile.write('} def\n')
        workfile.write('\n')

    # writing recursion
    workfile.write('/F\n')
    workfile.write('{\n')
    workfile.write('\tdup\n')
    workfile.write('\t0 eq\n')
    workfile.write('\t{\n')
    workfile.write('\t\tL:d T:draw\n')
    workfile.write('\t\tpop\n')
    workfile.write('\t}\n')
    workfile.write('\t{\n')
    workfile.write('\t\t1 sub\n')

    no_rules = len(data['rules']['F'])
    concatenated = '['
    for i in range(no_rules):
        if (i+1) < no_rules:
            concatenated = concatenated + f'/F{i+1} ' #with space
        else:
            concatenated = concatenated + f'/F{i+1}' #no space
    concatenated = '\t\t'+ concatenated + '] L:rnd\n'
    workfile.write(concatenated)
    workfile.write('\t} ifelse\n')
    workfile.write('} def\n')
    workfile.write('\n')

    # writing epilogue
    workfile.write('/omega\n')
    workfile.write('{\n')
    workfile.write('\tF\n')
    workfile.write('} def\n')
    workfile.write('%%EndResource\n')
    workfile.write('%%EndProlog\n')
    workfile.write('\n')
    workfile.write(f'{data["parameters"]["start"][0]} {data["parameters"]["start"][1]}\n')
    workfile.write(f'{data["parameters"]["start"][2]}\n')
    workfile.write('T:init\n')
    workfile.write('\n')

    workfile.write(n + '\n')
    workfile.write('omega\n')
    workfile.write('%%EOF\n')
    workfile.close()


