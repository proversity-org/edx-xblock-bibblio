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
            var catalogIds = 'catalogIds' in result ? result.catalogIds : null;
            var userId = 'userId' in result ? result.userId : null;
            if (contentItemId) {
                var configuration = {
                    stylePreset: "bib--grd-4 bib--wide",
                    showRelatedBy: true
                }

                if (userId) { configuration['userId'] = userId; }
                if (catalogIds) {
                    configuration['catalogueIds'] = [catalogIds];
                }
                
                Bibblio.initRelatedContent(bibblioContentId,
                    recommendationKey,
                    contentItemId,
                    configuration
                );
            } else {
                var msg = "<p>No content item id provided.</p>";
                $("#" + bibblioContentId).append(msg);
            }
        }
    });
}
