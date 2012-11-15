'''
Created on Nov 15, 2012

@author: mfaraji
'''
from collections import defaultdict

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
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_settings']
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
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_settings']
    orders = defaultdict(list)
    order['subject'] = ['verb','object','object_description','location','delivery_time','privayc_settings']
    order['object_description'] = ['subject','verb','object','location','delivery_time','privayc_settings']
    order['location'] = ['subject','verb','object','object_description','delivery_time','privacy_settings']
    order['delivery_time'] = ['subject','verb','object','object_description','location','privacy_settings']
    order['privacy_settings'] = ['subject','verb','object','object_description','location','delivery_time']
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
    order = ['subject','verb','object','object_description','location','delivery_time','privacy_settings']
    orders = defaultdict(list)
    order['object_description'] = ['verb','object','object_description']
    order['subject'] = ['subject','verb','object']
    order['delivery_time'] = ['verb','object','delivery_time']
    order['location'] = ['verb','object','location']
    order['privacy_settings'] = ['verb','object','privayc_settings']
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
        go_through("", l, 0, output)
    print "Output is available on %" % (args.output+'3')


