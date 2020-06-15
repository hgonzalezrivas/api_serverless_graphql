from flask import Flask
from flask_graphql import GraphQLView
from utils.schema import schema
from flask_cors import CORS
import utils.database


app = Flask(__name__)
CORS(app)
app.debug = True

default_query = '''
{
    allEmployess {
        edges {
            node {
                id,
                name,
                department {
                    id,
                    name
                },
                role {
                    id,
                    name
                }
            }
        }
    }
}'''.strip()


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run()
