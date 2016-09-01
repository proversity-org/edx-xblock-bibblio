/* Javascript for BibblioXBlock. */
function BibblioXBlock(runtime, element) {
    $(document).ready(function() {
        console.log('ready');

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
            var contentItems = result.contentItems.results;
            var random = Math.floor(Math.random() * contentItems.length);
            var contentItem = contentItems[random];
            $("#loading").hide();
            $("#title").append('Recommendations for <a href="' + contentItem.url + '" target="_blank">' + contentItem.name + '</a>');  
            bib_initRelatedContent("bib_related-content",
                result.token,
                contentItem.contentItemId,
                {
                    stylePreset: "grid-4", // Options: grid-4, box-5, box-6. Default: box-6,
                }
            ); 
        }
    });
}
