import graphene


class SuspiciousType(graphene.ObjectType):
    tstart = graphene.Field(type=graphene.types.DateTime,
                            description='Time the flow was received by the flow collector',
                            resolver=lambda root, *_: root.get('tstart'))
    srcIp = graphene.Field(type=graphene.String,
                           description='Source IP address',
                           resolver=lambda root, *_: root.get('srcip'))
    dstIp = graphene.Field(type=graphene.String,
                           description='Destination IP address',
                           resolver=lambda root, *_: root.get('dstip'))
    srcPort = graphene.Field(type=graphene.Int,
                             description='Source port',
                             resolver=lambda root, *_: root.get('sport', 0))
    dstPort = graphene.Field(type=graphene.Int,
                             description='Destination port',
                             resolver=lambda root, *_: root.get('dport', 0))
    protocol = graphene.Field(type=graphene.String,
                              description="IP protocol")
    inPkts = graphene.Field(type=graphene.types.Int,
                            description='Input packets',
                            resolver=lambda root, *_: root.get('ipkt', 0))
    inBytes = graphene.Field(type=graphene.types.Int,
                             description='Input bytes',
                             resolver=lambda root, *_: root.get('ibyt', 0))
    outPkts = graphene.Field(type=graphene.types.Int,
                             description='Output packets',
                             resolver=lambda root, *_: root.get('opkt', 0))
    outBytes = graphene.Field(type=graphene.types.Int,
                              description='Output bytes',
                              resolver=lambda root, *_: root.get('obyt', 0))
    score = graphene.Field(type=graphene.types.Float,
                           description='Spot ML score',
                           resolver=lambda root, *_: root.get('ml_score', 0))
    rank = graphene.Field(type=graphene.types.Int,
                          description='Spot ML rank',
                          resolver=lambda root, *_: root.get('rank', 0))
    srcIp_isInternal = graphene.Field(type=graphene.types.Int,
                                      description='Internal source IP address context flag',
                                      resolver=lambda root, *_: root.get('srcip_internal'))
    dstIp_isInternal = graphene.Field(type=graphene.types.Int,
                                      description='Internal destionation IP address context flag',
                                      resolver=lambda root, *_: root.get('dstip_internal'))
    srcIp_geoloc = graphene.Field(type=graphene.types.String,
                                  description='Source IP geolocation',
                                  resolver=lambda root, *_: root.get('src_geoloc'))
    dstIp_geoloc = graphene.Field(type=graphene.types.String,
                                  description='Destination IP geolocation',
                                  resolver=lambda root, *_: root.get('dst_geoloc'))
    srcIp_domain = graphene.Field(type=graphene.types.String,
                                  description='Source IP domain',
                                  resolver=lambda root, *_: root.get('src_domain'))
    dstIp_domain = graphene.Field(type=graphene.types.String,
                                  description='Destination IP domain',
                                  resolver=lambda root, *_: root.get('dst_domain'))
    srcIp_rep = graphene.Field(type=graphene.types.String,
                               description='Source IP reputation metadata',
                               resolver=lambda root, *_: root.get('src_rep'))
    dstIp_rep = graphene.Field(type=graphene.types.String,
                               description='Destination IP reputation metadata',
                               resolver=lambda root, *_: root.get('dst_rep'))


flow_types = [SuspiciousType]
