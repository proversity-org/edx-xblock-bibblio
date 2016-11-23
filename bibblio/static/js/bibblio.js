/* Javascript for BibblioXBlock. */
function BibblioXBlock(runtime, element) {
    $(document).ready(function() {
    
        $("#loading").hide();
        var handlerUrl = runtime.handlerUrl(element, 'recommendations');

        loadRecommendations()

        $('button', element).click(function(eventObject) {
            loadRecommendations()
        });

        function loadRecommendations() {
            $("#loading").show();
            $("#bib_related-content").empty();
            $.ajax({
                type: "POST",
                url: handlerUrl,
                data: JSON.stringify({"hello": "world"}),
                success: showRecommendations
            });
        }

        function showRecommendations(result) {
            $("#loading").hide();
            var contentItem = result.contentItem;
            var catalogId = result.catalogId;
            if (contentItem.status >= 400) {
                // Something went wrong
            } else {
                bib_initRelatedContent("bib_related-content",
                    result.token,
                    contentItem.contentItemId,
                    {
                        stylePreset: "grid-4",
                        catalogueIds: [catalogId],
                        showRelatedBy: true
                    }
                );
            }
        }
    });
}
