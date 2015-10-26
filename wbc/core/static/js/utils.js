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