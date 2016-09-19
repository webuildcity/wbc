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

function scrollCheck(element, scroller){
    var move = function() {
        var st = $(scroller).scrollTop();
        var ot = $(element).offset().top+300;
        var el = $('#header-right #nav-search');
        if (st> ot){
            el.addClass('fade-in');
        } else {
            el.removeClass('fade-in')
        }
    }
    $(scroller).scroll(move);
    move();
}

// function to load the modal and handle form submussions in modals
function loadModal(modal, button) {
    modal = $(modal)
    $(button).on('click', function(ev) { // for each edit contact url
        ev.preventDefault(); // prevent navigation
        var url = $(this).data('form');
        var title = $(this).data('title') 
        modal.find('.modal-header h3').html(title); // display the modal on url load
        modal.modal('show'); // display the modal on url load
        modal.find('.custom-content').load(url, function(response, status) {
            if ( status == "error" ) {
                modal.find('.custom-content').html("Fehler!");
            }
            modal.modal();
            modal.unbind( "submit" );
            modal.on('submit', 'form', function(e){

                // disable button to prevent double submits
                $(this).find('input[type=submit]').prop('disabled', true);

                e.preventDefault();
                $.ajax({ 
                    type: $(this).attr('method'), 
                    url: url, 
                    data: $(this).serialize(),
                    context: this,
                    success: function(data, status) {
                        if (data.redirect){
                            window.location.href = data.redirect;
                        }
                        else {
                            modal.find('.custom-content').html(data);
                        }
                    },
                    error: function (xhr, ajaxOptions, thrownError) {
                        if(xhr.status==403) {
                            modal.find('.custom-content').html("Keine Berechtigungen für diese Aktion.");
                        }
                    }
                });
            });
        });
        return false; // prevent the click propagation
    });
}

function loadLoginModal(modal, button){
    modal = $(modal);
    $(button).on('click', function(ev) { // for each edit contact url
        ev.preventDefault(); // prevent navigation
        var url = $(this).data('form');
        modal.find('.custom-content').load(url, function(response, status) {
            if ( status == "error" ) {
                $modal.find('.custom-content').html("Fehler!");
            }
            modal.modal();
            modal.modal('show'); // display the modal on url load
//             modal.find('form').unbind( "submit" );

            modal.on('submit', 'form', function(e){

                // disable button to prevent double submits
                $(this).find('input[type=submit]').prop('disabled', true);
                
                e.preventDefault();
                $.ajax({ 
                    type: $(this).attr('method'), 
                    url: $(this).attr("action"), 
                    data: $(this).serialize(),
                    context: this,
                    success: function(data, status) {
                        if (data.redirect){
                            window.location.href = data.redirect;
                        }
                        else {
                            modal.find('.custom-content').html(data);
                        }
                    },
                    error: function (xhr, ajaxOptions, thrownError) {
                        if(xhr.status==403) {
                            modal.find('.custom-content').html("Keine Berechtigungen für diese Aktion.");
                        }
                    }
                });
            });
        });
        return false; // prevent the click propagation
    });
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

//function to load a script. useful if you only want to load a script in certain conditions
function getScript(url, success) {

    var script     = document.createElement('script');
         script.src = url;
    
    var head = document.getElementsByTagName('head')[0],
    done = false;
    
    // Attach handlers for all browsers
    script.onload = script.onreadystatechange = function() {
    
        if (!done && (!this.readyState || this.readyState == 'loaded' || this.readyState == 'complete')) {
        
        done = true;
            
            // callback function provided as param
            success();
            
            script.onload = script.onreadystatechange = null;
            head.removeChild(script);
            
        };
    
    };
    
    head.appendChild(script);

};