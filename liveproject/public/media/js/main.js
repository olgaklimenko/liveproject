function update() {
    update_holder = $("#update-holder");
    most_recent = update_holder.find("div:first");
    $.getJSON("/liveupdate/updates-after/" + most_recent.attr('id')+"/",
        function(data) {
            cycle_class = most_recent.hasClass("odd")
                ? "even" : "odd";
            jQuery.each(data, function() {
                update_holder.prepend('<div id="'+this.pk
                    +'"class="update ' +cycle_class
                    +'"><div class="timestamp">'
                    +this.fields.timestamp
                    +'</div><div class="text">'
                    +this.fields.text
                    +'</div><div class="clear"></div></div>'
                );
                cycle_class = (cycle_class == "odd")
                    ? "even" : "odd"
            });                  
        }
    );
}
$(document).ready(function() {
    setInterval("update()", 20000);
})
