# lib imports
import graphene
from flask import Flask
from flask_graphql import GraphQLView
# local imports
from schema import spotSchema


# Flask configs
app = Flask(__name__)
app.debug = True

# This is to enable the GraphQL GUI
app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql',
                                               schema=spotSchema,
                                               graphiql=True))

#app.route("/", methods=['POST'])

if __name__ == '__main__':
    app.run(port=8880)
