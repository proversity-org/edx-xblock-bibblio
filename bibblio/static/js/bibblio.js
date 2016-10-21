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
            $("#title").empty();
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
                $("#title").append('Content Item not found.');
            } else {
                $("#title").append('Recommendations for <a href="' + contentItem.url + '" target="_blank">' + contentItem.name + '</a>');  
                bib_initRelatedContent("bib_related-content",
                    result.token,
                    contentItem.contentItemId,
                    {
                        stylePreset: "grid-4",
                        catalogueIds: [catalogId]
                    }
                ); 
            }
        }
    });
}
