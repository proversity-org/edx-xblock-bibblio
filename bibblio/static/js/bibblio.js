/* Javascript for BibblioXBlock. */
function BibblioXBlock(runtime, element) {
    $(document).ready(function() {
    
        $("#loading").hide();
        var handlerUrl = runtime.handlerUrl(element, 'recommendations');

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

        loadRecommendations()

        $('button', element).click(function(eventObject) {
            loadRecommendations()
        });

        function showRecommendations(result) {
            $("#loading").hide();
            var contentItem = result.contentItem;
            var catalogId = result.catalogId;
            if (contentItem.status >= 400) {
                // Something went wrong
            } else {
                initRelatedContent("bib_related-content",
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
