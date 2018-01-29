/* Javascript for BibblioXBlock. */
function BibblioXBlock(runtime, element, data) {
    $(document).ready(function() {
    
        var handlerUrl = runtime.handlerUrl(element, 'recommendations');
        var loadingId = "loading-" + data.xblockId;
        var bibblioContentId = "bib_related-content-" + data.xblockId;

        function loadRecommendations() {
            $("#" + loadingId).show();
            $("#" + bibblioContentId).empty();
            $.ajax({
                type: "POST",
                url: handlerUrl,
                data: JSON.stringify({"hello": "world"}),
                dataType: "json",
                success: showRecommendations
            });
        }

        loadRecommendations()

        function showRecommendations(result) {
            $("#" + loadingId).hide();
            var recommendationKey = result.recommendationKey;
            var contentItemId = 'contentItemId' in result ? result.contentItemId : null;
            var catalogIds = 'catalogIds' in result ? result.catalogIds : [];
            var userId = 'userId' in result ? result.userId : null;
            var customUniqueIdentifier = 'customUniqueIdentifier' in result ? result.customUniqueIdentifier : null;
            if (contentItemId || customUniqueIdentifier) {
                var configuration = {
                    targetElementId: bibblioContentId,
                    recommendationKey: recommendationKey,
                    styleClasses: "bib--grd-4 bib--wide"
                }

                if (userId) { configuration['userId'] = userId; }
                if (contentItemId) {
                    configuration['contentItemId'] = contentItemId;
                }

                if (customUniqueIdentifier) {
                    configuration['customUniqueIdentifier'] = customUniqueIdentifier;
                    configuration['autoIngestion'] = true;
                }

                if (catalogIds) {
                    configuration['catalogueIds'] = catalogIds;
                }
                
                Bibblio.initRelatedContent(configuration);
            } else {
                var msg = "<p>No content item id or custom unique identifier provided.</p>";
                $("#" + bibblioContentId).append(msg);
            }
        }
    });
}
