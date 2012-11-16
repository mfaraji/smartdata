'''
Created on Nov 15, 2012

@author: mfaraji
'''
from collections import defaultdict
from itertools import combinations

Input=defaultdict(list)

def fill(element,path):
    try:
        with open(path) as file:
            for line in file.readlines():
                if line[0] != '#':
                    Input[element].append(line.rstrip())
    except IOError as e:
            import traceback
            traceback.print_exc()

def go_through(prefix,order,turn,output=None):
    if turn == len(order):
        output.write(prefix+'\n')
        print prefix+"//",
        return
    for word in Input.get(order[turn]):
        go_through(prefix+" "+word, order, turn+1, output)

def generate_command7(args):
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_features']
    print "Generating the output"
    output=open(args.output+'7','w')
    Input = dict.fromkeys(order)
    ns=args.__dict__
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    go_through("", order, 0, output)
    print "Output is available on %" % (args.output+'7')

def generate_command6(args):
    print "Generating the output"
    output=open(args.output+'6','w')
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_features']
    orders = defaultdict(list)
    order['subject'] = ['verb','object','object_description','location','delivery_time','privacy_features']
    order['object_description'] = ['subject','verb','object','location','delivery_time','privacy_features']
    order['location'] = ['subject','verb','object','object_description','delivery_time','privacy_features']
    order['delivery_time'] = ['subject','verb','object','object_description','location','privacy_features']
    order['privacy_features'] = ['subject','verb','object','object_description','location','delivery_time']
    ns=args.__dict__
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    for (k,l) in order:
        print "Eliminating %" % k
        go_through("", l, 0, output)
    print "Output is available on %" % (args.output+'6')

def generate_command3(args):
    print "Generating the output"
    output=open(args.output+'3','w')
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_features']
    orders = defaultdict(list)
    order['object_description'] = ['verb','object','object_description']
    order['subject'] = ['subject','verb','object']
    order['delivery_time'] = ['verb','object','delivery_time']
    order['location'] = ['verb','object','location']
    order['privacy_features'] = ['verb','object','privacy_features']
    ns=args.__dict__
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    for (k,l) in order:
        print "Adding %" % k
        #go_through("", l, 0, output)
    print "Output is available on %" % (args.output+'3')

def generate_command4(args):
    ns=args.__dict__
    output=open(args.output+'4','w')
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_features']
    select_set = ['subject','object_description','location','delivery_time','privacy_features']
    comb=list(combinations(select_set,2))
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    for seq in comb:
        if seq[0] == 'subject':
            new_order = ['subject','verb','object', seq[1]]
        else:
            new_order = ['verb','object']
            new_order.append(seq[0])
            new_order.append(seq[1])
        #print new_order
        go_through("", new_order, 0, output)

def generate_command5(args):
    ns=args.__dict__
    output=open(args.output+'5','w')
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_features']
    select_set = ['subject','object_description','location','delivery_time','privacy_features']
    comb=list(combinations(select_set,2))
    print comb
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    for seq in comb:
        new_order = list(order)
        new_order.remove(seq[0])
        new_order.remove(seq[1])
        go_through("", new_order, 0, output)
