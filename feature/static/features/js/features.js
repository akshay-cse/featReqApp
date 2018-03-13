$(function () {
      var loadForm = function () {
        var btn = $(this);
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

      var calMaxPriorityNoForGivenClient = function(clientId){
        debugger;
        var client = $(this);
        $.ajax({
          url: 'client/'+clientId+'/maxPriorityAvail/',
          type: 'POST',
          dataType: 'json',
          success: function (data) {
            $("#id_client").val(data['feat_priority__max'])
          }
        });
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

      var maxFeaturePriorityAvail = function(){
        var clientId = $("#id_client").val();
        $("#id_client").change(calMaxPriorityNoForGivenClient(1));
        if(clientId!=""){
          
        }
        
      }

    });