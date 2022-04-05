$(document).ready(function () {
    let i = 0
    let j = 0
    $("#addtent").click(function () {
        if (i < 1) {
            i += 1;
            $("#stage_id").append("<label for='stage_identry'>Stage ID:</label><br>");
            $("#stage_id").append("<div><input type='number' name='stage_identry' placeholder = 'stage id' min = '1' max = "+stagecount+"'></div>");
            $("#num_workers").append("<label for='num_workersentry'>Number of Workers: </label>");
            $("#num_workers").append("<div><input type='number' name='num_workersentry' placeholder = 'Number of Workers' min = '1' max = '1000'></div>");
            $("#tentbutton").append("<input type='submit' value='Submit'>");
            $("#addbuttontent").empty();
            $("#itemhead").empty();
            $("#addbuttonitem").empty();
        }
    });

    

    $("#additem").click(function () {
        if (j < 1) {
            j += 1;
            $("#item_tent_id").append("<div><input type='text' name='item__tentidentry' placeholder = 'tent id'></div>");
            //$("#item_tent_id").append("<label for='item_tentidentry' id='item_tentid_warning'></label>");
            $("#item_name").append("<div><input type='text' name='item_nameentry' placeholder = 'item name'></div>");
            //$("#item_name").append("<label for='item_nameentry' id='itemname_warning'></label>");
            $("#item_type").append("<div id ='dropdownmerch'><label for='merchitemtype'>Choose Type:</label><select name='merchitemtype'><option value='shirt'>Shirt</option><option value='hoodie'>Hoodie</option><option value='sweatpants'>Sweatpants</option><option value='hat'>Hat</option><option value='other'>Other</option></select></div>");
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