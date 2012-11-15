from smartdata import utils
from smartdata.v1_0 import command
from smartdata.v1_0.command import generate_command

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
@utils.arg('--privacy_settings',metavar='<privacy-settings-file>',
            default='./privacy_settings.txt',help='Defaults to ./privacy_settings.txt')
@utils.arg('--elements',metavar='<elements-number>',
            requires=True,help='Represents number of elements in a command and at least 3')
@utils.arg('--output',metavar='<output-file>',
            default='./output.txt',help='Defaults to ./output.txt')
def do_generate_command(args):
    """Generate full sentence dataset"""
    #order = ['subject','verb','object', 'object_description']
    if args.elements == 7:
        generate_command7(args)
    if args.elements == 6:
        generate_command6(args)
    if args.elements == 5:
