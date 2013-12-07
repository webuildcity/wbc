function initSocial() {
    $('body').prepend('<div id="fb-root">');
    $('#facebook').append('<div class="fb-like" data-href="http://buergerbautstadt.de" data-send="false" data-layout="button_count" data-width="450" data-show-faces="true" data-font="verdana"></div>');
    $('#twitter').append('<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://buergerbautstadt.de" data-via="BueBauSta" data-lang="de">Twittern</a>');
    $('#gplus').append('<div id="gplus" class="g-plusone" data-size="medium"></div>');
}
function runSocial() {
    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');

    (function() {
        var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
        po.src = 'https://apis.google.com/js/plusone.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
    })();
}
$(document).ready(function() {
    setTimeout('initSocial()',100);
    setTimeout('runSocial()',200);
});
