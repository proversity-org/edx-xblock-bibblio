
# encoding=utf8

"""XBlock to display content recommendations using the Bibblio API."""

import bibbliothon
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin
from xblockutils.settings import XBlockWithSettingsMixin

# Global variables
fontawesome_js = 'https://use.fontawesome.com/c80492468b.js'

@XBlock.wants('settings')
class BibblioXBlock(XBlock, StudioEditableXBlockMixin, XBlockWithSettingsMixin):
    """
    XBlock to display content recommendations using the Bibblio API
    """
    display_name = String(
        display_name="Display Name",
        help="This name appears in the horizontal navigation at the top of the page.",
        scope=Scope.settings,
        default="Bibblio Recommendations"
    )

    content_item_id = String(
        display_name="Content Item ID",
        help="Bibblio ContentItemId corresponding to the recommendation source video.",
        default='',
        scope=Scope.content
    )

    catalog_id = String(
        display_name="Catalog ID",
        help="[Optional] Bibblio Catalog from which recommendations should load.",
        default='',
        scope=Scope.content
    )

    editable_fields = ('display_name', 'content_item_id', 'catalog_id',)

    block_settings_key = 'bibblio'

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

        settings = self.get_xblock_settings(default={})
        assert settings['client_id'] and settings['client_secret']

        bibbliothon.client_id = settings['client_id']
        bibbliothon.client_secret = settings['client_secret']

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
