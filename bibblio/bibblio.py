
# encoding=utf8

"""TO-DO: Write a description of what this XBlock is."""

import bibbliothon
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

# Global variables
fontawesome_js = 'https://use.fontawesome.com/c80492468b.js'

class BibblioXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    content_item_id = String(
        display_name="Content Item ID",
        help="Will retrieve recommendations based on this ID.",
        default='',
        scope=Scope.content
    )
    catalog_id = String(
        display_name="Catalog ID",
        help="Catalog of the organization (eg. Network Rail).",
        default='',
        scope=Scope.content
    )
    editable_fields = ('content_item_id', 'catalog_id',)

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
        frag.add_javascript_url(fontawesome_js)
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
        content_item_id = self.content_item_id if len(self.content_item_id) > 0 else 'no-content-item-id'
        content_item = bibbliothon.Enrichment.get_content_item(content_item_id)

        return {"token": access_token, "contentItem": content_item, "catalogId": self.catalog_id}

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
