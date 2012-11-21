'''
Created on Nov 15, 2012

@author: mfaraji
'''
from collections import defaultdict
from itertools import combinations

Input=defaultdict(list)
order = ['subject','verb','object','object_description','location','delivery_time','privacy_features','vendor']

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
        #print prefix+"//",
        return
    for word in Input.get(order[turn]):
        go_through(prefix+" "+word, order, turn+1, output)
        if turn==0:
           print word
           output.flush()

def generate_command7(args):

    print "Generating the output"
    #order = ['subject','verb','object']
    output_file_name = args.output+'7'
    output=open(output_file_name,'w', 1000)
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
    print "Output is available on %s" % output_file_name

def generate_command6(args):
    print "Generating the output"
    output=open(args.output+'6','w')
    orders = defaultdict(list)
    orders['subject']=['verb','object','object_description','location','delivery_time','privacy_features','vendor']
    orders['object_description']=['subject','verb','object','location','delivery_time','privacy_features','vendor']
    orders['location']=['subject','verb','object','object_description','delivery_time','privacy_features','vendor']
    orders['delivery_time']=['subject','verb','object','object_description','location','privacy_features','vendor']
    orders['privacy_features']=['subject','verb','object','object_description','location','delivery_time','vendor']
    orders['vendor']=['subject','verb','object','object_description','location','delivery_time','privacy_features']
    ns=args.__dict__
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    for word,value in orders.items():
        print "Eliminating %s" % word
        go_through("", value, 0, output)
    print "Output is available on %s" % (args.output+'6')

def generate_command3(args):
    print "Generating commands with 3 elements"
    output=open(args.output+'3','w')
    orders = defaultdict(list)
    orders['object_description'] = ['verb','object','object_description']
    orders['subject'] = ['subject','verb','object']
    orders['delivery_time'] = ['verb','object','delivery_time']
    orders['location'] = ['verb','object','location']
    orders['privacy_features'] = ['verb','object','privacy_features']
    orders['vendor'] = ['verb','object','vendor']
    ns=args.__dict__
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    for (k,l) in orders.items():
        print "Adding %s" % k
        go_through("", l, 0, output)
    print "Output is available on %s" % (args.output+'3')

def generate_command4(args):
    print "Generating commands with 4 elements"
    ns=args.__dict__
    output=open(args.output+'4','w')
    select_set = ['subject','object_description','location','delivery_time','privacy_features','vendor']
    comb=list(combinations(select_set,2))
    for element in order:
        try:
            ns.get(element)
            fill(element,ns.get(element))
        except KeyError as e:
            import traceback
            traceback.print_exc()
    for seq in comb:
        print "Command with %s" % (seq,)
        if seq[0] == 'subject':
            new_order = ['subject','verb','object', seq[1]]
        else:
            new_order = ['verb','object']
            new_order.append(seq[0])
            new_order.append(seq[1])
        #print new_order
        go_through("", new_order, 0, output)

def generate_command5(args):
    print "Generating commands with 5 elements"
    ns=args.__dict__
    output=open(args.output+'5','w')
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
        print "Removing %s elements from the list" % (seq,)
        new_order = list(order)
        new_order.remove(seq[0])
        new_order.remove(seq[1])
        go_through("", new_order, 0, output)
