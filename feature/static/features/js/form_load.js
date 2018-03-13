$(function () {
    var calMaxPriorityNoForGivenClient = function(clientId){
      $.ajax({
        url: 'client/'+clientId+'/maxPriorityAvail/',
        type: 'POST',
        dataType: 'json',
        success: function (data) {
          debugger;
          $("#id_feat_priority").val(data['feat_priority__max'])
        }
      });
    };
  
    /* Binding */
      $("#id_client").change(function(){
        debugger;
        var clientId = $("#id_client").val();
        if(clientId!=""){
            calMaxPriorityNoForGivenClient(clientId)
        }
      });
    

  });