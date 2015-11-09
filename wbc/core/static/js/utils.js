function getAllNamedSelectors() {
    var ret = {};
    for(var i = 0; i < document.styleSheets.length; i++) {
        var rules = document.styleSheets[i].rules || document.styleSheets[i].cssRules;
        for(var x in rules) {
            if(typeof rules[x].selectorText == 'string') {
                ret[rules[x].selectorText] = rules[x];
            }
        }
    }
    return ret;
}

function getRuleForSelector(selector) {
    var selectors = getAllNamedSelectors();
    return selectors[selector];
}

function moveScroller(anchorSelector, scrollerSelector) {
    var move = function() {
        var scrollTop = $(scrollerSelector).scrollTop();
        var offset = $(anchorSelector).offset();
        var offsetTop = 0;
        if(offset !== undefined) {
            offsetTop = offset.top;
        }

        var anchor = $(anchorSelector);
        if(scrollTop > offsetTop) {
            anchor.addClass('fixed-top')
        } else {
            anchor.removeClass('fixed-top')
        }
    };

    $(scrollerSelector).scroll(move);
    move();
}