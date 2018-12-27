# lib imports
import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS, cross_origin
# local imports
from schema import schemaOA


# Flask configs
app = Flask(__name__)
cors = CORS(app)
app.debug = True

# This is to enable the GraphQL GUI
app.add_url_rule('/oa',
                 view_func=GraphQLView.as_view('Operational Analytics',
                                               schema=schemaOA,
                                               graphiql=True))

#app.route("/", methods=['POST'])

if __name__ == '__main__':
    app.run(port=8880,
            host='0.0.0.0')
