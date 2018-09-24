import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(graphene.String, default_value="stranger"))

    def resolve_hello(self, info, **args):
        return 'Hello ' + args['name']


# package up the schema
spotSchema = graphene.Schema(query=Query)