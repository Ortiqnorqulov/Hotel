$(document).ready(function () {

    // JQUERY MASK FOR PHONE

    jQuery(document).ready(function () {
        $(".phonenumber").mask("+998 (11) 111 11 11");
    });

    // MOBILE MENU OPEN

    $(".mobile-button").click(function () {
        $(".navigation").toggleClass("active");
    });

    // BOOK FORM SCRIPTS

    $(".input").click(function () {
        $(this).toggleClass("opened");
    });
    $(".input-item").click(function () {
        var text = $(this).text();
        $(this).parent().parent().siblings(".drop").val(text);
    });

    $(".mobile-book-call").click(function () {
        $('.introduction-form').toggleClass("opened");
    });
    $(".book-form-close").click(function () {
        $('.introduction-form').toggleClass("opened");
    });


    // MODAL OPEN

    $(".leaveapp-modal-btn").click(function () {
        $(".leaveapp-modal").addClass("active");
    });
    $(".modal-close").click(function () {
        $(this).parent().removeClass("active");
    });


    // LANGUAGE DROPDOWN

    $(".lang-drop").click(function () {
        $(".lang").toggleClass("opened");
    });
    $(".modal-close").click(function () {
        $(this).parent().removeClass("active");
    });


    // NEWS INPUT CHANGER

    $(".leaveapp-modal-btn.newsin").click(function () {
        var title = $(this).attr("data-title");
        $('#newsin-input-type').val(title);
    });

    // $(".measuring-modal-btn").click(function () {
    //     $(".measuring-modal").addClass("active");
    // });

    // CAROUSELS

    $(".introduction-carousel, .aboutshort-carousel, .hotel_rooms-carousel, .hotelrooms-carousel").owlCarousel({
        items: 1,
        dots: false,
        nav: true,
        loop: true,
        // autoplay: true,
        smartSpeed: 1000,
        mouseDrag: true,
        touchDrag: true
    });

    $(".inner_room-carousel").owlCarousel({
        items: 1,
        dots: false,
        nav: false,
        loop: true,
        // autoplay: true,
        smartSpeed: 1000,
        mouseDrag: true,
        touchDrag: true
    });

    $('.nextow').click(function () {
        $('.inner_room-carousel').trigger('next.owl.carousel');
    })
    $('.prevow').click(function () {
        $('.inner_room-carousel').trigger('prev.owl.carousel');
    })


    $(".spec_offer-carousel").owlCarousel({
        items: 2,
        dots: false,
        nav: true,
        loop: true,
        // autoplay: true,
        smartSpeed: 1000,
        mouseDrag: true,
        touchDrag: true,
        responsive: {

            0: {

                items: 1

            },

            768: {

                items: 2

            },

        }
    });

});

// IMAGE AUTO ALT

$(document).ready(function () {
    $("img").each(function () {
        var $img = $(this);
        var filename = $img.attr("src");
        if (typeof attr == typeof undefined || attr == false) {
            $img.attr(
                "alt",
                filename.substring(
                    filename.lastIndexOf("/") + 1,
                    filename.lastIndexOf(".")
                )
            );
        }
    });
});