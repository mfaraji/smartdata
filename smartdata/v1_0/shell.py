from smartdata import utils
from smartdata.v1_0 import command
from smartdata.v1_0.command import *

@utils.arg('--subject',metavar='<subject-file>',
           default='./subject.txt',help='Defaults to ./subject.txt')
@utils.arg('--verb',metavar='<verb-file>',
            default='./verb.txt',help='Defaults to ./verb.txt')
@utils.arg('--object',metavar='<object-file>',
            default='./object.txt',help='Defaults to ./object.txt')
@utils.arg('--object_description',metavar='<object-description-file>',
            default='./object_description.txt',help='Defaults to ./object_description.txt')
@utils.arg('--delivery_time',metavar='<delivery-time-file>',
            default='./delivery_time.txt',help='Defaults to ./delivery_time.txt')
@utils.arg('--location',metavar='<location-file>',
            default='./location.txt',help='Defaults to ./location.txt')
@utils.arg('--privacy_features',metavar='<privacy-features-file>',
            default='./privacy_features.txt',help='Defaults to ./privacy_features.txt')
@utils.arg('--vendor',metavar='<vendor-file>',
            default='./vendor.txt',help='Defaults to ./vendor.txt')
@utils.arg('--elements',metavar='<elements-number>',
            required=True,help='Represents number of elements in a command and at least 3')
@utils.arg('--output',metavar='<output-file>',
            default='./output.txt',help='Defaults to ./output.txt')
def do_generate_command(args):
    """Generate full command dataset"""
    if args.elements == '7':
        generate_command7(args)
    elif args.elements == '6':
        generate_command6(args)
    elif args.elements == '5':
        generate_command5(args)
    elif args.elements == '4':
        generate_command4(args)
    elif args.elements == '3':
        generate_command3(args)
