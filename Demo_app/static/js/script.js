$(document).ready(function () {
  let loadForm = function () {
    var btn = $(this);
    $.ajax({
      type: "get",
      url: btn.attr("data-url"),
      dataType: "json",
      beforeSend: function () {
        $("#modal-product .modal-content").html("");
        $("#modal-product").modal("show");
      },
      success: function (data) {
        $("#modal-product .modal-content").html(data.html_form);
      },
    });
  };

  var save_form = function () {
    var form = $(this);
    $.ajax({
      type: form.attr("method"),
      url: form.attr("action"),
      data: form.serialize(),
      dataType: "json",
      success: function (data) {
        if (data.form_is_valid()) {
          $("$product-table tbody").html(data.html_product_list);
          $("#modal-product").modal("hide");
        } else {
          $("#modal-product .modal-content").html(data.html_form);
        }
      },
    });
  };

  $(".js-criar-produto").click(loadForm);
  $("#modal-produto").on("submit", "js-product-create-form", save_form);
});
