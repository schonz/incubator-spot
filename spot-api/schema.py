import graphene
# local imports
from oa.flow import NetflowQueryType


class QueryOA(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(graphene.String, default_value="stranger"))

    flow = graphene.Field(NetflowQueryType)

    def resolve_hello(self, info, **args):
        return 'Hello ' + args['name']

    def resolve_flow(self, info, **args):
        return NetflowQueryType


# package up the schema
schemaOA = graphene.Schema(query=QueryOA)