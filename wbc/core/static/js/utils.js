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

function moveScroller(anchor, scroller) {
    var move = function() {
        var st = $(scroller).scrollTop();
        var ot = $(anchor).offset().top;
        var s = $(anchor);
        if(st > ot) {
            s.addClass('fixed-top')
        } else {
            s.removeClass('fixed-top')
        }
    };
    $(scroller).scroll(move);
    move();
}

function scrollCheck(element, scroller){
    console.log(element);
    console.log(scroller);
    var move = function() {
        var st = $(scroller).scrollTop();
        var ot = $(element).offset().top+250;
        var el = $('#nav-search');
        console.log(st)
        console.log(ot)
        if (st> ot){
            el.addClass('fade-in');
        } else {
            el.removeClass('fade-in')
        }
    }
    $(scroller).scroll(move);
    move();
}