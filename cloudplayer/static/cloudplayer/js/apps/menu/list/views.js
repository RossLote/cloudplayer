CloudPlayer.module("MenuApp.List", function(List, CloudPlayer, Backbone, Marionette, $, _){
    
    List.MenuItem = Marionette.ItemView.extend({
        template : '#menu-list-item-tmpl',
        tagName : 'li'
    });
    
    List.Menu = Marionette.CompositeView.extend({
        template : '#menu-list-tmpl',
        childView : List.MenuItem,
        childViewContainer : 'ul'
    });

});