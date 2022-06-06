$('.tab-item').on('click', function () {
  $([$(this).parent('.tabs-nav').siblings('.tabs-content').children('.tab')[+$(this).data('num')]]).addClass("active").siblings().removeClass("active");
  $(this).addClass("active").siblings().removeClass("active");
});