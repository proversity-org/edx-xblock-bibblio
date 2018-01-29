
# -*- coding: utf-8 -*-
#
""" Bibblio XBlock """

import logging
import pkg_resources

from django.contrib.auth.models import User

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblock.validation import ValidationMessage
from xblockutils.studio_editable import StudioEditableXBlockMixin
from xblockutils.settings import XBlockWithSettingsMixin

from .utils import _

logger = logging.getLogger(__name__)


@XBlock.wants('settings')
class BibblioXBlock(StudioEditableXBlockMixin, XBlock, XBlockWithSettingsMixin):
    """
    XBlock to display content recommendations using the Bibblio API
    """
    display_name = String(
        display_name=_("Display Name"),
        help=_("Name of the component"),
        scope=Scope.settings,
        default=_("Bibblio Recommendations")
    )

    content_item_id = String(
        display_name=_("Content Item ID"),
        help=_(
            "The Bibblio contentItemId of the article (or other piece of "
            "content) in order to retrieve content recommendations."
        ),
        default="",
        scope=Scope.content
    )

    custom_unique_identifier = String(
        display_name=_("Custom Unique Identifier"),
        help=_(
            "The Bibblio customUniqueIdentifier is used instead of the Content Item ID. "
            "This unique identifier needs to be provided when creating a Content Item in Bibblio. "
            "To auto ingest content from Bibblio the custom unique idenfifier needs to exist."
        ),
        default="",
        scope=Scope.content
    )

    catalog_ids = String(
        display_name=_("Catalog IDs"),
        help=_(
            "[Optional] Bibblio Catalogs that recommendations should draw "
            "from, separate by comma."
        ),
        default="",
        scope=Scope.content
    )

    editable_fields = ('display_name', 'content_item_id', 'catalog_ids', 'custom_unique_identifier',)

    block_settings_key = 'bibblio'

    def validate_field_data(self, validation, data):
        """
        Validate that the content_item_id is set.
        """
        if len(data.content_item_id) == 0:
            logger.error("Content Item ID is required.")
            validation.add(
                ValidationMessage(
                    ValidationMessage.ERROR,
                    u"Content Item ID is required."
                )
            )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    @XBlock.supports("multi_device")
    def student_view(self, context=None):
        """
        The primary view of the BibblioXBlock, shown to students
        when viewing courses.
        """
        idArray = self.scope_ids.usage_id._to_string().split('@')
        xblock_id = idArray[len(idArray) -1]
        html = self.resource_string("static/html/bibblio.html")
        frag = Fragment(html.format(self=self, xblock_id=xblock_id))
        frag.add_css(self.resource_string("static/css/bibblio.css"))
        frag.add_css(
            self.resource_string("public/css/bib-related-content.css")
        )

        frag.add_javascript_url(
            self.runtime.local_resource_url(
                self, 'public/js/underscore-min.js'
            )
        )

        frag.add_javascript_url(
            self.runtime.local_resource_url(
                self, 'public/js/bib-related-content.js'
            )
        )

        frag.add_javascript(self.resource_string("static/js/bibblio.js"))
        frag.initialize_js('BibblioXBlock', {
            'xblockId': xblock_id
        })

        return frag

    @XBlock.json_handler
    def recommendations(self, data, suffix=''):
        """
        Get Bibblio recommendations based on the content_item_id
        """

        # Make sure the Bibblio recommendation key is set on settings
        settings = self.get_xblock_settings(default={})
        if 'recommendation_key' not in settings:
            logger.error('No recommendation_key set, unable to contact Bibblio')
            return {}

        response = { "recommendationKey": settings['recommendation_key'] };

        # Add the content_item_id
        if len(self.content_item_id) > 0:
            response["contentItemId"] = self.content_item_id

        # Add the catalog_ids
        if len(self.catalog_ids) > 0:
            response["catalogIds"] = self.catalog_ids

        if len(self.custom_unique_identifier) > 0:
            response["customUniqueIdentifier"] = self.custom_unique_identifier

        # Add the user_id
        user_id = None
        try:
            user =\
                self.runtime.get_real_user(self.runtime.anonymous_student_id)
            user_id = user.id
        except Exception as e:
            logger.error('Studio cannot access self.runtime.get_real_user')

        if user_id:
            response["userId"] = user_id

        return response
