$(window).trigger('hashchange').scroll(NavCheck);
NavCheck()
function NavCheck() {
    if ($(window).scrollTop() == 0) {
        $('.navigation').addClass('index');
        $('#logo_image').attr('src', '/assets/icons/logo-white.svg')
    } else {
        $('.navigation').removeClass('index');
        $('#logo_image').attr('src', '/assets/icons/logo.svg')
    }

    if ($(window).width() < 992) {
        $('.navigation').removeClass('index');
        $('#logo_image').attr('src', '/assets/icons/logo.svg')
    }
}