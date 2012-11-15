from smartdata import utils

@utils.arg('--subject',metavar='<subject-file>',
           default='subject.txt',help='Defaults to verb.txt')
@utils.arg('--verb',metavar='<verb-file>',
            default='verb.txt',help='Defaults to verb.txt')
@utils.arg('--object',metavar='<object-file>',
            default='object.txt',help='Defaults to object.txt')
@utils.arg('--object_description',metavar='<object-description-file>',
            default='object_description.txt',help='Defaults to object_description.txt')
@utils.arg('--delivery_time',metavar='<delivery-time-file>',
            default='delivery_time.txt',help='Defaults to delivery_time.txt')
@utils.arg('--location',metavar='<location-file>',
            default='location.txt',help='Defaults to location.txt')
def do_generate_sentence(kc, args):
    """Generate full sentence dataset"""
    print "asdasdas"
#    endpoint = kc.endpoints.create(args.region,
#                                   args.service_id,
#                                   args.publicurl,
#                                   args.adminurl,
#                                   args.internalurl)
