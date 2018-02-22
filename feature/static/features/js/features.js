$(function () {
    
      // $(".js-create-feature").click(function () {
      //   $.ajax({
      //     url: 'create',
      //     type: 'get',
      //     dataType: 'json',
      //     beforeSend: function () {
      //       $("#modal-book").modal("show");
      //     },
      //     success: function (data) {
      //       $("#modal-book .modal-content").html(data.html_form);
      //     }
      //   });
      // });

      // $("#modal-book").on("submit", ".js-feature-create-form", function () {
      //   var form = $(this);
      //   $.ajax({
      //     url: form.attr("action"),
      //     data: form.serialize(),
      //     type: form.attr("method"),
      //     dataType: 'json',
      //     success: function (data) {
      //       if (data.form_is_valid) {
      //         $("#book-table tbody").html(data.html_book_list);  // <-- Replace the table body
      //         $("#modal-book").modal("hide");  // <-- Close the modal
      //       }
      //       else {
      //         $("#modal-book .modal-content").html(data.html_form);
      //       }
      //     }
      //   });
      //   return false;
      // });

      // $(".js-create-feature").click(function () {
      //   var btn = $(this);  // <-- HERE
      //   $.ajax({
      //     url: btn.attr("data-url"),  // <-- AND HERE
      //     type: 'get',
      //     dataType: 'json',
      //     beforeSend: function () {
      //       $("#modal-book").modal("show");
      //     },
      //     success: function (data) {
      //       $("#modal-book .modal-content").html(data.html_form);
      //     }
      //   });
      // });

      var loadForm = function () {
        var btn = $(this);
        debugger;
        $.ajax({
          url: btn.attr("data-url"),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#modal-book").modal("show");
          },
          success: function (data) {
            $("#modal-book .modal-content").html(data.html_form);
          }
        });
      };
    
      var saveForm = function () {
        var form = $(this);
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              debugger;
              $("#book-table tbody").html(data.html_feature_list);
              $("#modal-book").modal("hide");
            }
            else {
              $("#modal-book .modal-content").html(data.html_form);
            }
          }
        });
        return false;
      };
    
    
      /* Binding */
    
      // Create feature req
      $(".js-create-feature").click(loadForm);
      $("#modal-book").on("submit", ".js-feature-create-form", saveForm);
    
      // Update feature req
      $("#book-table").on("click", ".js-update-feature", loadForm);
      $("#modal-book").on("submit", ".js-feature-update-form", saveForm);

      // Delete feature
      $("#book-table").on("click", ".js-delete-feature", loadForm);
      $("#modal-book").on("submit", ".js-feature-delete-form", saveForm);
    
    });