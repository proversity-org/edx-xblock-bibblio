
# encoding=utf8

"""TO-DO: Write a description of what this XBlock is."""

import bibbliothon
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment

# Global variables
bootstrap_css = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
bootstrap_js = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'
fontawesome_js = 'https://use.fontawesome.com/c80492468b.js'
jquery = 'https://code.jquery.com/jquery-1.12.3.min.js'

class BibblioXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the BibblioXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/bibblio.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/bibblio.css"))
        frag.add_css(self.resource_string("static/css/bib-related-content.css"))
        frag.add_css_url(bootstrap_css)
        frag.add_javascript_url(jquery)
        frag.add_javascript_url(bootstrap_js)
        frag.add_javascript_url(fontawesome_js)
        frag.add_javascript(self.resource_string("static/js/bibblio.js"))
        frag.add_javascript(self.resource_string("static/js/bibblio.js"))
        frag.add_javascript(self.resource_string("static/js/underscore-min.js"))
        frag.add_javascript(self.resource_string("static/js/bib-related-content.js"))
        frag.initialize_js('BibblioXBlock')

        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    @XBlock.json_handler
    def recommendations(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        bibbliothon.client_id = 'ff90bfe4'
        bibbliothon.client_secret = '1c2428219c598bcfc6cc26a197afbc47'

        response = bibbliothon.Token.get_access_token()
        access_token = response.get('access_token', None)

        bibbliothon.access_token = access_token
        payload = {
            'name': 'What Mr. Robot\'s Rami Malek Really Snorts in Those Morphine Scenes',
            'url': 'https://www.youtube.com/watch?v=JqONvYXC_MQ', 
            'text': 'Rami Malek has a whole system for his character\'s drug scenes.'
        }

        print payload

        content_item = bibbliothon.Enrichment.create_content_item(payload)
        content_items = bibbliothon.Enrichment.get_content_items()

        return {"token": access_token, "contentItems": content_items}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("BibblioXBlock",
             """<bibblio/>
             """),
            ("Multiple BibblioXBlock",
             """<vertical_demo>
                <bibblio/>
                <bibblio/>
                <bibblio/>
                </vertical_demo>
             """),
        ]
