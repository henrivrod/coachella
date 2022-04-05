$(document).ready(function () {
    let i = 0
    let j = 0
    $("#addtent").click(function () {
        if (i < 1) {
            i += 1;
            $("#tent_id").append("<div><input type='text' name='tent_identry' placeholder = 'tent id'></div>");
            //$("#tent_id").append("<label for='tent_identry' id='tentid_warning'></label>");
            $("#stage_id").append("<div><input type='text' name='stage_identry' placeholder = 'stage id'></div>");
            //$("#stage_id").append("<label for='stage_identry' id='stageid_warning'></label>");
            $("#num_workers").append("<div><input type='text' name='num_workersentry' placeholder = 'Number of Workers'></div>");
            //$("#num_workers").append("<label for='num_workersentry' id='numworkerswarning'></label>");
            $("#tentbutton").append("<input type='submit' value='Submit'>");
            $("#addbuttontent").empty();
            $("#itemhead").empty();
            $("#addbuttonitem").empty();
        }
    });

    $("#additem").click(function () {
        if (j < 1) {
            j += 1;
            $("#item_id").append("<div><input type='text' name='item_identry' placeholder = 'item id'></div>");
            //$("#item_id").append("<label for='item_identry' id='itemid_warning'></label>");
            $("#item_tent_id").append("<div><input type='text' name='item__tentidentry' placeholder = 'tent id'></div>");
            //$("#item_tent_id").append("<label for='item_tentidentry' id='item_tentid_warning'></label>");
            $("#item_name").append("<div><input type='text' name='item_nameentry' placeholder = 'item name'></div>");
            //$("#item_name").append("<label for='item_nameentry' id='itemname_warning'></label>");
            $("#item_type").append("<div><input type='text' name='item_typeentry' placeholder = 'item type'></div>");
            //$("#item_type").append("<label for='item_typeentry' id='itemtype_warning'></label>");
            $("#num_remaining").append("<div><input type='text' name='num_remainingentry' placeholder = 'Number remaining'></div>");
            //$("#num_remaining").append("<label for='num_remainingentry' id='numremainingwarning'></label>");
            $("#price").append("<div><input type='text' name='price_entry' placeholder = 'price'></div>");
            //$("#price").append("<label for='price_entry' id='price_warning'></label>");
            $("#itembutton").append("<input type='submit' value='Submit'>");
            $("#addbuttonitem").empty();
            $("#tenthead").empty();
            $("#addbuttontent").empty();
        }
    });

});